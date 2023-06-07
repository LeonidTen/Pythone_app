
import json
import datetime

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

# Функция для добавления новой заметки
def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'created_at': datetime.datetime.now().isoformat(),
        'updated_at': datetime.datetime.now().isoformat()
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

# Функция для редактирования заметки
def edit_note():
    note_id = int(input("Введите идентификатор заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            title = input("Введите новый заголовок заметки: ")
            body = input("Введите новое тело заметки: ")
            note['title'] = title
            note['body'] = body
            note['updated_at'] = datetime.datetime.now().isoformat()
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным идентификатором не найдена")

# Функция для удаления заметки
def delete_note():
    note_id = int(input("Введите идентификатор заметки для удаления: "))
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_notes(notes)
            print("Заметка успешно удалена")
            return
    print("Заметка с указанным идентификатором не найдена")

# Функция для чтения заметок с фильтрацией по дате
def read_notes():
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
        filtered_notes = [note for note in notes if note['created_at'].startswith(date_str)]
        if len(filtered_notes) > 0:
            print("Заметки, созданные в указанную дату:")
            for note in filtered_notes:
                print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело: {note['body']}")
        else:
            print("Заметки, созданные в указанную дату, не найдены")
    except ValueError:
        print("Некорректный формат даты")

# Основной код
notes = load_notes()


notes
while True:
    command = 
    command

input("Введите команду (add, edit, delete, read или exit): ")

if command == "add":
        add_note()
    
        add_note()
   

        add_note()

       
elif command == "edit":
        edit_note()
    
        edit_note()
   

        edit_note()

       
elif command == "delete":
        delete_note()
    
        delete_note()
   

        delete_note()

       
elif command == "read":
        read_notes()
    
        read_notes()
   

        read_notes()

       
elif command == "exit":
       
break
   
else:
      
print("Некорректная команда")

print("Завершение программы")
