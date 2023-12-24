from tkinter import *
import sqlite3


class BorrowBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Borrow Book")
        self.resizable(False,False)


if __name__ == "__main__":
    root = Tk()
    app = BorrowBook(root)
    root.mainloop()