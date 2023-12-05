import os

import gspread
from dotenv import load_dotenv
from gspread import Worksheet, Spreadsheet, Client

load_dotenv()


class SaveUserData:
    def __init__(self, name, username, chat_id, message):
        self.name = name
        self.username = username
        self.chat_id = chat_id
        self.message = message
        self.gc: Client = gspread.service_account('ServiceData.json')
        self.sh: Spreadsheet = self.gc.open_by_url(os.getenv('SPREADSHEET_URL'))

    def insert(self):
        ws: Worksheet = self.sh.sheet1
        ws.append_row(values=[self.name, '@' + self.username, self.chat_id, self.message])

    def to_dict(self):
        return {'first name': self.name, 'username': self.username, 'chat_id': self.chat_id, 'message': self.message}
