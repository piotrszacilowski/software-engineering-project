from tkinter import *
from tkinter import filedialog
import upload_data as uploadData
import visualization_menu


def main_menu():
    global main_screen

    main_screen = Tk()
    main_screen.geometry("300x450")
    main_screen.title("Menu główne")

    Label(text="Co chcesz zrobić?", bg="#49A", width="300", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    Button(text="Wizualizacje", height="2", width="30",
        command=lambda: visualization_menu.visualizations(main_screen)).pack()
    Label(text="").pack()

    Button(text="Wybierz dane", height="2", width="30", command=lambda: uploadData.upload_data(main_screen)).pack()
    Label(text="").pack()

    Button(text="Wyloguj", height="2", width="15", command=lambda: exit()).pack()
    Label(text="").pack()

    main_screen.mainloop()

    # To Do
    # Przycisk Exit (?)
