import tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 1), ('/', 1)],
        ]

mainWindowPadding = 8

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())

mainWindow.mainloop()
# base_widow = tkinter.Tk()
# base_widow.title("Calculator")
# base_widow.geometry("250x400")
#
# entry = tkinter.Entry(base_widow)
# entry.grid(row=0, column=0, sticky="nsew")
#
# base_widow.columnconfigure(0, weight=1)
# base_widow.columnconfigure(1, weight=1)
# base_widow.columnconfigure(2, weight=1)
# base_widow.columnconfigure(3, weight=1)
# base_widow.columnconfigure(4, weight=10)
# base_widow.rowconfigure(0, weight=1)
# base_widow.rowconfigure(1, weight=1)
# base_widow.rowconfigure(2, weight=1)
# base_widow.rowconfigure(3, weight=1)
# base_widow.rowconfigure(4, weight=1)
# base_widow.rowconfigure(5, weight=1)
#
# # list1 = ["C", "CE", "7", "4", "1", "0"]
#
# tkinter.Button(base_widow, text="C").grid(row=1, column=0, sticky="e")
# tkinter.Button(base_widow, text="7").grid(row=2, column=0, sticky="e")
# tkinter.Button(base_widow, text="4").grid(row=3, column=0, sticky="e")
# tkinter.Button(base_widow, text="1").grid(row=4, column=0, sticky="e")
# tkinter.Button(base_widow, text="0").grid(row=5, column=0, sticky="e")
# tkinter.Button(base_widow, text="CE").grid(row=1, column=1, sticky="nw")
# tkinter.Button(base_widow, text="8").grid(row=2, column=1, sticky="nw")
# tkinter.Button(base_widow, text="5").grid(row=3, column=1, sticky="nw")
# tkinter.Button(base_widow, text="2").grid(row=4, column=1, sticky="nw")
# tkinter.Button(base_widow, text="=").grid(row=5, column=1, sticky="nsew", rowspan=2)
# tkinter.Button(base_widow, text="9").grid(row=2, column=2, sticky="w")
# tkinter.Button(base_widow, text="6").grid(row=3, column=2, sticky="w")
# tkinter.Button(base_widow, text="3").grid(row=4, column=2, sticky="w")
# tkinter.Button(base_widow, text="+").grid(row=2, column=3, sticky="e")
# tkinter.Button(base_widow, text="-").grid(row=3, column=3, sticky="e")
# tkinter.Button(base_widow, text="*").grid(row=4, column=3, sticky="e")
# tkinter.Button(base_widow, text="/").grid(row=5, column=3, sticky="e")
#
# base_widow.mainloop()
