# -*- coding: utf-8 -*-
import unittest
from hypothesis import given, strategies as s

from cebar.data_structures.chromosome import CHRTYPE, Chromosome


class ChromosomeTestCase(unittest.TestCase):
    CHROMOSOME_TYPES = [CHRTYPE.linear, CHRTYPE.circular]

    @given(name=s.text())
    def test_minimal_chromosome_creation(self, name):
        chromosome = Chromosome(name=name)
        self.assertEqual(chromosome.chr_type, CHRTYPE.linear)
        self.assertEqual(chromosome.name, name)
        self.assertEqual(len(chromosome.blocks), 0)
