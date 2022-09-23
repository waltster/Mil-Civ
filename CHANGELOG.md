# Changelog

# 0.0
* Added Changelog
* Added `src/model/content/labelmap.pbtxt` - This provides the labels and classification numbers for each of the classifications in the dataset. (see `src/data/demo_date_gatherer` notebook for more information)
* Added `notebooks` directory to store utility notebooks
* Added `src/notebooks/Generate TF Record.ipynb` - A notebook for generating TF records to train with
* Added `src/notebooks/Demo Data Gatherer.ipynb` - A notebook for example Python to associate label data with image data
* Modified `src/data/train_labels.csv`, removing non-existent entries
