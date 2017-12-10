from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from GUI.defaultClass import *
from GUI.mainMenuClass import *


class Welcome:
    fasta_filename=''
    excel_filename=''

    def __init__(self):
        self.root = Tk()

        default = Defaults(self.root)
        self.lbl01 = Label(self.root,text="DNA-Toolkit(Beta)",font=('Verdana', 50))
        self.lbl02 = Label(self.root, text="Enter Fasta File Address :", font=('Verdana', 15))
        self.lbl03 = Label(self.root, text="Enter Excel File Address :", font=('Verdana', 15))
        self.lbl01.place(x=450,y=100)
        self.lbl02.place(x=500,y=275)
        self.lbl03.place(x=500,y=300)

        self.entry01 = Entry(self.root,width=30)
        self.entry02 = Entry(self.root, width=30)
        self.entry01.place(x=790,y=282)
        self.entry02.place(x=790, y=306)

        self.btn01 = Button(self.root, text="Browse",height=1,width=5,bg="Gray",font=('Verdana', 8),command=self.browse_fasta)
        self.btn02 = Button(self.root, text="Browse", height=1, width=5, bg="Gray",font=('Verdana', 8), command=self.browse_excel)
        self.btn03 = Button(self.root, text="Next", height=2, width=8, bg="Red",font=('Verdana', 10),command=self.next_page)
        self.btn01.place(x=990,y=281)
        self.btn02.place(x=990, y=301)
        self.btn03.place(x=725, y=450)
        self.root.mainloop()

    def browse_fasta(self):
        self.fasta_filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                       filetypes=(("Fasta Files", "*.fasta"),("All Files", "*.*")))
        print(self.fasta_filename)
        #messagebox.showinfo("ACTION","Loading Completed")

    def browse_excel(self):

        self.excel_filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                       filetypes=(("Excel Files", "*.xlsx"),("All Files", "*.*")))
        print(self.excel_filename)
        #messagebox.showinfo("ACTION","Loading Completed")

    def next_page(self):
        new_root=Tk()
        self.root.destroy()
        #master.destroy()
        menu_base1 = MainMenu(new_root)
        new_root.mainloop()

    # def next_page_id(self):
    #     self.next_page(self.root)


