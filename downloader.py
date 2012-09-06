#!/usr/bin/python

from config.gdata import connection_data
from downloader.GoogleSpreadsheets import Client

spreadsheet_key = "0AsmXhe3Jaw0hdF83S2RGRHhpQzBsbkN5SGRWZ3NLcVE"
gs = Client(*connection_data)
response = gs.download(spreadsheet_key, 38)
with open('file.ods', 'w') as f:
    f.write(response.content)
