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

    def create_file_structure(self, entity_type, entity_value, multi_entity=None, engine=None):

        if multi_entity is None:
            multi_entity = {}

        if entity_type == cst.Entities.PROJECT:
            project_path = os.environ.get(cst.Variables.SYN_PROJECT_FILE_STRUCTURE)
        else:
            project_path = self._project_path

        items_to_create = self._get_folders_for_entity(entity_type, entity_value, project_path, multi_entity)
        pprint(items_to_create)

    def _get_folders_for_entity(self, entity_type, entity_value, project_path, multi_entity=None):
        """ TO REFACTO A LOTTTT
        """
        _items = []
        if multi_entity is None:
            multi_entity = {}

        schema_folder = os.path.join(
            os.environ.get(cst.Variables.SYN_ROOT_CONFIG_PATH),
            "schema"
        )

        main_folder = ""
        new_dir_path = []
        for root, dirs, files in os.walk(schema_folder):
            for dir in dirs:

                sub_dir_path_schema = os.path.join(root, dir)
                has_grp = any(
                    [True for i in os.listdir(os.path.dirname(sub_dir_path_schema)) if f".{entity_type.lower()}" == i]
                )

                if has_grp:
                    new_dir_path = [os.path.join(
                        root.replace(schema_folder, project_path),
                        entity_value
                    )]
                    main_folder = sub_dir_path_schema

                elif main_folder:
                    for item in self._get_sub_dirs(main_folder, multi_entity):
                        new_item = item.replace(
                            schema_folder,
                            project_path,
                        )
                        new_item = new_item.replace(entity_type.lower(), entity_value)
                        if new_item in _items:
                            continue
                        _items.append(new_item)
                    continue

                if new_dir_path:
                    _items.extend(new_dir_path)

        return _items

    def _get_sub_dirs(self, entity_path, multi_entity=None):
        _all_dirs = []

        if multi_entity is None:
            multi_entity = {}

        if not os.listdir(entity_path):
            return [entity_path]

        for i in os.listdir(entity_path):
            _this_sub_dir = os.path.join(entity_path, i)

            if not os.path.isdir(_this_sub_dir) and not i.startswith("."):
                _all_dirs.extend([_this_sub_dir])
                continue

            if i.startswith(".") or any(
                    [True for a in os.listdir(os.path.dirname(_this_sub_dir)) if a.startswith(".")]
            ):
                continue

            # # check if part of multi entity
            # _get = [a for a in os.listdir(_this_sub_dir) if a.startswith(".")]
            # if _get:
            #     print(i, _get, _this_sub_dir)

            _all_dirs.append(_this_sub_dir)
            _all_dirs.extend(self._get_sub_dirs(_this_sub_dir, multi_entity))

        return _all_dirs


if __name__ == '__main__':
    from pprint import pprint
    path = Paths("D:\Desk\python\Projects\Project1")
    # print(path.get_sequence_dir())
    # print(path.get_sequence_path("sh"))
    # print(path.get_shot_path("sh", "sh010"))
    # path.create_file_structure("Project", "Project1")
    path.create_file_structure("Sequence", "sh", {"Project": "Project1"})
    # path.create_file_structure("Shot", "sh10", {"Project": "Project1", "Sequence": "sh"})
    # path.create_file_structure("Task", "cmp", {"Project": "Project1", "Sequence": "sh", "Shot": "sh10"})
