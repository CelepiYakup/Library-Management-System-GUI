from tkinter import *
from tkinter import messagebox
import sqlite3
con =sqlite3.connect('LMS.db')
cur=con.cursor()

class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("500x450+200+200")
        self.title("Add a Member")
        self.resizable(False, False)

        self.topFrame = Frame(self, height=150, bg='#ADD8E6')
        self.topFrame.pack(fill=X)

        self.bottomFrame = Frame(self, height=600, bg='#ADD8E6')
        self.bottomFrame.pack(fill=X)

        self.top_image = PhotoImage(file='images/member_50.png')
        top_image_lbl = Label(self.topFrame, image=self.top_image, bg='white', cursor='hand2', relief=SUNKEN)
        top_image_lbl.place(x=50, y=30)
        heading = Label(self.topFrame, text='   Add a Member', font=("Times New Roman", 22, "bold"), fg='#003f8a',
                        bg='#ADD8E6',)
        heading.place(x=200, y=35)

        # Entries for member name
        lbl_name = Label(self.bottomFrame, text='Name:', font=("Times New Roman", 15, "bold"), fg='#003f8a',
                         bg='#ADD8E6')
        lbl_name.place(x=40, y=10)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.place(x=150, y=9)

        # Entries for member surname
        lbl_surname = Label(self.bottomFrame, text='Surname:', font=("Times New Roman", 15, "bold"), fg='#003f8a',
                           bg='#ADD8E6')
        lbl_surname.place(x=40, y=70)
        self.ent_surname = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_surname.place(x=150, y=69)

        # Entries for member phone number
        lbl_phone = Label(self.bottomFrame, text='Phone:', font=("Times New Roman", 15, "bold"), fg='#003f8a',
                           bg='#ADD8E6')
        lbl_phone.place(x=40, y=130)
        self.ent_phone = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_phone.place(x=150, y=129)

       
        button=Button(self.bottomFrame,text='Add Member', command=self.addMember, cursor='hand2')
        button.place(x=260,y=170)

    def addMember(self):
            name = self.ent_name.get()
            surname = self.ent_surname.get()
            phone=self.ent_phone.get()
           

            if(name and surname and phone !=""):
                try:
                    query="INSERT INTO 'members' (member_name,member_surname,member_phone) VALUES(?,?,?)"
                    cur.execute(query,(name,surname,phone))
                    con.commit()
                    messagebox.showinfo("Success","Successfully added to database",icon = 'info')
                
                except:
                    messagebox.showerror("Error","Can't add to database",icon='warning')
            else:
                 messagebox.showerror("Error","Fields can't be empty",icon='warning')