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
    def is_dir(path):
        if any([True for a in ["text.txt"] if a in path or os.path.basename(path).startswith(".")]):
            return False
        return True

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
        elif path == os.path.join("path", "to", "schema"):
            return ["project", ".project"]
        elif path == os.path.join("path", "to", "schema", "project"):
            return ["sequence", "_admin"]
        elif path == os.path.join("path", "to", "schema", "project", "_admin"):
            return ["nuke", "text.txt"]
        elif path == os.path.join("path", "to", "schema", "project", "sequence"):
            return ["sequence", ".sequence"]
        elif path == os.path.join("path", "to", "schema", "project", "sequence", "sequence"):
            return ["shot", ".shot"]
        elif path == os.path.join("path", "to", "schema", "project", "sequence", "sequence", "shot"):
            return ["task", ".task"]
        return values

    @staticmethod
    def walk(path):
        top, dirs, files = [], [], []

        path = path.replace("/", os.sep)
        if path == "path/to/schema".replace("/", os.sep):
            top = "path/to/schema".replace("/", os.sep)
            dirs = ["project"]
            files = [".project"]

        if path == "path/to/schema/project".replace("/", os.sep):
            top = "path/to/schema/project".replace("/", os.sep)
            dirs = ["_admin", "sequence"]
            files = []

        if path == "path/to/schema/project/_admin".replace("/", os.sep):
            top = "path/to/schema/project/_admin".replace("/", os.sep)
            dirs = ["nuke"]
            files = ["text.txt"]

        if path == "path/to/schema/project/_admin/nuke".replace("/", os.sep):
            top = "path/to/schema/project/_admin/nuke".replace("/", os.sep)
            dirs = []
            files = []

        if path == "path/to/schema/project/sequence".replace("/", os.sep):
            top = "path/to/schema/project/sequence".replace("/", os.sep)
            dirs = ["sequence"]
            files = [".sequence"]

        if path == "path/to/schema/project/sequence/sequence".replace("/", os.sep):
            top = "path/to/schema/project/sequence/sequence".replace("/", os.sep)
            dirs = ["shot"]
            files = [".shot"]

        if path == "path/to/schema/project/sequence/sequence/shot".replace("/", os.sep):
            top = "path/to/schema/project/sequence/sequence/shot".replace("/", os.sep)
            dirs = ["task"]
            files = [".task"]

        if path == "path/to/schema/project/sequence/sequence/.shot".replace("/", os.sep):
            top = "path/to/schema/project/sequence/sequence/.shot".replace("/", os.sep)
            dirs = []
            files = []

        if path == "path/to/schema/project/sequence/sequence/shot/task".replace("/", os.sep):
            top = "path/to/schema/project/sequence/sequence/shot/task".replace("/", os.sep)
            dirs = []
            files = []

        yield top, dirs, files

        for d in dirs:
            new_path = os.path.join(top, d)
            for result in FakeDiskWrapper.walk(new_path):
                yield result


class FakeTankWrapper(object):

    def __init__(self, project_path):
        self.project_path = project_path

    def get_template(self, name):
        return name

    def build_path_from_template(self, template, fields):
        path = ""
        if template == "sequence_root":
            path = os.path.join(self.project_path, "sequence", fields.get("Sequence"))
        elif template == "shot_root":
            path = os.path.join(self.project_path, "sequence", fields.get("Sequence"), fields.get("Shot"))
        return path


if __name__ == '__main__':
    for root, dirs, files in FakeDiskWrapper.walk("path/to/schema".replace("/", os.sep)):
        print(root, dirs, files)