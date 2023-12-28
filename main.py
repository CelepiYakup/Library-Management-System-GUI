from tkinter import *
from tkinter import messagebox
from tabs import Tabs
import addBook, addMember,BorrowBook
import sqlite3
from BorrowBookWindow import BorrowBook

# connection from sqlite3 db
con = sqlite3.connect('LMS.db')
cur = con.cursor()

class Main(object):
    def __init__(self, master):
        self.master = master

        master.title("Library Management System")

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate X and Y offsets for center position main window
        x_offset = (screen_width - 1440) // 2
        y_offset = (screen_height - 850) // 2
        master.geometry(f"1355x790+{x_offset}+{y_offset}")

        # Main frame creation
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Bottom frame creation
        bottomFrame = Frame(mainFrame, width=1440, height=150, bg='orange2', relief=SUNKEN, padx=20, borderwidth=2)
        bottomFrame.pack(side=BOTTOM, fill=X)

        # Top frame creation
        topFrame = Frame(mainFrame, width=1440, height=150, bg='#A9A9A9', relief=RIDGE, padx=5, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        # Center frame creation
        centerFrame = Frame(mainFrame, width=1440, bg='#FFFFFF', relief=RIDGE, height=700)
        centerFrame.pack(side=TOP)

        # Creating center left and right frames creation
        centerLeft = Frame(centerFrame, width=1000, height=700, bg='#A9A9A9', relief=SUNKEN, borderwidth=2)
        centerLeft.pack(side=LEFT)

        centerRight = Frame(centerFrame, width=440, height=700, bg='#FFFFFF', relief=SUNKEN, borderwidth=2)
        centerRight.pack()

        # Bottom created by us
        social_links = [
            ("Github by Yakup Celepi", "https://github.com/CelepiYakup"),
            ("Github by Yağmur Çelik", "https://github.com/your_username")
        ]

        for social, link in social_links:
            label = Label(bottomFrame, text=social, fg='blue', cursor='hand2', font=("Times New Roman", 12, "bold"))
            label.bind("<Button-1>", lambda event, url=link: self.open_url(url))
            label.pack(side=LEFT, padx=10)

    
        # Search bar creation
        search_bar = LabelFrame(centerRight, width=450, height=250, text='Search to book', bg='#9bc9ff',
                                font=("Times New Roman", 12, "bold"))
        search_bar.pack(fill=BOTH)

        # Search bar Label
        self.lbl_search = Label(search_bar,
                                relief=FLAT,
                                text='Search: ',
                                font=("Times New Roman", 12, "bold"),
                                bg='#9bc9ff',
                                fg='white',
                                border=5)
        self.lbl_search.grid(row=0, column=0, padx=20, pady=10)
        # Entry Search box
        self.ent_search = Entry(search_bar,
                                font=("Times New Roman", 12, "bold"),
                                fg="#000000",
                                width=25,
                                bd=10)

        self.ent_search.grid(
            row=0,
            column=1,
            columnspan=3,
            padx=5,
            pady=5)

        self.btn_search = Button(search_bar, text='Search', font=("Times New Roman", 12, "bold"), bg='#fcc324',
                                 fg="white", cursor='hand2', command=self.searchBooks)
        self.btn_search.grid(row=0, column=4, padx=5, pady=10)

        # List creation
        list_bar = LabelFrame(centerRight, 
                              width=450, 
                              height=250, 
                              text='List Box', 
                              bg='#fcc324',
                              font=("Times New Roman", 12, "bold"))
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar, text='Sort By', font=("Times New Roman", 16, "bold"), fg='white', bg='#fcc324')
        lbl_list.grid(row=0, column=2)
        self.listChoice = IntVar()
        rb1 = Radiobutton(list_bar, text='All Books', var=self.listChoice, value=1, bg='#fcc324')
        rb2 = Radiobutton(list_bar, text='In Library', var=self.listChoice, value=2, bg='#fcc324')
        rb3 = Radiobutton(list_bar, text='Borrowed Books', var=self.listChoice, value=3, bg='#fcc324')
        rb1.grid(row=1, column=0)
        rb2.grid(row=1, column=1)
        rb3.grid(row=1, column=2)
        btn_list = Button(list_bar, text='List Books', bg='#2488ff', fg='white',
                          font=("Times New Roman", 12, "bold"), command=self.listBooks, cursor='hand2')
        btn_list.grid(row=1, column=3, padx=20, pady=5)

        bar_img = Frame(centerRight, width=450, height=250)
        bar_img.pack(fill=BOTH)

        #Title and img from tabs.py

        self.title_right = Label(bar_img, text='SEN4017 LIBRARY MANAGEMENT SYSTEM',fg='orange',
                                 font=("Times New Roman", 16, "bold"))
        self.title_right.grid(row=0)
        self.library_image = PhotoImage(file='images/LibraryimgBau.png')
        self.lblImg = Label(bar_img, image=self.library_image)
        self.lblImg.grid(row=1)

        # Book button and image
        self.iconbook = PhotoImage(file='images/add_book50.png')
        self.btnbook = Button(topFrame, text='Add a book', image=self.iconbook, compound=LEFT,
                              command=self.addBook,
                              highlightthickness=0,
                              highlightbackground='#212121',
                              highlightcolor='blue',
                              border=0,
                              cursor='hand2', font=("Times New Roman", 12))
        self.btnbook.pack(side=LEFT, padx=5)

        # Member button and image
        self.iconmember = PhotoImage(file='images/member_50.png')
        self.btnmember = Button(topFrame, text='Add a member', image=self.iconmember, compound=LEFT,
                                command=self.addMember,
                                highlightthickness=0,
                                highlightbackground='#212121',
                                highlightcolor='blue',
                                border=0,
                                cursor='hand2', font=("Times New Roman", 12, "bold"))
        self.btnmember.pack(side=LEFT, padx=5)

        # Borrow book
        self.iconborrow = PhotoImage(file='images/borrow_50.png')
        self.btnborrow = Button(topFrame, text='Borrow a book', image=self.iconborrow, command=self.BorrowAbook,
                                compound=LEFT,
                                highlightthickness=0,
                                highlightbackground='#212121',
                                highlightcolor='blue',
                                border=0,
                                cursor='hand2', font=("Times New Roman", 12, "bold"))
        self.btnborrow.pack(side=LEFT, padx=5)

        # Creating an instance of the Tabs class
        self.tabs_frame = Tabs(centerLeft, cur)
        self.tabs_frame.pack(side=LEFT)


        # Functions
        
        self.displayBooks()
        self.Statistic()
        

    def Statistic(self ,evt=None):
        book_counter=cur.execute("SELECT count (books_id) FROM books").fetchall()
        member_counter=cur.execute("SELECT count (members_id) FROM members").fetchall()
        borrowed_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status =1").fetchall()
        print(book_counter)
    
        self.tabs_frame.lbl_book_number.config(text='Totally : ' + str(book_counter[0][0]) + ' books in library')
        self.tabs_frame.lbl_member_number.config(text='Total of the member : ' + str(member_counter[0][0]))
        self.tabs_frame.lbl_borrowed_book.config(text='Total Borrowed books : ' + str(borrowed_books[0][0]))
        self.displayBooks()

        

    def addBook(self):
        add = addBook.AddBook()
        

    def addMember(self):
        member = addMember.AddMember()


        
    def displayBooks(self):
        books = cur.execute("SELECT * FROM books").fetchall()
        count = 0

        self.tabs_frame.list_books.delete(0,END)

        for book in books:
            print(book)
            self.tabs_frame.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1

        def bookInfo(evt):
            selected_books = self.tabs_frame.list_books.curselection()
            book_info = []  # Initialize with an empty list

            if selected_books:
                value = str(self.tabs_frame.list_books.get(selected_books))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE books_id=?", (id,))
                book_info = book.fetchall()
                print(book_info)

            # Deploy the list details on tabs.py
            list_details = self.tabs_frame.list_details
            list_details.delete(0, 'end')

            if book_info:
                list_details.insert(0, "Book Name : " + book_info[0][1])
                list_details.insert(1, "Page : " + str(book_info[0][2]))
                list_details.insert(2, "Author Name : " + book_info[0][3])

                if book_info[0][4] == 0:
                    list_details.insert(4, "Status : Available")
                else:
                    list_details.insert(4, "Status : Not Available")




        self.tabs_frame.list_books.bind('<<ListboxSelect>>', bookInfo)
        self.tabs_frame.tabs.bind('<<NotebookTabChanged>>', self.Statistic)
        self.tabs_frame.list_books.bind('<Double-Button-1>',self.doubleClick)

        #Borrow book function

    def doubleClick(self, evt):
        value = str(self.tabs_frame.list_books.get(self.tabs_frame.list_books.curselection()))
        given_id = value.split('-')[0]
        give_book = BorrowBook(self.master, con, cur, given_id)

        #searching book function

    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ? ", ('%'+value+'%',)).fetchall()
        print(search)
        self.tabs_frame.list_books.delete(0, END)

        count = 0
        for book in search:
           
            self.tabs_frame.list_books.insert(count, str(book[0]) + "-" + book[1])
            count += 1
    #Listing  sort function  
    def listBooks(self):
        value = self.listChoice.get()
        if value == 1:
            allbooks= cur.execute("SELECT * FROM books").fetchall()
            print(allbooks)
            self.tabs_frame.list_books.delete(0,END)

            count=0
            for book in allbooks:
                self.tabs_frame.list_books.insert(count, str(book[0]) + "-" + book[1])
                count +=1
        
        elif value == 2:
            in_library_books = cur.execute("SELECT * FROM books WHERE book_status = ?", (0,)).fetchall()
            self.tabs_frame.list_books.delete(0,END)
            print(in_library_books)
            count = 0
            for book in in_library_books:
                self.tabs_frame.list_books.insert(count,str(book[0]) + "-" + book[1])
                count += 1
        else:
            borrowed_books= cur.execute("SELECT * FROM books WHERE book_status = ?", (1,)).fetchall()
            print(borrowed_books)
            self.tabs_frame.list_books.delete(0,END)

            count = 0
            for book in borrowed_books:
                self.tabs_frame.list_books.insert(count, str(book[0]) + "-" + book[1])
                count += 1
            
        #Add a webbrowser url for social media contact
    

    def BorrowAbook(self):
        selected_books = self.tabs_frame.list_books.curselection()

        if selected_books:
           value = str(self.tabs_frame.list_books.get(selected_books))
           given_id = value.split('-')[0]
           give_book = BorrowBook(self.master, con, cur, given_id)
        else:
           messagebox.showwarning("Warning", "Please select a book to borrow.")



    def open_url(self, url):
        import webbrowser
        webbrowser.open(url)


if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()