import FreeSimpleGUI as sg
from bonus18_functions import extract_files

archive_text = sg.Text("Select archive:")
archive_input = sg.Input(key="archive")
archive_button = sg.FileBrowse("Choose")

destination_text = sg.Text("Select folder:")
destination_input = sg.Input(key="folder")
destination_button = sg.FolderBrowse("Choose")

extract_button = sg.Button("Extract")
extract_text = sg.Text(key="extract_text")

window = sg.Window(
    title="Archive Extractor",
    font=("Helvetica", 16),
    layout=[
        [archive_text, archive_input, archive_button],
        [destination_text, destination_input, destination_button],
        [extract_button, extract_text],
    ],
)

while True:
    event, values = window.read()
    # print(event)
    # print(values)
    match event:
        case "Extract":
            archive = values["archive"]
            dest = values["folder"]
            extract_files(archive, dest)
            window["extract_text"].update(value="Extraction complete!")
        case sg.WINDOW_CLOSED:
            break

window.close()
