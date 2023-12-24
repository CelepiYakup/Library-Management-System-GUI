from tkinter import *
from tkinter import ttk, Frame, Listbox, Scrollbar, Label

class Tabs(Frame):
    def __init__(self, parent, cur=None):
        super().__init__(parent)
        self.cur = cur
        self.given_id = None
        self.tabs = ttk.Notebook(self, width=900, height=660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='images/books32.png')
        self.tab2_icon = PhotoImage(file='images/member32.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound='left')
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound='left')

        # Listed books tabs
        self.list_books_frame = Frame(self.tab1)
        self.list_books_frame.grid(row=0, column=0, padx=(10, 0), pady=10, sticky='n')
        self.list_books = Listbox(self.list_books_frame, width=50, height=35, bd=5, font=("Times New Roman", 12, "bold"), cursor='hand2',bg='#A9A9A9')
        self.list_books.pack(side='left', fill='both')
        sb = Scrollbar(self.list_books_frame, orient='vertical')
        sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=sb.set)
        sb.pack(side='right', fill='y')

        # List details
        self.list_details_frame = Frame(self.tab1)
        self.list_details_frame.grid(row=0, column=1, padx=(10, 0), pady=10, sticky='nsew')
        self.list_details = Listbox(self.list_details_frame, width=80, height=40, bd=5, font=("Times New Roman", 12, "bold"), cursor='hand2',bg='#A9A9A9')
        self.list_details.pack(side='left', fill='both')

        # Statistic tabs
        self.lbl_book_number = Label(self.tab2, text="1", pady=20, font=("Times New Roman", 12, "bold"))
        self.lbl_book_number.grid(row=0)
        self.lbl_member_number = Label(self.tab2, text="", pady=20, font=("Times New Roman", 12, "bold"))
        self.lbl_member_number.grid(row=1, sticky='w')
        self.lbl_borrowed_book = Label(self.tab2, text="", pady=20, font=("Times New Roman", 12, "bold"))
        self.lbl_borrowed_book.grid(row=2, sticky='w')
