# -*- coding: utf-8 -*-
import unittest

from hypothesis import given, strategies as s

from cebar.data_structures.block import Block, Orientation


class BlockTestCase(unittest.TestCase):

    @given(name=s.text())
    def test_default_orientation(self, name):
        block = Block(name)
        self.assertEqual(block.orientation, Orientation.forward)
