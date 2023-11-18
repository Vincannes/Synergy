#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import unittest

from .fake_objects import FakeTankWrapper, FakeDiskWrapper
from app.syhub.core.path import Path


class TestPath(unittest.TestCase):

    def setUp(self):
        self.path_project = "path/tp/project"
        _path = Path
        _path.tank_wrapper = FakeTankWrapper
        _path.disk_wrapper = FakeDiskWrapper
        self.path = _path(self.path_project)
        self.path.schema_folder = "path/to/schema"

    def test_project_get_sub_dir(self):
        entity = "Project"
        entity_value = "Project1"
        expected = [
            f"{self.path_project}/Project1",
            f"{self.path_project}/Project1/sequence/",
            f"{self.path_project}/Project1/_admin/",
            f"{self.path_project}/Project1/_admin/nuke",
        ]
        self.assertEqual(
            expected,
            self.path.get_folders_for_entity(entity, entity_value)
        )

