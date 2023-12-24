from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from tabs import Tabs

class BorrowBook(Toplevel):
    def __init__(self, master, con, cur, book_id):
        Toplevel.__init__(self, master)
        self.master = master
        self.con = con
        self.cur = cur
        self.book_id = int(book_id)
        self.geometry("650x750+550+200")
        self.title("Borrow Book")
        self.resizable(False, False)
        self.setup_ui()

    def setup_ui(self):
        query = "SELECT * FROM books WHERE book_status=0"
        books = self.cur.execute(query).fetchall()
        books_list = [f"{book[0]}-{book[1]}" for book in books]

        query2 = "SELECT * FROM members"
        members = self.cur.execute(query2).fetchall()
        member_list = [f"{member[0]}-{member[1]}" for member in members]

        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill='x')

        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill='x')

        self.top_image = PhotoImage(file='images/member_50.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white', cursor='hand2', relief='sunken')
        top_image_lbl.place(x=50, y=30)
        heading = Label(self.topFrame, text='   Borrow A Book', font=("Times New Roman", 22, "bold"), fg='#003f8a',
                        bg='white',)
        heading.place(x=200, y=35)

        # Entries for book name
        self.book_name = StringVar()
        lbl_name = Label(self.bottomFrame, text='Book Name:', font=("Times New Roman", 15, "bold"), fg='black',
                         bg='#fcc324')
        lbl_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottomFrame, textvariable=self.book_name)
        self.combo_name['values'] = books_list
        self.combo_name.place(x=180, y=45)

        # Entries for member name
        self.member_name = StringVar()
        lbl_surname = Label(self.bottomFrame, text='Member Name:', font=("Times New Roman", 15, "bold"), fg='black',
                            bg='#fcc324')
        lbl_surname.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottomFrame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=180, y=85)

        button = Button(self.bottomFrame, text='Borrow Book', command=self.borrow_book_action, cursor='hand2')
        button.place(x=242, y=110)

    def borrow_book_action(self):
        book_name = self.book_name.get()
        self.book_id = book_name.split('-')[0]
        member_name = self.member_name.get()

        if book_name and member_name:
            try:
                query = "INSERT INTO 'borrows' (bbook_id, bmember_id) VALUES (?, ?)"
                self.cur.execute(query, (self.book_id, member_name))
                self.con.commit()
                messagebox.showinfo("Success", "Successfully added", icon='info')
                self.cur.execute("UPDATE books SET book_status = ? WHERE books_id = ?", (1, self.book_id))
                self.con.commit()
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}", icon='warning')
        else:
            messagebox.showerror("Error", "Fields must be filled", icon='warning')
