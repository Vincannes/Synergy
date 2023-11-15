import os


class FakePaths(object):

    def __init__(self, project_path):
        self._project_path = project_path

    def get_sequence_dir(self):
        return self._project_path

    def get_sequence_path(self, sequence):
        return os.path.join(self._project_path, sequence)

    def get_shot_path(self, sequence, shot):
        return os.path.join(self._project_path, sequence, shot)


class FakeDiskWrapper(object):

    @staticmethod
    def list_dir(path):
        values = []
        if path == os.path.join("path", "to", "projects"):
            values = [
                "Project1",
                "Project2",
                "Project3",
            ]
        elif path == os.path.join("path", "to", "projects", "Project1"):
            values = [
                "sequence1",
                "sequence2",
                "sequence3",
            ]
        elif path == os.path.join("path", "to", "projects", "Project1", "sequence1"):
            values = [
                "shots_010",
                "shots_020",
                "shots_030",
                "shots_040",
            ]
        return values
