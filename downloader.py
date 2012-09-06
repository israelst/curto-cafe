#!/usr/bin/python

from config.gdata import connection_data
from downloader.GoogleSpreadsheets import Client


spreadsheet_key = "0AsmXhe3Jaw0hdF83S2RGRHhpQzBsbkN5SGRWZ3NLcVE"
gs = Client(*connection_data)
file_format = "ods"
response = gs.download(spreadsheet_key, 38, file_format)
with open('file.{}'.format(file_format), 'w') as f:
    f.write(response.content)
