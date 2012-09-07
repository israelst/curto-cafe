# -*- coding: utf-8 -*-
import unittest

from parser import find_cell
from tests import factories


class TestTorraDatails(unittest.TestCase):
    def test_find_cell(self):
        coord = (9, 2)
        sheet = factories.workbook.sheet_by_name('662')
        self.assertEqual(find_cell(u'FICHA TECNICA', sheet), coord)
