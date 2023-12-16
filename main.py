from tkinter import *
from tabs import Tabs
import addBook
import sqlite3

#connection from sqlite3 db

con = sqlite3.connect('LMS.db')
cur = con.cursor()

class Main(object):
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate X and Y offsets for center position
        x_offset = (screen_width - 1440) // 2
        y_offset = (screen_height - 850) // 2
        master.geometry(f"1440x850+{x_offset}+{y_offset}")

        # Main frame
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Bottom frame
        bottomFrame = Frame(mainFrame, width=1440, height=150, bg='orange2', relief=SUNKEN, padx=20, borderwidth=2)
        bottomFrame.pack(side=BOTTOM, fill=X)

        # Top frame
        topFrame = Frame(mainFrame, width=1440, height=150, bg='#FA2521', relief=RIDGE, padx=20, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        # Center frame
        centerFrame = Frame(mainFrame, width=1440, bg='#FFFFFF', relief=RIDGE, height=700)
        centerFrame.pack(side=TOP)

        # Creating center left and right frames
        centerLeft = Frame(centerFrame, width=1000, height=700, bg='#212121', relief=SUNKEN, borderwidth=2)
        centerLeft.pack(side=LEFT)

        centerRight = Frame(centerFrame, width=440, height=700, bg='#FFFFFF', relief=SUNKEN, borderwidth=2)
        centerRight.pack()
        #Bottom created by us

        social_links = [
            ("Github by Yakup Celepi", "https://github.com/CelepiYakup"),
            ("Github by Yağmur Çelik", "https://github.com/your_username")
            
            
        ]

        for social, link in social_links:
            label = Label(bottomFrame, text=social, fg='blue', cursor='hand2', font=("Times New Roman", 12, "bold"))
            label.bind("<Button-1>", lambda event, url=link: self.open_url(url))
            label.pack(side=LEFT, padx=10)

            def open_url(self, url):
                import webbrowser
                webbrowser.open(url)
            
            self.social_img=PhotoImage(file='images/github_50.png')


        #search bar creation 

        search_bar = LabelFrame(centerRight, width=450, height=250, text='Search to book', bg='#9bc9ff', font=("Times New Roman", 12,"bold"))
        search_bar.pack(fill=BOTH)

        #Search bar Label
        self.lbl_search=Label(search_bar,
                            relief=FLAT,
                            text='Search: ',
                            font=("Times New Roman", 12, "bold"),
                            bg='#9bc9ff',
                            fg='white',
                            border=5)
        self.lbl_search.grid(row=0,column=0,padx= 20, pady=10)
        #Entry Search box
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
        
        self.btn_search=Button(search_bar,text= 'Search',font=("Times New Roman",12,"bold"), bg='#fcc324',fg="white",cursor='hand2')
        self.btn_search.grid(row=0,column=4,padx=5,pady=10)
        

        #List creation 
        list_bar = LabelFrame(centerRight, width=450, height=250, text='List Box', bg='#fcc324', font=("Times New Roman", 12,"bold"))
        list_bar.pack(fill=BOTH)
        lbl_list=Label(list_bar,text='Short By', font=("Times New Roman", 16,"bold"), fg='white',bg='#fcc324')
        lbl_list.grid(row=0,column=2)
        self.listChoice=IntVar()
        rb1=Radiobutton(list_bar,text='All Books',var=self.listChoice,value=1,bg='#fcc324')
        rb2=Radiobutton(list_bar,text='In Library',var=self.listChoice,value=2,bg='#fcc324')
        rb3=Radiobutton(list_bar,text='Borrowed Books',var=self.listChoice,value=3,bg='#fcc324')
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)
        btn_list=Button(list_bar,text='List Books', bg='#2488ff', fg='white', font=("Times New Roman", 12 ,"bold"),cursor='hand2')
        btn_list.grid(row=1,column=3,padx=20,pady=5)


        bar_img=Frame(centerRight, width=450,height=250)
        bar_img.pack(fill=BOTH)
        self.title_right=Label(bar_img, text='SEN4017 LIBRARY MANAGMENT SYSTEM',font=("Times New Roman", 16, "bold"))
        self.title_right.grid(row=0)
        self.library_image=PhotoImage(file='images/LibraryimgBau.png')
        self.lblImg=Label(bar_img,image=self.library_image)
        self.lblImg.grid(row=1)


        #book button and image 
        self.iconbook=PhotoImage(file='images/add_book50.png')
        self.btnbook= Button(topFrame,text='Add a book', image=self.iconbook,compound=LEFT,
                             command=self.addBook,
                             highlightthickness=0,
                             highlightbackground='#212121',
                             highlightcolor='blue',
                             border=0,
                             cursor='hand2',font=("Times New Roman", 12))
        self.btnbook.pack(side=LEFT,padx=5)

        #member button and image

        self.iconmember=PhotoImage(file='images/member_50.png')
        self.btnmember=Button(topFrame,text='Add a member', image=self.iconmember,compound=LEFT,
                             command=self.addBook,
                             highlightthickness=0,
                             highlightbackground='#212121',
                             highlightcolor='blue',
                             border=0,
                             cursor='hand2',font=("Times New Roman", 12,"bold"))
        self.btnmember.pack(side=LEFT,padx=5)

       
        #borrow book 

        
        self.iconborrow=PhotoImage(file='images/borrow_50.png')
        self.btnborrow=Button(topFrame,text='Borrow a book', image=self.iconborrow,compound=LEFT,
                              highlightthickness=0,
                             highlightbackground='#212121',
                             highlightcolor='blue',
                             border=0,
                             cursor='hand2', font=("Times New Roman", 12,"bold"))
        self.btnborrow.pack(side=LEFT,padx=5)

        
        # Creating an instance of the Tabs class
        self.tabs_frame = Tabs(centerLeft)
        self.tabs_frame.pack(side=LEFT)

    def addBook(self):
        add = addBook.AddBook()

if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()
