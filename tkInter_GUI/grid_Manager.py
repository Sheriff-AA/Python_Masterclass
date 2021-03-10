import tkinter

mainWindow = tkinter.Tk()

mainWindow.title("New Window")
mainWindow.geometry("700x500-80-200")

label = tkinter.Label(mainWindow, text="Experiment")
label.grid(row=0, column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1, column=1)

canvas = tkinter.Canvas(leftFrame, relief="raised", borderwidth=1)
canvas.grid(row=0, column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1, column=2)

button1 = tkinter.Button(rightFrame, text="Button1")
button2 = tkinter.Button(rightFrame, text="Button2")
button3 = tkinter.Button(rightFrame, text="Button3")
button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)

# configure the columns
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=1)

rightFrame.config(relief="sunken", borderwidth=1)
leftFrame.config(relief="sunken", borderwidth=1)
leftFrame.grid(sticky="ns")
rightFrame.grid(sticky="new")

rightFrame.columnconfigure(0, weight=1)
button2.grid(sticky="ew")

mainWindow.mainloop()
