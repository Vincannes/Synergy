#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os

from app.syhub.core import constants as cst
from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.core.path import Path
from app.syhub.core.exceptions import *


class Projects(object):
    path_wrapper = Path
    disk_wrapper = DiskWrapper

    def __init__(self, pfs=None):
        if pfs is None:
            pfs = os.environ.get(cst.Variables.SYN_PROJECT_FILE_STRUCTURE)
        self._pfs_path = pfs

        self._pw = None
        self._project = None
        self._project_path = None

    @property
    def project(self):
        return self._project

    @property
    def project_path(self):
        return self._project_path

    def get_projects(self):
        return self.disk_wrapper.list_dir(self._pfs_path)

    def get_sequences(self):
        if not self._project:
            raise NoProjectSetError()

        _sequences_path = self._pw.get_sequence_dir()
        sequences = self.disk_wrapper.list_dir(_sequences_path)

        if not sequences:
            raise NoSequencesFoundError(self._project)

        return sequences

    def get_shots(self, sequence):
        if not self._project:
            raise NoProjectSetError()

        if not sequence:
            raise NoSequenceSetError()

        _sequences_dir = self._pw.get_sequence_path(sequence)
        shots = self.disk_wrapper.list_dir(_sequences_dir)
        if not shots:
            raise NoShotsFoundError(sequence)
        return shots

    def get_tasks(self, sequence, shot):
        if not self._project:
            raise NoProjectSetError()

        if not sequence:
            raise NoSequenceSetError()

        _shot_dir = self._pw.get_shot_path(
            sequence,
            shot
        )
        tasks = self.disk_wrapper.list_dir(_shot_dir)
        if not tasks:
            raise NoTasksFoundError(_shot_dir)
        return tasks

    def get_variants(self, sequence, shot, task):
        """ TODO
        """
        if not self._project:
            raise NoProjectSetError()

        if not sequence:
            raise NoSequenceSetError()

        _task_dir = self._pw.get_task_path(
            sequence,
            shot,
            task
        )

        fields = {
            "Sequence": sequence,
            "Shot": shot,
            "Task": task,
            "name": shot,
        }
        _variants = []
        for _path in self._pw.get_engine_scenes("nuke", fields):
            _fields = self._pw.get_fields_from_path(_path)
            _variants.append(_fields.get("variant"))
        return list(set(_variants))

    def get_versions(self, sequence, shot, task, variant):
        """ TODO
        """
        if not self._project:
            raise NoProjectSetError()

        if not sequence:
            raise NoSequenceSetError()

        _task_dir = self._pw.get_task_path(
            sequence,
            shot,
            task
        )
        fields = {
            "Sequence": sequence,
            "Shot": shot,
            "Task": task,
            "name": shot,
            "variant": variant,
        }
        _versions = []
        for _path in self._pw.get_engine_scenes("nuke", fields):
            _fields = self._pw.get_fields_from_path(_path)
            _versions.append(_fields.get("version"))
        return list(set(_versions))

    def get_nuke_scenes(self, sequence, shot, task, variant):
        return self._pw.get_nuke_scenes(
            sequence=sequence,
            shot=shot,
            task=task,
            variant=variant
        )

    def set_project(self, project):
        self._project = project
        self._project_path = os.path.join(self._pfs_path, project)
        self._pw = self.path_wrapper(self._project_path)


if __name__ == '__main__':
    from pprint import pprint

    path = Projects("D:\Desk\python\Projects")
    path.set_project("autre_name")
    pprint(path.get_variants("seq_010", "cmp"))
    pprint(path.get_versions("seq_010", "cmp", "test"))

    # print(path._tk.get_fields_from_path("D:\\Desk\\python\\Projects\\autre_name\\sequence\\seq\\seq_010\\cmp\\nuke\\wip\\seq_010-cmp-base-v001.nk"))