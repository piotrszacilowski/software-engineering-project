from tkinter import *
from tkinter import filedialog
from typing import TextIO

from globals import set_tree_dataset
from visualizations.tree import generate_tree

def dataset_picker_screen():

    data_screen = Tk()
    data_screen.wm_title = "Scatterplot"

    data_screen.geometry("300x450")
    data_screen.title("Wybór danych")

    Label(data_screen, text="Wybierz dataset z listy\ni maksymalną liczbę liści", bg="#49A", width="300", height="3",
          font=("Arial", 13)).pack()
    Label(data_screen, text="").pack()

    Button(
        data_screen,
        text="Iris", 
        height="2", 
        width="30", 
        command=lambda: set_tree_dataset(0)
    ).pack()

    Button(
        data_screen, 
        text="Digits", 
        height="2",
        width="30",
        command=lambda: set_tree_dataset(1)
    ).pack()

    Button(
        data_screen, 
        text="Wine", 
        height="2", 
        width="30", 
        command=lambda: set_tree_dataset(2)
    ).pack()

    Button(
        data_screen, 
        text="Breast cancer",
        height="2", 
        width="30", 
        command=lambda: set_tree_dataset(3)
    ).pack()

    Label(data_screen, text="").pack()

    Label(data_screen, text="Maksymalna liczba liści:", height="2", font=("Arial", 13)).pack()
    clicked = StringVar(data_screen)
    clicked.set( 3 )
    drop = OptionMenu( data_screen , clicked , *[3,4,5,6,7,8,9,10,11,12,13,14,15],  )
    drop.pack()

    Label(data_screen, text="").pack()

    Button(
        data_screen, 
        text='Dalej',
        height="1", 
        width="15", 
        command=lambda: generate_tree(int(clicked.get()))
    ).pack()

    Label(data_screen, text="").pack()

    Button(
        data_screen, 
        text='Powrót',
        height="1", 
        width="15", 
        command=lambda: data_screen.destroy()
    ).pack()
