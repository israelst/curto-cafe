# -*- coding: utf-8 -*-

from xlrd import xldate_as_tuple
from datetime import time, date


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
            value = unicode(time(*datetime_value[3:]))
        else:
            value = unicode(date(*datetime_value[:3]))
        return value
    else:
        return cell
    #print cell.ctype, cell.value, value
