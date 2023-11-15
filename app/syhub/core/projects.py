#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

import os

from app.syhub.adapters.disk_wrapper import DiskWrapper
from app.syhub.core.path import Paths
from app.syhub.core.exceptions import (
    NoSequencesFoundError, NoProjectSetError,
    NoShotSetError, NoSequenceSetError, NoShotsFoundError
)


class Projects(object):
    path_wrapper = Paths
    disk_wrapper = DiskWrapper

    def __init__(self, pfs):
        self._pfs_path = pfs
        
        self._pw = None
        self._project = None
        self._sequence = None
        self._project_path = None

    def get_projects(self):
        return self.disk_wrapper.list_dir(self._pfs_path)

    def set_project(self, project):
        self._project = project
        self._project_path = os.path.join(self._pfs_path, project)
        self._pw = self.path_wrapper(self._project_path)

    def set_sequence(self, sequence):
        self._sequence = sequence

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

if __name__ == '__main__':
    from pprint import pprint
    path = Projects("D:\Desk\python\Projects")
    pprint(path.get_projects())
