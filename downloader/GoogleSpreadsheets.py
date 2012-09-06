#!/usr/bin/python

import re, requests

class Client:
    def __init__(self, email, password, source, service='wise'):
        self.email = email
        self.password = password
        self.source = source
        self.service = service

    def get_auth_token(self):
        """Get auth token as described at \
        https://developers.google.com/accounts/docs/AuthForInstalledApps#Request"""

        url = "https://www.google.com/accounts/ClientLogin"
        data= {
            "Email": self.email, "Passwd": self.password,
            "service": self.service,
            "accountType": "HOSTED_OR_GOOGLE",
            "source": self.source,
        }
        response = requests.post(url, data=data)
        response.raise_for_status()
        return re.findall(r"Auth=(.*)", response.text)[0]

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
    from config.gdata import connection_data

    spreadsheet_key = "0AsmXhe3Jaw0hdF83S2RGRHhpQzBsbkN5SGRWZ3NLcVE"
    gs = Client(*connection_data)
    response = gs.download(spreadsheet_key, 38)
    with open('file.ods', 'w') as f:
        f.write(response.content)
