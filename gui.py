import functions
import FreeSimpleGUI as sg

label=sg.Text('Type in a todo')
input_box=sg.InputText(tooltip='Enter a todo', key='todo')
add_button=sg.Button('Add')

window=sg.Window('My Todo App',
                 layout=[[label],[input_box, add_button]],
                 font=('Helvetica',20))
while True:
    event, values=window.read()
    match event:
        case "Add":
            todos=functions.get_todos()
            todos.append(values['todo']+'\n')
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break


window.close()