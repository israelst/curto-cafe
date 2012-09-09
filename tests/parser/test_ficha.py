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

class TestRoastingProgess(unittest.TestCase):
    def test_roasting_progress(self):
        expected = [
           (u'0', u'220', u'igual'),
           (u'0.25', u'170', u'igual'),
           (u'0.5', u'128', u'igual'),
           (u'0.75', u'103', u'igual'),
           (u'1', u'92', u'igual'),
           (u'1.25', u'86', u'igual'),
           (u'1.5', u'85', u'a1'),
           (u'1.75', u'88', u'igual'),
           (u'2', u'91', u'igual'),
           (u'2.25', u'93', u'igual'),
           (u'2.5', u'101', u'igual'),
           (u'2.75', u'103', u'igual'),
           (u'3', u'106', u'igual'),
           (u'3.25', u'109', u'igual'),
           (u'3.5', u'115', u'igual'),
           (u'3.75', u'118', u'igual'),
           (u'4', u'121', u'igual'),
           (u'4.25', u'124', u'igual'),
           (u'4.5', u'128', u'igual'),
           (u'4.75', u'131', u'igual'),
           (u'5', u'134', u'igual'),
           (u'5.25', u'139', u'igual'),
           (u'5.5', u'143', u'igual'),
           (u'5.75', u'146', u'igual'),
           (u'6', u'150', u'igual'),
           (u'6.25', u'153', u'igual'),
           (u'6.5', u'156', u'igual'),
           (u'6.75', u'159', u'igual'),
           (u'7', u'163', u'igual'),
           (u'7.25', u'166', u'igual'),
           (u'7.5', u'169', u'igual'),
           (u'7.75', u'172', u'd1'),
           (u'8', u'176', u'igual'),
           (u'8.25', u'179', u'igual'),
           (u'8.5', u'183', u'igual'),
           (u'8.75', u'186', u'igual'),
           (u'9', u'189', u'igual'),
           (u'9.25', u'191', u'igual'),
           (u'9.5', u'193', u'igual'),
           (u'9.75', u'196', u'igual'),
           (u'10', u'199', u'igual'),
           (u'10.25', u'201', u'igual'),
           (u'10.5', u'203', u'igual'),
           (u'10.75', u'206', u'igual'),
           (u'11', u'210', u'igual'),
           (u'11.25', u'213', u'igual'),
           (u'11.5', u'214', u'igual'),
        ]
        self.assertEqual(expected, roasting_progress(factories.sheet_662))

class TestRoastingDatails(unittest.TestCase):
    def setUp(self):
        self.sheet = factories.sheet_662

    def assertDict(self, result, expected):
        for k, v in expected.iteritems():
            self.assertEqual(result[k], expected[k])
        self.assertEqual(result, expected)

    def test_get_sample_name(self):
        self.assertEqual(sample_name(self.sheet), u'662')

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
