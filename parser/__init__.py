# -*- coding: utf-8 -*-


def _rows(sheet):
    for row_index in xrange(sheet.nrows):
        yield sheet.row_values(row_index)

def find_cell(value, sheet):
    for i, row in enumerate(_rows(sheet)):
        try: return i, row.index(value)
        except ValueError: pass

    return None, None

