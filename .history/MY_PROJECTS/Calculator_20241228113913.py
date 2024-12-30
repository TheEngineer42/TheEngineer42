from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700,   #main body
                  width = 400, bd = 3, relief = 'groove')

display = Entry(main_body, font = 'Calibri 25')           #display

b7 = Button(main_body, height = 5, width = 9, text = '7')
b8 = Button(main_body, height = 5, width = 9, text = '8')
b9 = Button(main_body, height = 5, width = 9, text = '9')
b_plus = Button(main_body, height = 5, width = 9, text = '+')





main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry
display.pack(pady = 40)

b7.pack(padx = 10, pady = 10)
b8.pack()
b9.pack()
b_plus.pack()
root.mainloop()