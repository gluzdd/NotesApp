import text
from model import load_notes


def show_notes():
    list_notes = load_notes()
    if not list_notes:
        print("Заметок нет")
    else:
        for note in list_notes:
            print(f'{note["id"]}. {note["title"]} {note["datetime"]}')


def show_by_id(note_id):
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            print(f'{note["title"]} {note["message"]} {note["datetime"]}')
            return note_id
    print(f"Под таким id {note_id} нет заметок: ")


def menu():
    for i, item in enumerate(text.main_menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')

    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < len(text.main_menu):
            return int(choice)
        print(text.input_menu_error)
