# -*- coding: utf-8 -*-
import unittest
from cebar.data_structures.block import Block, Orientation
from hypothesis import given, assume, strategies as s


class BlockTestCase(unittest.TestCase):
    ORIENTATIONS = [Orientation.forward, Orientation.reverse]

    @given(name=s.text())
    def test_default_orientation(self, name):
        block = Block(name)
        self.assertEqual(block.orientation, Orientation.forward)

    @given(orientation=s.sampled_from(ORIENTATIONS))
    def test_reverse_orientation(self, orientation):
        block = Block(name="name", orientation=orientation)
        self.assertEqual(block.orientation, orientation)
        block.reverse()
        self.assertNotEqual(block.orientation, orientation)
        self.assertIn(block.orientation, self.ORIENTATIONS)

    @given(name=s.text(), orientation=s.sampled_from(ORIENTATIONS), show_plus=s.booleans())
    def test_str_(self, name, orientation, show_plus):
        assume(len(name) > 0)
        block = Block(name=name, orientation=orientation)
        str_representation = block.as_string(show_plus=show_plus)
        if orientation == Orientation.forward and show_plus:
            self.assertTrue(str_representation.startswith("+"))
        if orientation == Orientation.reverse:
            self.assertTrue(str_representation.startswith("-"))
        self.assertTrue(str_representation.endswith(name))
