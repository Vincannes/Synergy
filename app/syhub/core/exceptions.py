#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes

class NoProjectSetError(Exception):
    "Raised when no project has been set."
    pass


class NoSequenceSetError(Exception):
    "Raised when no sequence has been set."
    pass


class NoShotSetError(Exception):
    "Raised when no shot has been set."
    pass


class NoSequencesFoundError(Exception):
    "Raised when no sequences found for a given project."

    def __init__(self, project_name):
        super().__init__(
            f"No sequence found for this project: {project_name}"
        )


class NoShotsFoundError(Exception):
    "Raised when no shots found for a given project."

    def __init__(self, shot_name):
        super().__init__(
            f"No shot found for this sequence: {shot_name}"
        )


class NoTasksFoundError(Exception):
    "Raised when no shots found for a given project."

    def __init__(self, task_name):
        super().__init__(
            f"No task found for this sequence: {task_name}"
        )
