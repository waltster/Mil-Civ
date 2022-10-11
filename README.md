# CSCE-585 Project
## Dependencies
* `wget`
* `python3`, `pip3`

## Usage
### 1. Install Dependencies
[Install Python](https://www.python.org/) from this link.

```shell
$ python -m ensurepip --upgrade # Install pip if it was not installed automatically
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install tensorflow-object-detection-api
$ pip install notebook
```

### 2. Run the Provided Notebooks
The default notebook to use when building and configuring the model
is
## Authors
* Logan Nall
* Walter Pach
* Vera Svensson

## Links
* [Project Trello](https://trello.com/w/mlproject36)
* [Project Proposal - OverLeaf](https://www.overleaf.com/7497962469qwbbdxyxrmjg)
* [Project Proposal - PDF](docs/CSCE_585_Project_Report.pdf)
* [Single Page Proposal - PDF](docs/Single_Page_Proposal.pdf)
* [Project Pitch Presentation - PDF](docs/Project_Presentation.pdf)
* [Project Milestone 1 - PDF](docs/CSCE_585_Project_Milestone_1.pdf)

## Directory Structure
* `docs` - Documentation, project papers, etc.
* `src` - Source code, Python Nodebooks, libraries, etc

## Branch Structure
* `main` - Production ready code, tested and tried.
* `test` - Code being tested and needs verified by the team.
* `dev` - In-development code, fine to merge into at any time.

When making changes, create a new branch and then merge it into dev. This will help with concurrent edits and teamwork and prevent losing each others works.
