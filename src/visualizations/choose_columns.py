import tkinter
from tkinter import *
from globals import get_metadata, set_metadata, get_selection
from visualizations.scatterplot import generate_scatterplot

def choose_columns_screen():
    global choose_screen
    choose_screen = Tk()
    choose_screen.geometry("300x250")
    choose_screen.title("Wybierz dane do wykresu")

    meta = get_metadata()

    # Metadata not gathered? - show alert and return
    if meta == None:
        choose_screen.destroy()
        show_method = getattr(tkinter.messagebox, 'show{}'.format("warning"))
        show_method("Error", "Dataset not selected.")       
        return

    # Not enough numeric columns - show alert and return
    numericColumnData = meta.get_numeric_columns()
    if numericColumnData[0] < 1:
        choose_screen.destroy()
        show_method = getattr(tkinter.messagebox, 'show{}'.format("warning"))
        show_method("Error", "Not enough numeric types in dataset.")       
        return

    Label(choose_screen, text="X:", height="2", font=("Arial", 13)).pack()
    Label(choose_screen, text="").pack()
    clickedX = StringVar(choose_screen)
    clickedX.set( numericColumnData[1][0] )
    dropX = OptionMenu( choose_screen , clickedX , *numericColumnData[1],  )
    dropX.pack()
    
    Label(choose_screen, text="Y:", height="2", font=("Arial", 13)).pack()
    Label(choose_screen, text="").pack()
    clickedY = StringVar(choose_screen)
    clickedY.set( numericColumnData[1][0] )
    dropY = OptionMenu( choose_screen , clickedY , *numericColumnData[1],  )
    dropY.pack()       
    Label(choose_screen, text="").pack()
    def submit_choice_and_return():
        sX = clickedX.get()
        sY = clickedY.get()
        #print("SX:", sX, "\nSY:", sY)
        c1 = 0
        c2 = 0
        for i, c in enumerate(meta.columns):
            if c == sX:
                c1 = i
            if c == sY:
                c2 = i
        #print(meta.columns)
        #print("c1:", c1, "\nc2:", c2)
        meta.chosenColumns = [c1, c2]
        set_metadata(meta)
        choose_screen.destroy()
        generate_scatterplot(get_selection())

    Button(choose_screen, text='Dalej', height="1", width="15", command=submit_choice_and_return ).pack()

    choose_screen.mainloop()
    