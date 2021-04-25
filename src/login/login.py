from tkinter import *


def main_account_screen():
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Okno logowania")


    Label(text="Wybierz logowanie albo rejestracja", bg="#49A", width="300", height="2", font=("Arial", 13)).pack()
    Label(text="").pack()

    Button(text="Logowanie", height="2", width="30").pack()
    Label(text="").pack()

    Button(text="Rejestracja", height="2", width="30").pack()

    main_screen.mainloop()
