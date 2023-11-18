#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import glob


class DiskWrapper(object):

    @staticmethod
    def list_dir(path):
        if not os.path.isdir(path):
            raise ValueError(f"Path has to be a directory {path}")
        return os.listdir(path)

    @staticmethod
    def symlink(src, dst):
        return os.symlink(src, dst)

    @staticmethod
    def mk_dir(path, mode=0o775, recursive=True):
        if not os.path.isdir(path):
            if recursive:
                os.makedirs(path, mode)
            else:
                os.mkdir(path, mode)

    @staticmethod
    def walk(path):
        return os.walk(path)
