# -*- coding: utf-8 -*-

from xlrd import xldate_as_tuple
from datetime import time, date


def details(sheet):
    x, y = find_cell(u"FICHA TECNICA", sheet)
    keys = map(get_value, sheet.col_slice(y, x+1))
    values = map(get_value, sheet.col_slice(y+1, x+1))
    details = dict(zip(keys, values))
    del details[u'']
    fill_weight_loss(details)
    return details

def roasting_target(sheet):
    x, y = find_cell(u"Parametros", sheet)
    keys = filter(None, map(get_value, sheet.col_slice(y, x+1)))
    values = map(get_value, sheet.col_slice(y+1, x+1))[:len(keys)]
    return dict(zip(keys, values))

def _rows(sheet):
    for row_index in xrange(sheet.nrows):
        yield sheet.row_values(row_index)

def find_cell(value, sheet):
    for i, row in enumerate(_rows(sheet)):
        try: return i, row.index(value)
        except ValueError: pass

    return None, None

def get_value(cell):
    if cell.ctype == 3:
        datetime_value = xldate_as_tuple(cell.value, 0)
        if datetime_value[0] == 0:
            value = time(*datetime_value[3:])
        else:
            value = date(*datetime_value[:3])
    elif cell.ctype == 2:
        value = int(cell.value) if cell.value.is_integer() else cell.value
    else:
        value = cell.value

    return unicode(value).strip()

def fill_weight_loss(details):
    unroasted, roasted = details[u'Qtd café cru (g)'], details[u'Qtd café Torrado (g)']
    weight_loss = (1 - float(roasted)/float(unroasted)) * 100
    details[u'Perda Peso na Torra (%)'] = u'{:.2f}%'.format(weight_loss)
