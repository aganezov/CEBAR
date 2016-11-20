# -*- coding: utf-8 -*-
import enum


class Orientation(enum.Enum):
    forward = "+"
    reverse = "-"
    unknown = "?"


class Block(object):
    def __init__(self, name, orientation=Orientation.forward):
        self.orientation = orientation
        self.name = name
