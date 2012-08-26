# coding: utf-8
from google_spreadsheet.api import SpreadsheetAPI

from config.gdata import connection_data


def get_key(obj):
    return obj[1]

api = SpreadsheetAPI(*connection_data)
for spreadsheet in api.list_spreadsheets():
    for worksheet in api.list_worksheets(get_key(spreadsheet)):
        keys = map(get_key, (spreadsheet, worksheet))
        sheet = api.get_worksheet(*keys)
        rows = [l for l in w.get_rows()]
