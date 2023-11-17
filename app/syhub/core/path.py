#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os

from app.syhub.core import constants as cst
from app.syhub.core.logger import create_log
from app.syhub.adapters.tank_wrapper import TankWrapper


class Paths(object):
    tank_wrapper = TankWrapper
    TPL_NAME_SHOT = "shot_root"
    TPL_NAME_SEQUENCE = "sequence_root"

    def __init__(self, project_path):
        self._project_path = project_path
        self._tk = self.tank_wrapper(project_path)

        self._logger = create_log(__file__)

    def get_sequence_dir(self):
        template = self._tk.get_template(self.TPL_NAME_SEQUENCE)
        sequence = self._tk.build_path_from_template(
            template=template,
            fields={"Sequence": ""}
        )
        return os.path.dirname(sequence)

    def get_sequence_path(self, sequence):
        template = self._tk.get_template(self.TPL_NAME_SEQUENCE)
        return self._tk.build_path_from_template(
            template=template,
            fields={"Sequence": sequence}
        )

    def get_shot_path(self, sequence, shot):
        template = self._tk.get_template(self.TPL_NAME_SHOT)
        fields = {
            "Sequence": sequence,
            "Shot": shot,
        }
        return self._tk.build_path_from_template(template=template, fields=fields)

    def create_file_structure(self):
        pass


if __name__ == '__main__':
    from pprint import pprint
    path = Paths("D:\Desk\python\Projects\Project1")
    # print(path.get_sequence_dir())
    # print(path.get_sequence_path("sh"))
    # print(path.get_shot_path("sh", "sh010"))

    path.create_file_structure()