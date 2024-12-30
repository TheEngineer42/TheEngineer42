from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700,   #main body
                  width = 400, bd = 3, relief = 'groove')

frame1 = Frame(main_body, bg = 'blue')

display = Entry(main_body, font = 'Calibri 25')           #display







main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry
display.pack(pady = 40)


root.mainloop()