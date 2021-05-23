import tkinter

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.axis as axis
import numpy as np

from globals import get_metadata

def generate_scatterplot_matrix(file):
    
    # Clear plot
    plt.close("all")

    root = tkinter.Tk()
    root.wm_title = "ScatterplotMatrix"

    meta = get_metadata()

    # Metadata not gathered? - show alert and return
    if meta == None:
        root.destroy()
        show_method = getattr(tkinter.messagebox, 'show{}'.format("warning"))
        show_method("Error", "Dataset not selected.")       
        return

    # Skip type and meta rows in datasets based on file extension
    rowsSkipped = 1    
    if meta.delimiter == '\t':
        rowsSkipped = 3

    data = open(file).readlines()

    # Create an array with only the relevant data
    numericColumnData = meta.get_numeric_columns()
    
    usedColumnCount = numericColumnData[0]
    usedColumns = []
    usedColumnIds = numericColumnData[2]
    for i in range(usedColumnCount):
        usedColumns.append([])
    for i, line in enumerate(data):
        if i <= rowsSkipped:
            continue
        splitLine = line.split(meta.delimiter)
        columnId = 0
        for id, cell in enumerate(splitLine):
            if id in usedColumnIds:
                val = 0
                try:
                    val = float(cell)
                except:
                    val = 0
                
                usedColumns[columnId].append(val)
                columnId += 1

    # Not enough numeric columns - show alert and return
    if usedColumnCount < 1:
        root.destroy()
        show_method = getattr(tkinter.messagebox, 'show{}'.format("warning"))
        show_method("Error", "Not enough numeric types in dataset.")       
        return


    ''' 
        Display scatterplots like a times table
    '''

    # Showing more graphs = less clarity, so let's cap it at 10x10
    if(usedColumnCount > 10):
        usedColumnCount = 10

    fig, axs = plt.subplots(usedColumnCount, usedColumnCount, figsize=(5, 5))
    t = np.arange(-50, 500, .05)

    for c1 in range(0, usedColumnCount):

        axs[c1, 0].set_ylabel( meta.columns[ usedColumnIds[ c1 ] ] )

        for c2 in range(0, usedColumnCount):
            if c1 == usedColumnCount-1:
                axs[c1, c2].set_xlabel( meta.columns[ usedColumnIds[ c2 ] ] )

            # Replace scatterplot with histogram if x and y axis use the same column
            if c1 == c2:                
                axs[c1, c2].hist(usedColumns[c1])
                continue

            axs[c1, c2].scatter(usedColumns[c1], usedColumns[c2])
            
            
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    toolbar = NavigationToolbar2Tk(canvas, root, pack_toolbar=False)
    toolbar.update()

    toolbar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
    tkinter.mainloop()
