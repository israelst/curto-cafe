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

class TestRoastingDatails(unittest.TestCase):
    def setUp(self):
        self.sheet = factories.sheet_662

    def assertDict(self, result, expected):
        for k, v in expected.iteritems():
            self.assertEqual(result[k], expected[k])
        self.assertEqual(result, expected)

    def test_find_cell(self):
        coord = (9, 2)
        self.assertEqual(find_cell(u'FICHA TECNICA', self.sheet), coord)

    def test_fill_weight_loss(self):
        "This is a calculated field, its formula is `1-(D35/D34)`"
        details = {
            u'Qtd café cru (g)': u'4000',
            u'Qtd café Torrado (g)': u'3324',
        }
        fill_weight_loss(details)
        self.assertEqual(details[u'Perda Peso na Torra (%)'], u'16.90%')

    def test_rosting_target(self):
        expected = {
            u'Sabor': u'Amendoado',
            u"Chama Inicial (ºC)": u"220",
            u'Tempo do 1° Crack (min)': u'9',
            u'Temperatura 1° Crack (ºC)': u'189',
            u'Tempo Final (min)': u'11.5',
            u'Temperatura Final (ºC)': u'214',
        }
        self.assertDict(roasting_target(self.sheet), expected)


    def test_rosting_done(self):
        expected = {
            u'Sabor': u'',
            u"Chama Inicial (ºC)": u'',
            u'Tempo do 1° Crack (min)': u'',
            u'Temperatura 1° Crack (ºC)': u'',
            u'Tempo Final (min)': u'',
            u'Temperatura Final (ºC)': u'',
        }
        self.assertDict(roasting_done(self.sheet), expected)

    def test_details(self):
        expected = {
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
             u'Altitude (m)': u'750',
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
             u'Qtd café cru (g)': u'4000',
             u'Qtd café Torrado (g)': u'3324',
             u'Perda Peso na Torra (%)': u'16.90%',
             u'Observações da Torra': u'',
        }
        self.assertDict(details(self.sheet), expected)
