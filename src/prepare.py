# Script for preparing environment for training the model.
# Aimed to be portable and support many environments. This is an attempt
# to have portable code.
# @author Walter Pach
# @version 0.1
import os
import shutil
import glob

# This class preserves the state of the working directory but allows for
# changing directories.
# Credit to https://stackoverflow.com/questions/431684/equivalent-of-shell-cd-
# command-to-change-the-working-directory.
class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)

def main():
    with cd("./src/model/models/research"):
        os.system("protoc object_detection/protos/*.proto --python_out=.")

        shutil.copyfile("object_detection/packages/tf2/setup.py", "./setup.py")
        os.system("python3 -m pip install .")
        os.system("python3 object_detection/builders/model_builder_tf2_test.py")

if __name__ == "__main__":
    main()
