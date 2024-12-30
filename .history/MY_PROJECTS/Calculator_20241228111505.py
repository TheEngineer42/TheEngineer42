from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700, width = 400, bd = 3, relief = 'groove')

display = Entry(main_body)

main_body.pack(ipadx = 10, ipady = 10)
display.pack_propagate(False)
display.pack()


root.mainloop()