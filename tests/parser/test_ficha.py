# -*- coding: utf-8 -*-
import unittest

from parser import *
from tests import factories


class TestTypes(unittest.TestCase):
    def assertValue(self, value, expected):
        self.assertEqual(get_value(value), expected)

    def test_parse_date(self):
        self.assertValue(factories.date_cell, u'2012-05-04')

    def test_parse_time(self):
        self.assertValue(factories.time_cell, u'09:22:00')

    def test_useless_spaces_in_field_names(self):
        self.assertValue(factories.nonstriped_cell, u'Umidade Ambiente')

class TestTorraDatails(unittest.TestCase):
    def test_find_cell(self):
        coord = (9, 2)
        sheet = factories.workbook.sheet_by_name('662')
        self.assertEqual(find_cell(u'FICHA TECNICA', sheet), coord)

    def test_fill_weight_loss(self):
        "This is a calculated field, its formula is `1-(D35/D34)`"
        details = {
            u'Qtd café cru (g)': u'4000',
            u'Qtd café Torrado (g)': u'3324',
        }
        fill_weight_loss(details)
        self.assertEqual(details[u'Perda Peso na Torra (%)'], u'16.90%')

