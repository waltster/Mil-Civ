# CSCE-585 Project
## Dependencies
* `wget`
* `python3`, `pip3`

## Usage
### 1. Data Preparation
* The data set used to train the model can be found in `src/data`, which includes both `test_labels.csv`, `train_labels.csv`, and `images`.
* A notebook for a demo-data gatherer has been created. To see how information about the images is collected and parsed, run this as a Jupyter notebook.

To prepare the data set for training, first run the following command. This will generate a single file, `train.record` that will contain all of the
information necessary to begin training a model.
```sh
$ cd src/model
$ python3 ./generate_tfrecord.py --csv_input=../data/train_labels.csv --image_dir=../data/images --output_path=train.record
```

## Authors
* Logan Nall
* Walter Pach
* Vera Svensson

## Links
* [Project Trello](https://trello.com/w/mlproject36)
* [Project Proposal - OverLeaf](https://www.overleaf.com/7497962469qwbbdxyxrmjg)
* [Project Proposal - PDF](docs/proposal/CSCE_585_Project_Report.pdf)
* [Single Page Proposal - PDF](docs/proposal/Single_Page_Proposal.pdf)
* [Project Pitch Presentation - PDF](docs/Project_Presentation.pdf)

## Directory Structure
* `docs` - Documentation, project papers, etc.
* `src` - Source code, Python Nodebooks, libraries, etc

## Branch Structure
* `main` - Production ready code, tested and tried.
* `test` - Code being tested and needs verified by the team.
* `dev` - In-development code, fine to merge into at any time.

When making changes, create a new branch and then merge it into dev. This will help with concurrent edits and teamwork and prevent losing each others works.
