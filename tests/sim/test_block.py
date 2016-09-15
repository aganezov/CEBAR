# -*- coding: utf-8 -*-
import unittest
from cebar.sim.block import Block, Orientation
from hypothesis import given, strategies as s


class BlockTestCase(unittest.TestCase):

    @given(name=s.text())
    def test_default_orientation(self, name):
        block = Block(name)
        self.assertEqual(block.orientation, Orientation.forward)
