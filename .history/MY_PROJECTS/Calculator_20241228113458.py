from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700,   #main body
                  width = 400, bd = 3, relief = 'groove')

display = Entry(main_body, font = 'Calibri 25')           #display

b7 = Button(main_body, text = '7')






main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry
display.pack(pady = 40)

b7.pack()
root.mainloop()