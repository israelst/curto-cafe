# -*- coding: utf-8 -*-
import xlrd


workbook = xlrd.open_workbook('tests/example.xlsx')
sheet_662 = workbook.sheet_by_name('662')
date_cell = sheet_662.cell(24, 3)
time_cell = sheet_662.cell(13, 3)
nonstriped_cell = sheet_662.cell(15, 2)
