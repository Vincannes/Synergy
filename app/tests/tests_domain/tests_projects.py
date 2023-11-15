import unittest

from app.syhub.core.projects import Projects
from app.syhub.core.exceptions import *
from app.tests.tests_domain.fake_objects import *


class TestProjects(unittest.TestCase):

    def setUp(self) -> None:
        _project = Projects
        _project.disk_wrapper = FakeDiskWrapper
        _project.path_wrapper = FakePaths
        pfs = os.path.join("path", "to", "projects")
        self.project = _project(pfs)

    def test_get_all_projects(self):
        expected = [
            "Project1",
            "Project2",
            "Project3",
        ]
        self.assertEqual(expected, self.project.get_projects())

    def test_RAISE_sequences_from_projects_NO_PROJECTS_SET(self):
        with self.assertRaises(NoProjectSetError):
            self.project.get_sequences()

    def test_RAISE_sequences_from_projects_NO_SEQUENCES_FOUND(self):
        self.project.set_project("Project_No_Sequence")
        with self.assertRaises(NoSequencesFoundError):
            self.project.get_sequences()

    def test_get_sequences_from_projects(self):
        expected = [
            "sequence1",
            "sequence2",
            "sequence3",
        ]
        self.project.set_project("Project1")
        self.assertEqual(expected, self.project.get_sequences())

    def test_get_shots(self):
        expected = [
            "shots_010",
            "shots_020",
            "shots_030",
            "shots_040",
        ]
        self.project.set_project("Project1")
        self.project.set_sequence("sequence1")
        self.assertEqual(expected, self.project.get_shots())

    def test_RAISE_shots_from_projects_NO_SHOTS_FOUND(self):
        self.project.set_project("Project1")
        self.project.set_sequence("sequence2")
        with self.assertRaises(NoShotsFoundError):
            self.project.get_shots()