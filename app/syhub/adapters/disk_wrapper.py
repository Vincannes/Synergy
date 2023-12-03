#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import re
import glob
import math
import shutil
from datetime import datetime
from sys import platform as _platform


def get_platform():
    if _platform.count("win32"):
        return "win32"
    elif _platform.count("linux"):
        return "linux"
    elif _platform.count("darwin"):
        return "darwin"


def get_user(path):
    _user = "Unknown"
    if get_platform() == "win32":
        from win32 import win32security
        sd = win32security.GetFileSecurity(path, win32security.OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        _user, _, _ = win32security.LookupAccountSid(None, owner_sid)
    elif get_platform() == "linux":
        from pwd import getpwuid
        stat_p = os.stat(path)
        _user = getpwuid(stat_p.st_uid).pw_name
    return _user


class FormatSize(int):
    """ define a size class to allow custom formatting
        Implements a format specifier of S for the size class - which displays a human readable in b, kb, Mb etc
    """

    def __format__(self, fmt):
        if fmt == "" or fmt[-1] != "S":
            if fmt[-1].tolower() in ['b', 'c', 'd', 'o', 'x', 'n', 'e', 'f', 'g', '%']:
                # Numeric format.
                return int(self).__format__(fmt)
            else:
                return str(self).__format__(fmt)

        val, s = float(self), ["B ", "KB", "MB", "GB", "TB", "PB"]
        if val < 1:
            # Can't take log(0) in any base.
            i, v = 0, 0
        else:
            i = int(math.log(val, 1024)) + 1
            v = val / math.pow(1024, i)
            v, i = (v, i) if v > 0.5 else (v * 1024, i - 1)
        return ("{0:{1}f}" + s[i]).format(v, fmt[:-1])


class DiskWrapper(object):

    @staticmethod
    def file_infos(file_path):
        file_info = os.stat(file_path)
        file_owner = get_user(file_path)
        # file_owner = file_info.st_uid
        formatted_time = datetime.fromtimestamp(
            file_info.st_mtime
        ).strftime('%Y/%m/%d %H:%M')
        file_size = "{0:.1S}".format(
            FormatSize(os.path.getsize(file_path))
        )
        return file_owner, formatted_time, file_size

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
