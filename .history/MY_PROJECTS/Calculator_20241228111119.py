from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700, width = 400, bd = 3, relief = 'groove')

display = Entry(main_body, height = 50, width = 300)

main_body.pack(expand = 1, ipadx = 10, ipady = 10)
display.pack()
root.mainloop()