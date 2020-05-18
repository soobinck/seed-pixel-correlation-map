from importlib.machinery import SourceFileLoader
import os
from importlib import import_module
import sys


def get_seeds(path):
    Path = os.path.normpath(path)
    folders = Path.split('/')  # create list of each folder component of the path
    folder_path = '/'.join(
        folders[:-1])  # remove the file from the path to specify path to the folder containing script
    sys.path.insert(1, folder_path)  # add folder path to sys path so python can find module

    mod = import_module(
        folders[-1][:-3])  # get rid of .py extension and use only name of the script rather than entire path
    return mod.seeds
