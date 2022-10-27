# CSCE-585 Project
## Contents
* [Dependencies](#dependencies)
  * [Installing Key Dependencies](#key_dependencies)
  * [Installing Auxillary Dependencies](#aux_dependencies)
* [Guided Command Line](#guided_cmd)
* [Running the Provided Notebooks](#notebooks)
* [Directory Structure](#dir_structure)
* [Branch Structure](#branch_structure)
* [Authors](#authors)
* [Links](#links)

## <span id="dependencies"></span> Dependencies
### <span id="key_dependencies"></span> Installing Key Dependencies

* `git`
* `grpc`
* `python` v3 - [Install Python](https://www.python.org/) from this link.
* `wget`

On macOS, these can be automatically installed using the `mac_helper.sh` script. Try running `bash mac_helper.sh install` to install them.

### <span id="aux_dependencies"></span> Installing Auxillary Dependencies
```sh
$ python -m ensurepip --upgrade # Install pip if it was not installed automatically
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install tensorflow-object-detection-api
$ pip install notebook
$ pip install opencv-python==4.6.0.66
$ pip install opencv-python-headless==4.6.0.66
$ pip install protobuf==3.19
```

If you encounter an error with the `python` or `pip` command not found, try running the below, and alias the reverse if you have the opposite problem.
```sh
$ alias python=python3
$ alias pip=pip3
```

## <span id="guided_cmd"></span> Option 1: Guided Command-Line
### Preparing the Environment
Make sure that you are `cd`'d into the project directory before running these commands.

First, clone TensorFlow's supplied models and support:
```sh
$ git clone https://github.com/tensorflow/models.git src/model/models
$ cd ../model/models/research
```

Next, generate the Python files from the `proto` files, copy them into the `research`
directory, and install them.
```sh
$ protoc object_detection/protos/*.proto --python_out=.
$ cp object_detection/packages/tf2/setup.py ./
$ python -m pip install .
```
After this, run the provided tests to ensure that the installation was successful:
```sh
$ python object_detection/builders/model_builder_tf2_test.py
$ cd ../../../  # Will place you back in src
```

### Assembling the Data & Preparing the Records
TensorFlow records can be prepared using the script found in `src/scripts/prepare_records.py`. Simply running this script will create the TFRecords:

```sh
$ cd scripts
$ python ./prepare_records.py
$ cd .. # Brings you back to src
```
This should output that two files were created: `test.record` and `train.record`

### Downloading the Base Model
Next, make the directory `model/content`:
```sh
$ mkdir model/content
$ cd model/content
```

Then, download `MobileNet` from the following url, uncompress it, and cleanup:
```sh
$ wget http://download.tensorflow.org/models/object_detection/classification/tf2/20200710/mobilenet_v2.tar.gz
$ tar -xvf mobilenet_v2.tar.gz
$ rm mobilenet_v2.tar.gz
```

Next, download the sample configuration:
```sh
$ wget wget https://raw.githubusercontent.com/tensorflow/models/master/research/object_detection/configs/tf2/ssd_mobilenet_v2_320x320_coco17_tpu-8.config
$ mv ssd_mobilenet_v2_320x320_coco17_tpu-8.config mobilenet_v2.config
```

### Configuring TensorFlow
To configure TensorFlow, make sure you are `cd`'d into the `src/model/content` directory and run the `configre_tensorflow.py` script:

```sh
$ python ../../scripts/configure_tensorflow.py
````

### Training the Model
Begin training by `cd`ing up one directory to `src/model` and running the following command:

```sh
$ python3 models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=content/mobilenet_v2.config \
    --model_dir="./training" \
    --alsologtostderr \
    --num_train_steps=50000 \
    --sample_1_of_n_eval_examples=1 \
    --num_eval_steps=1000
```
### Exporting the Model

### Testing the Model

## <span id="notebooks"></span> Option 2: Running the Provided Notebooks
The default notebook to use when building and configuring the model
is `src/notebooks/Training Model.ipynb`. This notebook can be used step by
step to prepare the environment, prepare the data, and train the model.

Start by launching the Jupyter notebook:
```sh
$ jupyter notebook
```
Then navigate to the `notebooks/Training Model.ipynb` file and run each
cell. You may need to adjust some of the commands that are operating-system
dependent. Alternatively, the guided command-line approach should
accommodate in a more portable manner.

## <span id="dir_structure"></span> Directory Structure
* `docs` - Documentation, project papers, etc.
* `src` - Source code, Python Nodebooks, libraries, etc

## <span id="branch_structure"></span> Branch Structure
* `main` - Production ready code, tested and tried.
* `test` - Code being tested and needs verified by the team.
* `dev` - In-development code, fine to merge into at any time.

When making changes, create a new branch and then merge it into dev.
This will help with concurrent edits and teamwork and prevent losing each others
works.

## <span id="authors"></span> Authors
* Walter Pach
* Vera Svensson

## <span id="links"></span> Links
* [Project Trello](https://trello.com/w/mlproject36)
* [Project Proposal - OverLeaf](https://www.overleaf.com/7497962469qwbbdxyxrmjg)
* [Project Proposal - PDF](docs/CSCE_585_Project_Report.pdf)
* [Single Page Proposal - PDF](docs/Single_Page_Proposal.pdf)
* [Project Pitch Presentation - PDF](docs/Project_Presentation.pdf)
* [Project Milestone 1 - PDF](docs/CSCE_585_Project_Milestone_1.pdf)
