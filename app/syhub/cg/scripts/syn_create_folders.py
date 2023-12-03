#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os


def syn_create_folders(path=None):
    osdir = os.path.dirname(path)
    if not os.path.isdir(osdir):
        try:
            os.makedirs(osdir)
        except OSError:
            print("OSError: makedirs %s" % osdir)
            pass
