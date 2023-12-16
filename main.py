from tkinter import *

class Main(object):
    def __init__(self, master):
        self.master = master
        master.title("Library Management System")
        master.geometry("1440x850+250+200")

        #Main frames can be proceeded
        mainFrame = Frame(self.master)
        mainFrame.pack()

        # Top frame
        topFrame = Frame(mainFrame, width=1440, height=90, bg='orange2', relief=SUNKEN, padx=20, borderwidth=2)
        topFrame.pack(side=BOTTOM, fill=X)

        #center frame
        centerFrame =Frame(mainFrame, width=1440,bg='#000000', relief=RIDGE, height=700)
        centerFrame.pack(side=TOP)



if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()
