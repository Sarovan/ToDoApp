import functions
import FreeSimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkGrey8")

clock = sg.Text(key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10)
)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "My Todo App",
    layout=[
        [clock],
        [label],
        [input_box, add_button],
        [list_box, edit_button, complete_button],
        [exit_button],
    ],
    font=("Helvetica", 18),
    grab_anywhere=True,
)

while True:
    event, values = window.read(timeout=200)
    match event:
        case "Add":
            if values["todo"]:
                todos = functions.get_todos()
                todos.append(values["todo"] + "\n")
                functions.write_todos(todos)
                window["todos"].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                new_todo = values["todo"]
                todo_index = todos.index(values["todos"][0])
                todos[todo_index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup(
                    "Please select an item first",
                    font=("Helvetica", 16),
                    no_titlebar=True,
                )
        case "Complete":
            try:
                todos = functions.get_todos()
                todos.remove(values["todos"][0])
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup(
                    "Please select an item first",
                    font=("Helvetica", 16),
                    no_titlebar=True,
                )
        case "todos":
            window["todo"].update(value=values["todos"][0].strip())
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

window.close()
