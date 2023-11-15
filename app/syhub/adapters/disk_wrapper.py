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
