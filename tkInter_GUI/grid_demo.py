import tkinter
import os

mainWindow = tkinter.Tk()

mainWindow.title("Grid Demo")
mainWindow.geometry("640x480-8-200")
mainWindow["padx"] = 8

label = tkinter.Label(mainWindow, text="TkInter Grid Demo")
label.grid(row=0, column=0, columnspan=3)

mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=3)
mainWindow.columnconfigure(3, weight=3)
mainWindow.columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)

file_list = tkinter.Listbox(mainWindow)
file_list.grid(row=1, column=0, sticky="nsew", rowspan=2)
file_list.config(relief="groove", border=2)

for zone in os.listdir("/Windows/System32"):
    file_list.insert(tkinter.END, zone)

list_scroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=file_list.yview)
list_scroll.grid(row=1, column=1, sticky="nsw", rowspan=2)
file_list["yscrollcommand"] = list_scroll.set

# frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text="File Details")
optionFrame.grid(row=1, column=2, sticky="ne")

rbValue = tkinter.IntVar()
rbValue.set(2)

# Radio Buttons
radio1 = tkinter.Radiobutton(optionFrame, text="Filename", value=1, variable=rbValue)
radio2 = tkinter.Radiobutton(optionFrame, text="Path", value=2, variable=rbValue)
radio3 = tkinter.Radiobutton(optionFrame, text="Timestamp", value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky="w")
radio2.grid(row=1, column=0, sticky="w")
radio3.grid(row=2, column=0, sticky="w")

# Widget to display the results
result_label = tkinter.Label(mainWindow, text="Result")
result_label.grid(row=2, column=2, sticky="nw")
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky="sw")

# Frame for time spinners
time_frame = tkinter.LabelFrame(mainWindow, text="Time")
time_frame.grid(row=3, column=0, sticky="new")
# time spinners
hour_spinner = tkinter.Spinbox(time_frame, width=2, value=tuple(range(0, 24)))
minute_spinner = tkinter.Spinbox(time_frame, width=2, value=tuple(range(0, 60)))
seconds_spinner = tkinter.Spinbox(time_frame, width=2, value=tuple(range(0, 60)))
hour_spinner.grid(row=0, column=0)
tkinter.Label(time_frame, text=": ").grid(row=0, column=1)
minute_spinner.grid(row=0, column=2)
tkinter.Label(time_frame, text=": ").grid(row=0, column=3)
seconds_spinner.grid(row=0, column=4)
time_frame["padx"] = 36

# Date frame
date_frame = tkinter.Frame(mainWindow)
date_frame.grid(row=4, column=0)
# date labels
day_label = tkinter.Label(date_frame, text="Date")
month_label = tkinter.Label(date_frame, text="Month")
year_label = tkinter.Label(date_frame, text="Year")
day_label.grid(row=0, column=0, sticky="w")
month_label.grid(row=0, column=1, sticky="w")
year_label.grid(row=0, column=2, sticky="w")
# date spinners
dayspin = tkinter.Spinbox(date_frame, width=5, from_=1, to=31)
monthspin = tkinter.Spinbox(date_frame, width=5,
                            value=("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"))
yearspin = tkinter.Spinbox(date_frame, width=5, from_=1999, to=2020)
dayspin.grid(row=1, column=0)
monthspin.grid(row=1, column=1)
yearspin.grid(row=1, column=2)

ok_button = tkinter.Button(mainWindow, text="OK")
quit_button = tkinter.Button(mainWindow, text="Cancel", command=mainWindow.quit)
ok_button.grid(row=4, column=3, sticky="e")
quit_button.grid(row=4, column=4, sticky="w")

mainWindow.mainloop()
