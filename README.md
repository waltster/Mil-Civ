# MIl/CIV Visual ML System for Identifying and Minimizing Civilian Fatality in Urban War Zones
## Contents
* [Dependencies](#dependencies)
  * [Installing Key Dependencies](#key_dependencies)
  * [Installing Auxillary Dependencies](#aux_dependencies)
* [Training](#training)
* [Running](#running)
* [Directory Structure](#dir_structure)
* [Branch Structure](#branch_structure)
* [Authors](#authors)
* [Links](#links)

## <span id="dependencies"></span> Dependencies
See [DEPENDENCIES.md](./DEPENDENCIES.md) for documentation.

## <span id="training"></span> Training
See [TRAINING.md](./TRAINING.md) for documentation.

## <span id="running"></span> Running
To run the front-end of the model, run the following commands:

```sh
$ cd src/front-end
$ python server.py
```

Then visit [main.html](src/front-end/main.html) in your browser.

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
* [Project Report](./docs/CSCE_585_Final_Milestone.pdf)
