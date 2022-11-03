# Simple model server: acts like a REST API and processes images.
from base64 import b64encode, b64decode
from PIL import Image
from urllib.parse import unquote
import io
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

api = Flask(__name__)
CORS(api)

# TODO: return modified image
def use_model(image):
    return image

################################################################################
# Image Encoding/Decoding stuff                                                #
################################################################################
def decode_base64_as_image(b_in):
    image_data = b64decode(b_in)
    image = Image.open(io.BytesIO(image_data))
    return image

def encode_image_as_base64(image_in):
    image_byte_array = io.BytesIO()
    image_in.save(image_byte_array, format=image_in.format)
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

            return make_response(jsonify({"image": f"{encoded_image}"}), 200)
        except Exception as e:
            print(f"An exception occured. Sending 400: {e}")
            return make_response(jsonify({"error": "Unable to process image"}), 400)

        return make_response(jsonify({"error": "Unable to process image"}), 400)

    else:
        return make_response(jsonify({"error": "Only GET supported"}), 400)

if __name__ == "__main__":
    api.run()
