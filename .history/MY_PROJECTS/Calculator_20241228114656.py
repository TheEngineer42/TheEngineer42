from tkinter import*
root = Tk()
root.geometry('800x800')

main_body = Frame(root, bg = 'gainsboro', height = 700,   #main body
                  width = 400, bd = 3, relief = 'groove')

frame1 = Frame(main_body, bg = 'gainsboro') #for 7,8,9,+
frame2 = Frame(main_body, bg = 'gainsboro') #for 4,5,6,-
frame3 = Frame(main_body, bg = 'gainsboro') #for 1,2,3,x
frame4 = Frame(main_body, bg = 'gainsboro') #for  ,0,=,/

display = Entry(main_body, font = 'Calibri 25')           #display


b7 = Button(frame1, height = 5, width = 9, text = '7')
b8 = Button(frame2, height = 5, width = 9, text = '8')
b9 = Button(frame3, height = 5, width = 9, text = '9')
b_plus = Button(frame4, height = 5, width = 9, text = '+')





main_body.pack(expand = 1)
main_body.pack_propagate(False) #because of pack(), your Frame will shrink to the size of entry

display.pack(pady = 40)

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

b7.pack(padx = 10, pady = 10)
b8.pack(padx = 10, pady = 10)
b9.pack(padx = 10, pady = 10)
b_plus.pack(padx = 10, pady = 10)

root.mainloop()