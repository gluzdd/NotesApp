import json
import os.path
from datetime import datetime

PATH = "notes.json"

if not os.path.exists(PATH):
    with open(PATH, "w") as file:
        json.dump([], file)

def load_notes():
    with open(PATH, "r") as file:
        return json.load(file)


def save_notes(notes):
    with open(PATH, "w") as file:
        json.dump(notes, file, indent=4)


def add_note(title, message):
    list_notes = load_notes()
    note = {"id": len(list_notes) + 1,
            "title": title,
            "message": message,
            "datetime": datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
    list_notes.append(note)
    save_notes(list_notes)
    print("Заметка успешно добавлена")


def edit_note(note_id, new_title, new_message):
    list_notes = load_notes()
    for note in list_notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["message"] = new_message
            note["datetime"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            save_notes(list_notes)
            print("Заметка успешно изменена")
            return note_id
    print(f"Заметка с таким {note_id} ID не найдена")


def delete_note(note_id):
    list_notes = load_notes()
    for note in list_notes:
        if note["id"] == note_id:
            list_notes.remove(note)
            save_notes(list_notes)
            print("Заметка успешно удалена")
            return note_id
    print(f"Заметка с таким {note_id} ID не найдена")

