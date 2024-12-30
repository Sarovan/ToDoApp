import FreeSimpleGUI as sg

sg.theme("Black")

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input(key="inches")

button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button = sg.Button("Exit")

window = sg.Window(
    title="Converter",
    layout=[
        [feet_label, feet_input],
        [inches_label, inches_input],
        [button, exit_button, output_label],
    ],
    font=("", 16),
)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    meters = float(values["feet"]) * 0.3048 + float(values["inches"]) * 0.0254
    result = f"{meters} m"
    window["output"].update(value=result)

window.close()
