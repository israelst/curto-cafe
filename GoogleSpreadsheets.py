#!/usr/bin/python

import re, requests

class Client(object):
    def __init__(self, email, password):
        super(Client, self).__init__()
        self.email = email
        self.password = password

    def _get_auth_token(self, email, password, source, service):
        url = "https://www.google.com/accounts/ClientLogin"
        data= {
            "Email": email, "Passwd": password,
            "service": service,
            "accountType": "HOSTED_OR_GOOGLE",
            "source": source
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return re.findall(r"Auth=(.*)", response.text)[0]

    def get_auth_token(self):
        source = type(self).__name__
        return self._get_auth_token(self.email, self.password, source, service="wise")

    def download(self, spreadsheet_key, gid=0, format="ods"):
        url = "https://spreadsheets.google.com/feeds/download/spreadsheets/Export"
        params = {
            'key': spreadsheet_key,
            'exportFormat': format, 
            'gid': gid,
        }
        headers = {
            "Authorization": "GoogleLogin auth=" + self.get_auth_token(),
            "GData-Version": "3.0"
        }
        response = requests.get(url, params=params, headers=headers)
        return response

if __name__ == "__main__":
    from config.gdata import email, password

    spreadsheet_key = "0AsmXhe3Jaw0hdF83S2RGRHhpQzBsbkN5SGRWZ3NLcVE"
    gs = Client(email, password)
    response = gs.download(spreadsheet_key, 38, "xls")
    with open('file.xls', 'w') as xls:
        xls.write(response.content)
