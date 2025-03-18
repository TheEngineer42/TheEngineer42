from tkinter import*

root = Tk()

def exit_win(event):
    root.destroy()


def to_label(event):
    t = ent.get()
    lbl.configure(text=t)

def select_all(event):
    def select_all2(widget):
        widget.
