import zipfile
import pathlib


def extract_files(archive, dest):
    print(archive, dest)
    # archive = pathlib.Path(archive)
    # dest = pathlib.Path(dest)
    print(archive, dest)
    with zipfile.ZipFile(archive, "r") as file:
        file.extractall(dest)


if __name__ == "__main__":
    extract_files(
        "test.zip",
        r"C:\Users\akazm\Documents\Python Learning\Udemy_Ardit_course\ToDoApp\quiz\testfolder",
    )
