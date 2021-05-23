import tkinter

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.axis as axis

from globals import get_metadata

def generate_scatterplot(file):

    scatterplot_screen = tkinter.Tk()
    scatterplot_screen.wm_title = "Scatterplot"

    meta = get_metadata()

    # Skip type and meta rows in datasets based on file extension
    rowsSkipped = 1    
    if meta.delimiter == '\t':
        rowsSkipped = 3

    data = open(file).readlines()
    usedColumn = [[],[]]

    for i, line in enumerate(data):
        if i <= rowsSkipped:
            continue
        splitLine = line.split(meta.delimiter)
        usedColumn[0].append(  float(splitLine[ meta.chosenColumns[ 0 ] ] ) )
        usedColumn[1].append(  float(splitLine[ meta.chosenColumns[ 1 ] ] ) )

    fig = Figure(figsize=(5, 4), dpi=100)
    plot = fig.add_subplot()    

    plot.set_ylabel(meta.columns[ meta.chosenColumns[0] ])
    plot.set_xlabel(meta.columns[ meta.chosenColumns[1] ])

    plot.scatter(
        usedColumn[0],
        usedColumn[1]
    )
    #plot.hist2d(data['0'], data['1'])
    #plot1 = fig.add_subplot()

    canvas = FigureCanvasTkAgg(fig, master=scatterplot_screen)  # A tk.DrawingArea.
    canvas.draw()

    toolbar = NavigationToolbar2Tk(canvas, scatterplot_screen, pack_toolbar=False)
    toolbar.update()

    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

    tkinter.mainloop()