# -*- coding: utf-8 -*-

from xlrd import xldate_as_tuple
from datetime import time, date


def sample_name(sheet):
    x, y = find_cell(u'Amostra', sheet)
    return get_value(sheet.cell(x+1, y))

def details(sheet):
    x, y = find_cell(u"FICHA TECNICA", sheet)
    details = key_value(x+1, y, x+1, y+1, sheet)
    fill_weight_loss(details)
    return details

def key_value(rowk, colk, rowv, colv, sheet):
    keys = filter(None, map(get_value, sheet.col_slice(colk, rowv)))
    values = map(get_value, sheet.col_slice(colv, rowv))[:len(keys)]
    return dict(zip(keys, values))

def roasting_target(sheet):
    x, y = find_cell(u"Parametros", sheet)
    return key_value(x+1, y, x+1, y+1, sheet)

def roasting_done(sheet):
    x, y = find_cell(u"Parametros", sheet)
    return key_value(x+1, y, x+1, y+2, sheet)

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
