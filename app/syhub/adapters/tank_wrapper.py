#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import re

from app.libs.Tank.python import sgtk

REGEX_FRAME = r"\.(\d+)\."

if not os.environ.get("SYN_ROOT_PATH"):
    os.environ["SYN_ROOT_PATH"] = os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        )
    )

os.environ["CONFIG_PATH"] = os.path.join(
    os.environ.get("SYN_ROOT_PATH"),
    "configs",
    "templates.yml"
)


class TankWrapper(object):

    def __init__(self, project_path="D:/Desk/python/Projects"):
        self._tk = sgtk.Tank(project_path)
        self.templates = self._tk.templates()

    def get_template(self, name):
        return self.templates[name]

    def get_template_from_path(self, path):
        try:
            path = re.sub(REGEX_FRAME, '.%04d.', path)
        except Exception as e:
            print(e)
            pass
        path = path.replace("%04d", "####")
        path = path.replace("\\", "/")  # thank you Windobe
        return self._tk.template_from_path(path)

    def get_template_keys(self, template):
        if isinstance(template, str):
            template = self.get_template(template)
        return set(template.ordered_keys())

    def get_fields_from_path(self, path, template=None):
        if not template:
            template = self.get_template_from_path(path)
        if isinstance(template, str):
            template = self.get_template(template)
        result_string = path.replace("\\", "/")  # thank you Windobe
        try:
            result_string = re.sub(REGEX_FRAME, '.%04d.', result_string)
        except:
            pass
        result_string = result_string.replace("%04d", "####")
        return template.get_fields(result_string)

    def get_abstract_path(self, template, fields):
        if isinstance(template, str):
            template = self.get_template(template)
        return self._tk.abstract_paths_from_template(template, fields)

    def build_path_from_template(self, template, fields):
        if isinstance(template, str):
            template = self.get_template(template)
        return template.apply_fields(fields)


if __name__ == '__main__':
    tk = TankWrapper()
    template_name = "Shot_NukeRender_Work_Sequence"
    fields = {
        "Sequence": "sh",
        "Shot": "sh_010",
        "version": "1",
        "Task": "cmp",
        "name": "sh_010",
        "write_node": "out",
        "colorspace": "linear",
        "variant": "test",
        "render_source": "nk",
        "ext_render_nuke": "exr"
    }
