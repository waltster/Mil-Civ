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
import time

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

def use_model(image):
    global model
    global category_index

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

    classes = output_dict['detection_classes']
    scores = output_dict['detection_scores']

    return im, [{'class':category_index.get(value)['name'],'score':str(scores[index])}
        for index,value in enumerate(classes)
            if scores[index] > 0.5
    ]

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
@api.route('/process', methods=['POST'])
def process_image():
    if request.method == 'POST':
        if request.data is None:
            return {"error": "400"}

        processed_image = None

        try:
            image = request.json
            image = image["image"]


            decoded_image = decode_base64_as_image(bytes(image, encoding='utf-8'))
            begin_time = time.time()
            processed_image, detected_classes = use_model(decoded_image)
            end_time = time.time()
            encoded_image = encode_image_as_base64(processed_image)
            encoded_image = encoded_image.decode("utf-8")

            total_time = round(end_time - begin_time, 4)

            return make_response(jsonify({"image": f"{encoded_image}", "stats": detected_classes, "time": total_time}), 200)
        except Exception as e:
            print(f"An exception occured. Sending 400: {e}")
            return make_response(jsonify({"error": "Unable to process image"}), 400)

        return make_response(jsonify({"error": "Unable to process image"}), 400)

    else:
        return make_response(jsonify({"error": "Only GET supported"}), 400)

if __name__ == "__main__":
    load_model()
    api.run()
