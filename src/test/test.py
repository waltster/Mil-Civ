# Model tester, providing various data points for graphing and drawing conclusions about performance.
from PIL import Image
from inferenceutils import *
import io
import os
import pandas as pd
import tensorflow as tf
import time
import csv

# Loads saved model into memory.
# @return a tuple of (model, category_index)
def load_model():
    print("Beginning load model function...")
    labelmap_path = "../model/labelmap.pbtxt"
    category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)
    tf.keras.backend.clear_session();

    print("Beginning to load model...")
    model = tf.saved_model.load("../model/inference_graph/saved_model")
    print("Done loading model")

    return (model, category_index)

def main():
    (model, category_index) = load_model()

    test = pd.read_csv("../data/test_labels.csv")
    samples = test.sample(n=90)
    images = samples["filename"]
    classifications = samples["class"]
    widths = samples["width"]
    heights = samples["height"]

    # The goal is for the model to detect civilian vehicles.
    # A true positive is correctly perceiving a civilian vehicle
    # A true negative is correctly _not_ identifying a civilian vehicle
    # A false positive is identifying anything incorrect as a civilian vehicle
    # A false negative is failing to identify a civilian vehicle
    data = {
        "num": 0,
        "true_positive": 0,
        "false_positive": 0,
        "true_negative": 0,
        "false_negative": 0,
        "time": [],
        "image_sizes": []
    }

    for i in range(len(samples)):
        image_name = images.iloc[i]
        image_classification = classifications.iloc[i]
        image_size = widths.iloc[i] * heights.iloc[i]

        begin_time = time.time()
        image_np = load_image_into_numpy_array(f"../data/images/{image_name}")
        output_dict = run_inference_for_single_image(model, image_np)
        vis_util.visualize_boxes_and_labels_on_image_array(
            image_np,
            output_dict["detection_boxes"],
            output_dict["detection_classes"],
            output_dict["detection_scores"],
            category_index,
            min_score_thresh=0.5,
            instance_masks=output_dict.get("detection_masks_reframed", None),
            use_normalized_coordinates=True,
            line_thickness=6
        )
        end_time = time.time()
        total_time = end_time - begin_time


        classes = output_dict["detection_classes"]
        scores = output_dict["detection_scores"]

        highest_class_number = classes[np.argmax(scores)]
        highest_class_name = category_index.get(highest_class_number)["name"]

        data["num"] += 1
        data["time"].append(total_time)
        data["image_sizes"].append(image_size)

        if highest_class_name == image_classification:
            # True positive condition
            if "civilian" in image_classification:
                data["true_positive"] += 1
            elif "military" in image_classification:
                data["true_negative"] += 1
            else:
                data["false_negative"] += 1
        else:
            if "civilian" in highest_class_name and "military" in image_classification:
                data["false_positive"] += 1
            else:
                data["false_negative"] += 1

    print("\nOutput:")
    print(f"= True Positive: {data['true_positive']} ({data['true_positive'] / data['num'] * 100}%)")
    print(f"= True Negative: {data['true_negative']} ({data['true_negative'] / data['num'] * 100}%)")
    print(f"= False Positive: {data['false_positive']} ({data['false_positive'] / data['num'] * 100}%)")
    print(f"= False Negative: {data['false_negative']} ({data['false_negative'] / data['num'] * 100}%)")
    print(f"= Total Data Points: {data['num']}")
    print(f"= Total Time: {sum(data['time'])}")
    print(f"= Average Time: {(sum(data['time']) / len(data['time']))}")

    with open("./results.csv", "w") as f:
        writer = csv.writer(f)

        writer.writerow(["index", "image_size", "time_to_process"])

        for i in range(len(data["time"])):
            writer.writerow([i, data["image_sizes"][i], data["time"][i]])

if __name__ == "__main__":
    main()
