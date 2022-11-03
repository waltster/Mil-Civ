# <span id="key_dependencies"></span> Installing Key Dependencies

* `git`
* `grpc`
* `python` v3 - [Install Python](https://www.python.org/) from this link.
* `wget`

On macOS, these can be automatically installed using the `mac_helper.sh` script. Try running `bash mac_helper.sh install` to install them.

# <span id="aux_dependencies"></span> Installing Auxillary Dependencies
```sh
$ python -m ensurepip --upgrade # Install pip if it was not installed automatically
$ pip install --upgrade pip
$ pip install tensorflow
$ pip install tensorflow-object-detection-api
$ pip install notebook
$ pip install opencv-python==4.6.0.66
$ pip install opencv-python-headless==4.6.0.66
$ pip install protobuf==3.19
$ pip install flask
```

If you encounter an error with the `python` or `pip` command not found, try running the below, and alias the reverse if you have the opposite problem.
```sh
$ alias python=python3
$ alias pip=pip3
```
