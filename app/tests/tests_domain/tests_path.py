#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
import os
import unittest
from pprint import pprint

from .fake_objects import FakeTankWrapper, FakeDiskWrapper
from app.syhub.core.path import Path


class TestPath(unittest.TestCase):

    def setUp(self):
        self.path_schema = "path/to/schema".replace("/", os.sep)
        self.path_project = "path/to/project".replace("/", os.sep)
        _path = Path
        _path.tank_wrapper = FakeTankWrapper
        _path.disk_wrapper = FakeDiskWrapper
        self.path = _path(self.path_project)
        self.path.schema_folder = self.path_schema

    def test_get_sequence_dir(self):
        expected = os.path.join(self.path_project, "sequence")
        self.assertEqual(expected, self.path.get_sequence_dir())

    def test_get_sequence_path(self):
        expected = os.path.join(self.path_project, "sequence", "seq")
        self.assertEqual(expected, self.path.get_sequence_path("seq"))

    def test_get_hot_path(self):
        expected = os.path.join(self.path_project, "sequence", "seq", "seq10")
        self.assertEqual(expected, self.path.get_shot_path("seq", "seq10"))

    def test_project_get_sub_dir_Project(self):
        entity = "Project"
        expected = [
            os.path.relpath(f"{self.path_schema}/project"),
            os.path.relpath(f"{self.path_schema}/project/sequence/"),
            os.path.relpath(f"{self.path_schema}/project/_admin/"),
            os.path.relpath(f"{self.path_schema}/project/_admin/nuke"),
            os.path.relpath(f"{self.path_schema}/project/_admin/text.txt"),
        ]
        self.assertEqual(
            sorted(expected),
            sorted(self.path.get_folders_for_entity(entity))
        )

    def test_project_get_sub_dir_Sequence(self):
        entity = "Sequence"
        expected = [
            os.path.relpath(f"{self.path_schema}/project/sequence/sequence"),
        ]
        self.assertEqual(
            sorted(expected),
            sorted(self.path.get_folders_for_entity(entity))
        )

    def test_project_get_sub_dir_Shot(self):
        entity = "Shot"
        expected = [
            os.path.relpath(f"{self.path_schema}/project/sequence/sequence/shot"),
        ]
        self.assertEqual(
            sorted(expected),
            sorted(self.path.get_folders_for_entity(entity))
        )

    def test_project_get_sub_dir_Task(self):
        entity = "Task"
        expected = [
            os.path.relpath(f"{self.path_schema}/project/sequence/sequence/shot/task"),
        ]
        self.assertEqual(
            sorted(expected),
            sorted(self.path.get_folders_for_entity(entity))
        )

    def test_generate_path_Project(self):
        paths = [
            os.path.relpath(f"{self.path_schema}/project"),
            os.path.relpath(f"{self.path_schema}/project/sequence/"),
            os.path.relpath(f"{self.path_schema}/project/_admin/"),
            os.path.relpath(f"{self.path_schema}/project/_admin/nuke"),
            os.path.relpath(f"{self.path_schema}/project/_admin/text.txt"),
        ]
        expected = [
            os.path.relpath(f"{self.path_project}/Project1"),
            os.path.relpath(f"{self.path_project}/Project1/sequence/"),
            os.path.relpath(f"{self.path_project}/Project1/_admin/"),
            os.path.relpath(f"{self.path_project}/Project1/_admin/nuke"),
            os.path.relpath(f"{self.path_project}/Project1/_admin/text.txt"),
        ]
        self.assertEqual(
            expected,
            self.path.generate_path_for_filestructure(
                paths,
                multi_entity={"project": "Project1"},
                project_path=self.path_project
            )
        )
