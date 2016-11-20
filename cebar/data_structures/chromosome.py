# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import enum


class CHRTYPE(enum.Enum):
    circular = 0
    linear = 1


class Chromosome(object):
    def __init__(self, name, chr_type=CHRTYPE.linear, blocks=None):
        self.name = name
        self.chr_type = chr_type
        self.blocks = blocks if blocks is not None else []
