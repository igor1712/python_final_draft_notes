import time
import json


class All_notes:

    def __init__(self):
        self.note_list = []
        self.note_dict = {}
        self.id = None

    def times(self):
        sec = time.time()
        struct = time.localtime(sec)
        date = time.strftime('%d.%m.%Y %H:%M', struct)
        return date

    def add_note(self):
        self.id = len(self.note_list) +1
        head = (input('Заголовок... ')),
        body = (input('Текст заметки... ')),
        self.note_dict = \
            {
                self.id: {
                    "head": head,
                    "body": body,
                    "time": self.times()
                }
            }
        self.note_list.append(self.note_dict)
        return self.note_list

    def all_notes(self):
        for i in self.note_list:
            if isinstance(i,dict):
                for key,val in i.items():
                    print(f"id: {key}")
                    for k,v in i.items():
                        if isinstance(v,dict):
                            for sub_k, sub_v in v.items():
                                print(f'  {sub_k}: {sub_v}')

    def save_note_jsone(self):
        with open('file.json', 'w', encoding="UTF-8") as f:
            json.dump(self.note_dict, f)
            print('complite')

    def dell_note(self):
        self.all_notes()
        num = int(input("Введите индекс... "))
        self.note_list.pop(num - 1)
        return self.note_list

    def edit(self):
        self.all_notes()
        num = int(input("Введите индекс... "))
        text = input("Введите текст... ")
        self.note_list[num - 1][self.id]['body'] = text
        return self.note_list

    def load_file_json(self):
        with open("file.json") as f:
            print(f'{json.load(f)}\n')