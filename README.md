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
* `protobuf`
* `wget`

On macOS, these can be automatically installed using the `mac_helper.sh` script. Try running `bash mac_helper.sh install` to install them.

### <span id="aux_dependencies"></span> Installing Auxillary Dependencies
```shell
$ python -m ensurepip --upgrade # Install pip if it was not installed automatically
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install tensorflow-object-detection-api
$ pip install notebook
$ pip install opencv-python==4.6.0.66
$ pip install opencv-python-headless==4.6.0.66
```

If you encounter an error with the `python` or `pip` command not found, try running the below, and alias the reverse if you have the opposite problem.
```shell
$ alias python=python3
$ alias pip=pip3
```

## <span id="guided_cmd"></span> Option 1: Guided Command-Line
### Preparing the Environment
Make sure that you are `cd`'d into the project directory before running these commands.

First, clone TensorFlow's supplied models and support:
```shell
$ git clone https://github.com/tensorflow/models.git src/model/models
```

## <span id="notebooks"></span> Option 2: Running the Provided Notebooks
The default notebook to use when building and configuring the model
is `src/notebooks/Training Model.ipynb`. This notebook can be used step by
step to prepare the environment, prepare the data, and train the model.

Start by launching the Jupyter notebook:
```shell
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
* Logan Nall

## <span id="links"></span> Links
* [Project Trello](https://trello.com/w/mlproject36)
* [Project Proposal - OverLeaf](https://www.overleaf.com/7497962469qwbbdxyxrmjg)
* [Project Proposal - PDF](docs/CSCE_585_Project_Report.pdf)
* [Single Page Proposal - PDF](docs/Single_Page_Proposal.pdf)
* [Project Pitch Presentation - PDF](docs/Project_Presentation.pdf)
* [Project Milestone 1 - PDF](docs/CSCE_585_Project_Milestone_1.pdf)
