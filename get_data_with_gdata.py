# coding: utf-8
import gdata.spreadsheet.service

from config.gdata import connection_data


service = gdata.spreadsheet.service.SpreadsheetsService()
service.ClientLogin(*connection_data)
document = service.GetWorksheetsFeed("0AsmXhe3Jaw0hdF83S2RGRHhpQzBsbkN5SGRWZ3NLcVE")
print u"Title", document.title
print u"Author", document.author[0].name.text
print u"worksheets:"
for worksheet in document.entry:
    print worksheet
