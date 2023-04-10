from All_notes import *

def play():
    notes = All_notes()

    menu = """Добро пожаловать в заметки.
     1. Список всех заметок.
     2. Создать заметку.
     3. Редактировать заметку.
     4. Удалить заметку.
     5. Сохранить заметку.
     6. Загрузить из jsone.
     
     0. Завершить работу.
     """
    print(menu)

    while(True):

        num = int(input("Введите цифру: "))
        if num == 1:
            notes.all_notes()
            continue
        elif num == 2:
            notes.add_note()
            continue
        elif num == 3:
            notes.edit()
            continue
        elif num == 4:
            notes.dell_note()
            continue
        elif num == 5:
            notes.save_note_jsone()
            continue
        elif num == 6:
            notes.load_file_json()
            continue
        elif num == 0:
            print("Программа завершена")
            break

