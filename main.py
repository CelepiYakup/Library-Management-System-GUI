from tkinter import *

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
        topFrame = Frame(mainFrame, width=1440, height=150, bg='red', relief=RAISED, padx=20, borderwidth=2)
        topFrame.pack(side=TOP, fill=X)

        # Center frame
        centerFrame = Frame(mainFrame, width=1440, bg='#000000', relief=RIDGE, height=700)
        centerFrame.pack(side=TOP)

        # Creating center left and right frames
        centerLeft = Frame(centerFrame, width=1008, height=700, bg='#212121', relief=SUNKEN, borderwidth=2)
        centerLeft.pack(side=LEFT)

        centerRight = Frame(centerFrame, width=432, height=700, bg='#313131', relief=SUNKEN, borderwidth=2)
        centerRight.pack(side=RIGHT)

if __name__ == "__main__":
    root = Tk()
    app = Main(root)
    root.mainloop()
