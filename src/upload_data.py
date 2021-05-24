from tkinter import *
from tkinter import filedialog
from typing import TextIO

from datasets import *
from globals import set_selection, get_selection, set_metadata
from visualizations.dataset_meta import metadata


def browse_file():  # Browse and upload file from explorer, to use in future

    file = filedialog.askopenfile(initialdir="/", title="Select a File",
                                  filetypes=(("Tab files", "*.tab*"), ("Csv files", "*.csv*"), ("All files", "*.*")))
    
    set_selection(file.name)

def open_file(path, mode):
    global selection
    selection = "./src/datasets/" + path
    selectionAlt = "./datasets/" + path
    set_selection(selection)
    meta = metadata()
    meta.collect_metadata(selection, selectionAlt)
    set_metadata(meta)
    print(meta)


def upload_data(main_screen):
    global data_screen

    data_screen = Toplevel(main_screen)
    data_screen.geometry("300x450")
    data_screen.title("Upload danych")

    Label(data_screen, text="Dodaj własny dataset \nlub wybierz jeden z listy", bg="#49A", width="300", height="3",
          font=("Arial", 13)).pack()
    Label(data_screen, text="").pack()

    Button(data_screen, text="Wybierz plik", height="2", width="30", command=lambda: browse_file()).pack()
    Label(data_screen, text="").pack()

    Button(data_screen, text="Iris", height="2", width="30", command=lambda: open_file('iris.tab', 'r')).pack()
    Button(data_screen, text="Heart_disease", height="2", width="30",
           command=lambda: open_file('heart_disease.tab', 'r')).pack()
    Button(data_screen, text="Titanic", height="2", width="30", command=lambda: open_file('titanic.tab', 'r')).pack()
    Button(data_screen, text="ZOO", height="2", width="30", command=lambda: open_file('zoo.tab', 'r')).pack()
    Label(data_screen, text="").pack()
    Button(data_screen, text='Powrót', height="1", width="15", command=lambda: data_screen.destroy()).pack()
