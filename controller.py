from model import *
from view import *


def start():

    while True:
        choice = menu()
        match choice:
            case 1:
                title = input("Введите заголовок: ")
                message = input("Введите заметку: ")
                add_note(title, message)
            case 2:
                show_notes()
            case 3:
                note_id = int(input("Введите id для поиска заметки: "))
                show_by_id(note_id)
            case 4:
                note_id = int(input("Введите id заметки для редактирования: "))
                new_title = input("Введите новый заголовок: ")
                new_message = input("Введите новую заметку: ")
                edit_note(note_id, new_title, new_message)
            case 5:
                note_id = int(input("Введите id заметки для удаления: "))
                delete_note(note_id)
            case 6:
                print("Завершение работы")
                break


