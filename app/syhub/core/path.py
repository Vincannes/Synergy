#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import re

from app.syhub.core import constants as cst
from app.syhub.core.logger import create_log
from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.adapters.tank_wrapper import TankWrapper


class Path(object):
    tank_wrapper = TankWrapper
    disk_wrapper = DiskWrapper
    TPL_NAME_SHOT = "shot_root"
    TPL_NAME_SEQUENCE = "sequence_root"

    def __init__(self, project_path):
        self._project_path = project_path
        self._tk = self.tank_wrapper(project_path)

        self._logger = create_log(__file__)

        self.schema_folder = os.path.join(
            os.environ.get(cst.Variables.SYN_ROOT_CONFIG_PATH),
            "schema"
        )

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

    def create_file_structure(self, entity_type, entity_value, multi_entity=None):

        _multi_entity = {
            entity_type.lower(): entity_value
        }
        if multi_entity is not None:
            for key, val in multi_entity.items():
                _multi_entity[key.lower()] = val

        if entity_type == cst.Entities.PROJECT:
            project_path = os.environ.get(cst.Variables.SYN_PROJECT_FILE_STRUCTURE)
        else:
            project_path = self._project_path

        items_to_create = self.get_folders_for_entity(entity_type)
        converted_path = self._convert_to(paths=items_to_create, multi_entity=_multi_entity, project_path=project_path)
        pprint(items_to_create)
        pprint(converted_path)

    def get_folders_for_entity(self, entity_type):
        _items = []

        for root, dirs, files in self.disk_wrapper.walk(self.schema_folder):
            for dir in dirs:
                sub_dir_path_schema = os.path.join(root, dir)
                has_grp = any(
                    [True for i in os.listdir(os.path.dirname(sub_dir_path_schema)) if f".{entity_type.lower()}" == i]
                )
                if has_grp:
                    _items.append(sub_dir_path_schema)
                    _items.extend(self._get_sub_dirs(sub_dir_path_schema))
                    break

        return _items

    def _get_sub_dirs(self, entity_path):
        _all_dirs = []

        if not os.listdir(entity_path):
            return [entity_path]

        for i in os.listdir(entity_path):
            _this_sub_dir = os.path.join(entity_path, i)

            if not os.path.isdir(_this_sub_dir) and not i.startswith("."):
                _all_dirs.append(_this_sub_dir)
                continue

            if i.startswith(".") or any(
                    [True for a in os.listdir(os.path.dirname(_this_sub_dir)) if a.startswith(".")]
            ):
                continue

            _all_dirs.append(_this_sub_dir)
            _all_dirs.extend(self._get_sub_dirs(_this_sub_dir))

        return _all_dirs

    def _convert_to(self, paths, multi_entity=None, project_path=""):
        if multi_entity is None:
            multi_entity = {}

        _converted_path = []
        schema_folder_ref = self.schema_folder.split(os.path.sep)

        for path in paths:
            folders = path.split(os.path.sep)
            final_path_list = []
            for i in range(len(folders), 0, -1):
                a = folders[0] + os.sep + folders[1]
                current_path = os.path.join(a, *folders[2:i])
                current_path = os.path.normpath(current_path)

                if folders[:i] == schema_folder_ref:
                    break
                if not os.path.isdir(current_path):
                    continue

                has_grp = any(
                    [True for i in os.listdir(os.path.dirname(current_path)) if i.startswith(".")]
                )

                i = i-1 if i != len(folders) else -1
                element = folders[i]
                if has_grp:
                    key = folders[i]
                    element = multi_entity.get(key.lower(), 'Invalid')
                final_path_list.append(element)

            final_curr_path = os.path.join(project_path, *reversed(final_path_list))
            final_curr_path = os.path.normpath(final_curr_path)
            _converted_path.append(final_curr_path)

        return _converted_path

if __name__ == '__main__':
    from pprint import pprint
    path = Path("D:\\Desk\\python\\Projects\\Project1")
    # print(path.get_sequence_dir())
    # print(path.get_sequence_path("sh"))
    # print(path.get_shot_path("sh", "sh010"))

    path.create_file_structure("Project", "Project1")
    print("")
    path.create_file_structure("Sequence", "sh", {"Project": "Project1"})
    print("")
    path.create_file_structure("Shot", "sh10", {"Project": "Project1", "Sequence": "sh"})
    print("")
    path.create_file_structure("Task", "cmp", {"Project": "Project1", "Sequence": "sh", "Shot": "sh10"})
