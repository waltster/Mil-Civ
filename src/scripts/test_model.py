from inferenceutils import *
import os
import pandas as pd

def main():
    labelmap_path = "../model/labelmap.pbtxt"
    category_index = label_map_util.create_category_index_from_labelmap(labelmap_path, use_display_name=True)
    tf.keras.backend.clear_session()

    print("Beginning to load the model...")
    model = tf.saved_model.load(f'../model/inference_graph/saved_model')
    print("Done loading model.")

    test = pd.read_csv('../data/test_labels.csv')
    #Getting 3 random images to test
    images = test.sample(n=3)["filename"] #['../test.jpg']

    for image_name in images:
      image_np = load_image_into_numpy_array("../data/images/" + image_name)
      output_dict = run_inference_for_single_image(model, image_np)
      vis_util.visualize_boxes_and_labels_on_image_array(
          image_np,
          output_dict['detection_boxes'],
          output_dict['detection_classes'],
          output_dict['detection_scores'],
          category_index,
          min_score_thresh=0.5, # Minimum score to show the box.
          instance_masks=output_dict.get('detection_masks_reframed', None),
          use_normalized_coordinates=True,
          line_thickness=8)

      im = Image.fromarray(image_np)
      display(im)
      
if __name__ == "__main__":
    main()
