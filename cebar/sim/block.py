# -*- coding: utf-8 -*-
import enum


class Orientation(enum.Enum):
    forward = "+"
    reverse = "-"


class Block(object):
    def __init__(self, name, orientation=Orientation.forward):
        self.orientation = orientation
        self.name = name

    def reverse(self):
        self.orientation = Orientation.forward if self.orientation == Orientation.reverse else Orientation.reverse

    def as_string(self, show_plus):
        return "{sign}{name}".format(sign="" if self.orientation == Orientation.forward and not show_plus else self.orientation.value, name=self.name)
