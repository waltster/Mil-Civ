# Simple model server: acts like a REST API and processes images.
from base64 import b64encode, b64decode
from PIL import Image
from urllib.parse import unquote
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from inferenceutils import *
import io
import os
import pandas as pd
import tensorflow as tf

api = Flask(__name__)
CORS(api)

model = None
category_index = None

def load_model():
    global model
    global category_index

    labelmap_path = "../model/labelmap.pbtxt"
    category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)
    tf.keras.backend.clear_session()

    print("Beginning to load the model...")
    model = tf.saved_model.load(f'../model/inference_graph/saved_model')
    print("Done loading model.")

# TODO: return modified image
def use_model(image):
    global model

    print("Running inference...")
    image_np = reshape(image)

    output_dict = run_inference_for_single_image(model, image_np)
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        output_dict['detection_boxes'],
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        min_score_thresh=0.5,
        instance_masks=output_dict.get('detection_masks_reframed', None),
        use_normalized_coordinates=True,
        line_thickness=6
    )


    im = Image.fromarray(image_np)

    print(output_dict['detection_classes'])

    return im

################################################################################
# Image Encoding/Decoding stuff                                                #
################################################################################
def decode_base64_as_image(b_in):
    image_data = b64decode(b_in)
    image = Image.open(io.BytesIO(image_data))
    return image

def encode_image_as_base64(image_in):
    image_byte_array = io.BytesIO()
    image_in.save(image_byte_array, format='PNG')
    image_byte_array = image_byte_array.getvalue()

    base64_data = b64encode(image_byte_array)
    return base64_data

################################################################################
# Routes and Web-Related stuff                                                 #
################################################################################
# Basic ping method to check online status
@api.route('/', methods=['GET'])
def ping():
    return json.dumps({"status": "online"})

# Method to process image.
# Accepts an image in Base-64, processes it using the model, then
# sends back an image with the detected objects highlighted.
@api.route('/process', methods=['GET'])
def process_image():
    if request.method == 'GET':
        if request.args is None or request.args.get("image") is None:
            return {"error": "400"}

        processed_image = None

        try:
            image = request.args.get("image")
            decoded_image = decode_base64_as_image(bytes(image, encoding='utf-8'))
            processed_image = use_model(decoded_image)
            encoded_image = encode_image_as_base64(processed_image)
            encoded_image = encoded_image.decode("utf-8")

            return make_response(jsonify({"image": f"{encoded_image}", "stats": ""}), 200)
        except Exception as e:
            print(f"An exception occured. Sending 400: {e}")
            return make_response(jsonify({"error": "Unable to process image"}), 400)

        return make_response(jsonify({"error": "Unable to process image"}), 400)

    else:
        return make_response(jsonify({"error": "Only GET supported"}), 400)

if __name__ == "__main__":
    load_model()
    api.run()
