import gspread
from gspread import Worksheet, Spreadsheet, Client


class SaveUserData:
    def __init__(self, name, username, chat_id, message):
        self.name = name
        self.username = username
        self.chat_id = chat_id
        self.message = message

    def insert(self, client, url):
        gc: Client = gspread.service_account(client)
        sh: Spreadsheet = gc.open_by_url(url)
        ws: Worksheet = sh.sheet1
        ws.append_row(values=[self.name, '@' + self.username, self.chat_id, self.message])

    def to_dict(self):
        return {'first name': self.name, 'username': self.username, 'chat_id': self.chat_id, 'message': self.message}
