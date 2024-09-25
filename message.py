from datetime import datetime, date, time
from json import load, dump


class Message:
    def __init__(self, d=datetime.now(), fileName='db.json'):
        self.fileName = fileName
        self.load()
        self.dat = d.strftime("%y/%m/%d %H:%M")

    def load(self):
        try:
            with open(self.fileName) as fp:
                self.mess = load(fp)
        except FileNotFoundError:
            self.mess = {}

    def save(self):
        with open(self.fileName, 'w') as fp:
            dump(self.mess, fp)

    def add_message(self, titlee='Title', text='Text', categry='categry'):
        title = titlee
        self.mess[title] = {'creatingDate': self.dat, 'editDate': self.dat, 'text': text, 'category': categry}
        self.save()

    def remove_message(self, title):
        if title in self.mess:
            del self.mess[title]
            self.save()

    def get_messages(self):
        return self.mess

    def get_message(self, title):
        return self.mess.get(title, None)


# a = Message()

# print(a.mess)

# # добавлять пользователя
# a.add_message("Poll", '124')
# a.add_message("gfdgdf", '231231')
# a.remove_message("gfdgdf")

# # Сохранить файл
# a.save()
