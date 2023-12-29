#!/usr/bin/env python
# #support	:Trolard Vincent
# copyright	:Vincannes
from abc import ABC, abstractmethod


class AbsDccWrapper(ABC):

    @staticmethod
    def open(path):
        NotImplementedError

    @staticmethod
    def close():
        NotImplementedError

    @staticmethod
    def clear():
        NotImplementedError

    @staticmethod
    def save():
        NotImplementedError

    @staticmethod
    def message(msg):
        NotImplementedError

    @staticmethod
    def get_current_scene():
        NotImplementedError
