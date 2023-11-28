#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os
import re

from app.libs.Tank.python import sgtk
from app.syhub.core import constants as cst

REGEX_FRAME = r"\.(\d+)\."

if not os.environ.get(cst.Variables.SYN_ROOT_PATH):
    from app.syhub.core.vars import set_vars
    set_vars()

os.environ[cst.Variables.CONFIG_PATH] = os.path.join(
    os.environ.get(cst.Variables.SYN_ROOT_CONFIG_PATH),
    "templates.yml"
)


class TankWrapper(object):

    def __init__(self, project_path="D:/Desk/python/Projects"):
        self.project_path = project_path
        self._tk = sgtk.Tank(self.project_path)
        self.templates = self._tk.templates()

    def get_template(self, name):
        return self.templates[name]

    def get_template_from_path(self, path):
        try:
            path = re.sub(REGEX_FRAME, '.%04d.', path)
            path = path.replace("%04d", "####")
        except Exception as e:
            print(e)
            pass
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
        try:
            path = re.sub(REGEX_FRAME, '.%04d.', path)
            path = path.replace("%04d", "####")
        except:
            pass
        return template.get_fields(path)

    def get_abstract_path(self, template, fields):
        if isinstance(template, str):
            template = self.get_template(template)
        return self._tk.abstract_paths_from_template(template, fields)

    def build_path_from_template(self, template, fields):
        if isinstance(template, str):
            template = self.get_template(template)
        return template.apply_fields(fields)


if __name__ == '__main__':
    tk = TankWrapper("D:/Desk/python/Projects/autre_name")
    template_name = "Shot_NukeRender_Work_Sequence"
    fields = {
        "Sequence": "seq",
        "Shot": "seq_010",
        # "version": "1",
        "Task": "cmp",
        "name": "seq_010",
        # "write_node": "out",
        # "colorspace": "linear",
        "variant": "base",
        # "render_source": "nk",
        # "ext_render_nuke": "exr"
    }
    from pprint import pprint
    pprint(tk.get_abstract_path("Shot_NukeScene_Work", fields))