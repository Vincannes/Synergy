#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
from pprint import pprint

from app.syhub.core import constants as cst
from app.syhub.core.logger import create_log
from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.adapters.tank_wrapper import TankWrapper


class Path(object):
    tank_wrapper = TankWrapper
    disk_wrapper = DiskWrapper
    TPL_NAME_SHOT = "shot_root"
    TPL_NAME_TASK = "shot_task_root"
    TPL_NAME_SEQUENCE = "sequence_root"
    TPL_NUKE_SCENE = "Shot_NukeScene_Work"
    TPL_MAYA_SCENE = "Shot_MayaScene_Work"
    TPL_HOUDINI_SCENE = "Shot_HoudiniScene_Work"

    def __init__(self, project_path):
        self._project_path = project_path
        self._tk = self.tank_wrapper(project_path)

        self._logger = create_log(__file__)

        self.schema_folder = os.path.join(
            os.environ.get(cst.Variables.SYN_ROOT_CONFIG_PATH),
            "schema"
        )

    def get_fields_from_path(self, path):
        return self._tk.get_fields_from_path(path)

    def get_abstract_path(self, template_name, fields):
        template = self._tk.get_template(template_name)
        return self._tk.get_abstract_path(template, fields)

    def get_engine_scenes(self, engine="nuke", fields=None):
        if fields is None:
            fields = {}
        template_name = ""
        if engine == cst.Engine.NUKE:
            template_name = self.TPL_NUKE_SCENE
        elif engine == cst.Engine.MAYA:
            template_name = self.TPL_MAYA_SCENE
        elif engine == cst.Engine.HOUDINI:
            template_name = self.TPL_HOUDINI_SCENE

        if not template_name:
            raise ValueError(f"No engine found: {[cst.Engine.NUKE, cst.Engine.MAYA, cst.Engine.HOUDINI]}")

        return self.get_abstract_path(template_name, fields)

    def get_nuke_scene(self, sequence, shot, task, variant, version):
        template = self._tk.get_template(self.TPL_NUKE_SCENE)
        fields = {
            "Sequence": sequence,
            "Shot": shot,
            "name": shot,
            "Task": task,
            "variant": variant,
            "version": version
        }
        return self._tk.build_path_from_template(template, fields)

    def get_nuke_scenes(self, sequence, shot, task, variant):
        template = self._tk.get_template(self.TPL_NUKE_SCENE)
        fields = {
            "Sequence": sequence,
            "Shot": shot,
            "name": shot,
            "Task": task,
            "variant": variant,
        }
        return self._tk.get_abstract_path(template, fields)

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

    def get_task_path(self, sequence, shot, task):
        template = self._tk.get_template(self.TPL_NAME_TASK)
        fields = {
            "Sequence": sequence,
            "Shot": shot,
            "Task": task
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
        converted_path = self.generate_path_for_filestructure(
            paths=items_to_create,
            entity_type=entity_type,
            multi_entity=_multi_entity,
            project_path=project_path
        )

        if entity_type == cst.Entities.PROJECT:
            self._project_path = sorted(converted_path)[0]

        pprint(converted_path)

        # copy dirs
        # for file in sorted(converted_path):
        #     if not self.disk_wrapper.is_path_exist(file):
        #         if self.disk_wrapper.is_file(file):
        #             continue
        #         self.disk_wrapper.make_dir(file)
        #
        # # copy files
        # for src, dst in zip(items_to_create, converted_path):
        #     if self.disk_wrapper.is_file(src) and self.disk_wrapper.is_file(dst):
        #         self.disk_wrapper.copy_file(src, dst)

    def get_folders_for_entity(self, entity_type):
        _items = []
        for root, dirs, files in self.disk_wrapper.walk(self.schema_folder):
            for dir in dirs:
                sub_dir_path_schema = os.path.join(root, dir)
                has_grp = any(
                    [True for i in self.disk_wrapper.list_dir(
                        os.path.dirname(sub_dir_path_schema)
                    ) if f".{entity_type.lower()}" == i]
                )
                if has_grp:
                    _items.append(sub_dir_path_schema)
                    _items.extend(self._get_sub_dirs(sub_dir_path_schema))
                    break
        return list(set(_items))

    def generate_path_for_filestructure(self, paths, entity_type=None, multi_entity=None, project_path=""):
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

                if not self.disk_wrapper.is_dir(current_path):
                    final_path_list.append(folders[-1])
                    continue

                has_grp = any(
                    [True for i in self.disk_wrapper.list_dir(
                        os.path.dirname(current_path)
                    ) if i.startswith(".")]
                )

                i = i-1 if i != len(folders) else -1
                element = folders[i]

                # Skip 'project' key to avoid double 'project' if entity =/= Project
                if entity_type and entity_type != cst.Entities.PROJECT and element == cst.Entities.PROJECT.lower():
                    continue

                if has_grp:
                    key = folders[i]
                    element = multi_entity.get(key.lower(), 'Invalid')
                final_path_list.append(element)

            final_curr_path = os.path.join(project_path, *reversed(final_path_list))
            final_curr_path = os.path.normpath(final_curr_path)
            _converted_path.append(final_curr_path)

        return _converted_path

    # PRIVATES

    def _get_sub_dirs(self, entity_path):
        _all_dirs = []

        if not self.disk_wrapper.list_dir(entity_path):
            return [entity_path]

        for i in self.disk_wrapper.list_dir(entity_path):
            _this_sub_dir = os.path.join(entity_path, i)

            if not self.disk_wrapper.is_dir(_this_sub_dir) and \
                    not i.startswith("."):
                _all_dirs.append(_this_sub_dir)
                continue

            if i.startswith(".") or any(
                    [True for a in self.disk_wrapper.list_dir(
                        os.path.dirname(_this_sub_dir)
                    ) if a.startswith(".")]
            ):
                continue

            _all_dirs.append(_this_sub_dir)
            _all_dirs.extend(self._get_sub_dirs(_this_sub_dir))

        return _all_dirs


if __name__ == '__main__':
    from pprint import pprint
    path = Path("D:\\Desk\\python\\Projects\\Project1")
    # print(path.get_sequence_dir())
    # print(path.get_sequence_path("sh"))
    # print(path.get_shot_path("sh", "sh010"))

    path.create_file_structure("Project", "Project3")
    print("")
    path.create_file_structure("Sequence", "sh")
    # print("")
    # path.create_file_structure("Shot", "sh10", {"Sequence": "sh"})
    # print("")
    # path.create_file_structure("Task", "cmp", {"Sequence": "sh", "Shot": "sh10"})
    print("")
    print(path.get_engine_scenes("dddd"))
    # print(path.get_nuke_scene("sh", "sh010", "cmp", "base"))