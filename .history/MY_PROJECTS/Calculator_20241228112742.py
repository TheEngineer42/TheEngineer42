from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700, width = 400, bd = 3, relief = 'groove')

display = Entry(main_body)

main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry
display.pack(pady = 30)


root.mainloop()