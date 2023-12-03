#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import sys
from configparser import ConfigParser
from app.syhub.adapters import disk_wrapper
from app.syhub.core import constants as cst


class ConfigFiles(object):

    def __init__(self, ini_file):
        self.parser = ConfigParser()
        self.ini_file = ini_file
        self.parser.read(self.ini_file)

    def get_dcc_path(self, engine):
        dcc_paths = {}
        if disk_wrapper.get_platform() == "win32":
            engines = self.parser["win32"]
            for version in engines:
                if engine not in version:
                    continue
                dcc_paths[version] = engines[version]
            return dcc_paths

        elif disk_wrapper.get_platform() == "linux":
            engines = self.parser["linux"]
            for version in engines:
                if engine not in version:
                    continue
                dcc_paths[version] = engines[version]
            return dcc_paths

        elif disk_wrapper.get_platform() == "darwin":
            engines = self.parser["darwin"]
            for version in engines:
                if engine not in version:
                    continue
                dcc_paths[version] = engines[version]
            return dcc_paths


if __name__ == '__main__':
    from pprint import pprint
    path = "D:\\Desk\\python\\Synergy\\app\\configs\\app_paths.ini"
    config = ConfigFiles(path)
    pprint(config.get_dcc_path("nuke"))

