from tkinter import *
from tkinter import messagebox
import sqlite3
con =sqlite3.connect('LMS.db')
cur=con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Add book")
        self.resizable(False, False)

        self.topFrame = Frame(self, height=150, bg='white')
        self.topFrame.pack(fill=X)

        self.bottomFrame = Frame(self, height=600, bg='#fcc324')
        self.bottomFrame.pack(fill=X)

        self.top_image = PhotoImage(file='images/add_book50.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white', cursor='hand2', relief=SUNKEN)
        top_image_lbl.place(x=50, y=30)
        heading = Label(self.topFrame, text='   Add a Book', font=("Times New Roman", 22, "bold"), fg='#003f8a',
                        bg='white',)
        heading.place(x=200, y=35)

        # Entries for book name
        lbl_name = Label(self.bottomFrame, text='Name:', font=("Times New Roman", 15, "bold"), fg='black',
                         bg='#fcc324')
        lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, 'Enter a book name')
        self.ent_name.place(x=150, y=45)

        # Entries for Author
        lbl_author = Label(self.bottomFrame, text='Author:', font=("Times New Roman", 15, "bold"), fg='black',
                           bg='#fcc324')
        lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_author.insert(0, 'Enter an Author')
        self.ent_author.place(x=150, y=85)

         # Entries for book page
        lbl_page = Label(self.bottomFrame, text='Page:', font=("Times New Roman", 15, "bold"), fg='black',
                         bg='#fcc324')
        lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_page.insert(0, 'Enter a book page')
        self.ent_page.place(x=150, y=125)

        button=Button(self.bottomFrame,text='Add Book', command=self.addBook, cursor='hand2')
        button.place(x=278,y=160)

    def addBook(self):
            name = self.ent_name.get()
            author=self.ent_author.get()
            page= self.ent_page.get()


            if(name and author and page !=""):
                try:
                    query="INSERT INTO 'books' (book_name,book_author,book_page) VALUES(?,?,?)"
                    cur.execute(query,(name,author,page))
                    con.commit()
                    messagebox.showinfo("Success","Successfully added to database",icon = 'info')
                
                except:
                    messagebox.showerror("Error","Can't add to database",icon='warning')
            else:
                 messagebox.showerror("Error","Fields can't be empty",icon='warning')