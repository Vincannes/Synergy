#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os

from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.core.path import Path
from app.syhub.core.exceptions import *


class Projects(object):
    path_wrapper = Path
    disk_wrapper = DiskWrapper

    def __init__(self, pfs):
        self._pfs_path = pfs

        self._pw = None
        self._task = None
        self._shot = None
        self._project = None
        self._sequence = None
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

    def get_shots(self):
        if not self._project:
            raise NoProjectSetError()

        if not self._sequence:
            raise NoSequenceSetError()

        _sequences_dir = self._pw.get_sequence_path(
            self._sequence
        )
        shots = self.disk_wrapper.list_dir(_sequences_dir)
        if not shots:
            raise NoShotsFoundError(self._sequence)
        return shots

    def get_tasks(self):
        if not self._project:
            raise NoProjectSetError()

        if not self._sequence:
            raise NoSequenceSetError()

        if not self._shot:
            raise NoShotSetError()

        _shot_dir = self._pw.get_shot_path(
            self._sequence,
            self._shot
        )
        tasks = self.disk_wrapper.list_dir(_shot_dir)
        if not tasks:
            raise NoTasksFoundError(_shot_dir)
        return tasks

    def set_project(self, project):
        self._project = project
        self._project_path = os.path.join(self._pfs_path, project)
        self._pw = self.path_wrapper(self._project_path)

    def set_sequence(self, sequence):
        self._sequence = sequence

    def set_shot(self, shot):
        self._shot = shot

    def set_task(self, task):
        self._task = task


if __name__ == '__main__':
    from pprint import pprint

    path = Projects("D:\Desk\python\Projects")
    pprint(path.get_projects())
