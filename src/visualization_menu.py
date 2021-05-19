from tkinter import *
from tkinter import filedialog

from globals import get_selection, get_metadata
from visualizations.scatterplot import generate_scatterplot
from visualizations.scatterplotMatrix import generate_scatterplot_matrix
from visualizations.choose_columns import choose_columns_screen

def visualizations(main_screen):
    #global visualizations_screen
    visualizations_screen = Toplevel(main_screen)

    visualizations_screen.geometry("300x450")
    visualizations_screen.title("Wizualizacje")

    Label(
        visualizations_screen,
        text="Wybierz wizualizacje",
        bg="#49A",
        width="300",
        height="2",
        font=("Arial", 13)
    ).pack()

    Button(
        visualizations_screen, 
        height="2", 
        width="30",
        text="Scatterplot", 
        command=lambda: choose_columns_screen() 
        #generate_scatterplot(get_selection(), [0, 1])
      ).pack()
    Label(visualizations_screen, text="").pack()
    Button(
        visualizations_screen,
        height="2", 
        width="30",
        text="Scatterplot Matrix",
        command=lambda: generate_scatterplot_matrix(get_selection()),     
    ).pack()
    Label(visualizations_screen, text="").pack()
    Button(
        visualizations_screen,
        height="2", 
        width="30",
        text="Tree",
        #command=lambda: generate_scatterplot_matrix(get_selection()),     
    ).pack()
    Label(visualizations_screen, text="").pack()
    Button(
        visualizations_screen, 
        text='Powrót', 
        height="1", 
        width="15",
        command=lambda: visualizations_screen.destroy()
    ).pack()
