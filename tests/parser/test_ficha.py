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
    def setUp(self):
        self.sheet = factories.sheet_662

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

    def test_details(self):
        result = {
             u'Mestre-de-Torra': u'Mario',
             u'Cópia da Torra': '',
             u'Data': u'2012-08-03',
             u'Hora': u'09:22:00',
             u'Temp (°C)': u'23,4°',
             u'Umidade Ambiente': u'0.49',
             u'Produtor': u'Jose Lucio',
             u'Sítio': u'Joao Altoe',
             u'Localidade': u'Caxixe Quente',
             u'Cidade': u'Castelo',
             u'Estado': u'Espirito Santo',
             u'Altitude (m)': u'750.0',
             u'Variedade do Arábica': u'Arabica (Catuai)',
             u'Processo': u'Cereja Descascado',
             u'Data da Colheita': u'2012-05-04',
             u'Data Processamento': u'2012-05-04',
             u'Data Secagem': u'2012-05-04',
             u'Data Tulha': u'2012-05-12',
             u'Data Beneficiamento': u'2012-07-03',
             u'Umidade do Grao': u'12,5°',
             u'Classificação própria': u'1A',
             u'Peneira': u'17 acima',
             u'Catação Manual de Defeitos?': u'Sim',
             u'Qtd café cru (g)': u'4000.0',
             u'Qtd café Torrado (g)': u'3324.0',
             u'Perda Peso na Torra (%)': u'16.90%',
             u'Observações da Torra': u'',
        }
        for k, v in result.iteritems():
            print k, details(self.sheet)[k], result[k]
            self.assertEqual(details(self.sheet)[k], result[k])
        self.assertEqual(details(self.sheet), result)
