#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import re
import glob
import shutil


class DiskWrapper(object):

    @staticmethod
    def copy_file(src, dest):
        shutil.copy(src, dest)

    @staticmethod
    def is_path_exist(path):
        return os.path.exists(path)

    @staticmethod
    def is_dir(path):
        return os.path.isdir(path)

    @staticmethod
    def is_file(path=""):
        regex_pattern = r'\.[^\W_]+$'
        if os.path.exists(path):
            return os.path.isfile(path)
        else:
            return bool(re.search(regex_pattern, path))

    @staticmethod
    def list_dir(path):
        if not os.path.isdir(path):
            raise ValueError(f"Path has to be a directory {path}")
        return os.listdir(path)

    @staticmethod
    def symlink(src, dst):
        return os.symlink(src, dst)

    @staticmethod
    def make_dir(path, mode=0o775, recursive=False):
        if recursive:
            os.makedirs(path, mode)
        else:
            os.mkdir(path, mode)

    @staticmethod
    def walk(path):
        return os.walk(path)
