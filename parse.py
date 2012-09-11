# -*- coding: utf-8 -*-
import os
import csv
import codecs

import parser

from xlrd import open_workbook

encode = lambda _:codecs.encode(_, 'utf-8')

def filter_xls(dir_list):
    return filter(lambda _: os.path.splitext(_)[-1] == u'.xls', dir_list)

root_path = os.path.abspath('spreadsheets')
paths = filter_xls(os.listdir(root_path))


roastings = []
for path in paths:
    wb = open_workbook(os.path.join(root_path, path))
    for s in wb.sheets():
        try:
            roastings.append(((path.decode(), s.name), parser.roasting_progress(s)))
        except:
           # print (path, s.name)
           pass

with file('output.csv', 'wr') as output:
    csv_writer = csv.writer(output)
    csv_writer.writerow(u'path', u'sheet', u'time', u'temp', u'flame')))
    for roasting in roastings:
        id, data = roasting
        path, sheet = id
        for row in data:
            time, temp, flame = row
            print path, sheet, time, temp, flame
            csv_writer.writerow(map(encode, (path, sheet, time, temp, flame)))
