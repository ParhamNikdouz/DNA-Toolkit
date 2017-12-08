from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import sys


class Defaults:
    def __init__(self,master):
        # fix the window
        #w = 800
        #h = 650
        #ws = master.winfo_screenwidth()
        #hs = master.winfo_screenheight()
        #x = (ws / 2) - (w / 2)
        #y = (hs / 2) - (h / 2)
        #master.geometry('%dx%d+%d+%d' % (w,h,x,y))
        master.wm_state('zoomed')
        master.resizable(width=False, height=False)
        master.title('DNA-Toolkit (Beta)')


class MainMenu:

    def __init__(self,master):
        # create an object from motif class ...
        default = Defaults(master)
        master.configure(background='gray')

        self.menubar = Menu(master)

        self.filemenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New Window",command=self.new_window)
        self.filemenu.add_command(label="Restart Program",command=self.restart_program)


        #self.filemenu.add_separator()

        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.ask_quit)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit")
        self.editmenu.add_command(label="Undo")
        self.editmenu.add_command(label="Redo")

        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.viewmenu.add_command(label="Normal Size", command=self.normalscreen_id)
        self.viewmenu.add_command(label="Full Screen", command=self.fullscreen_id)

        self.runmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Run", menu=self.runmenu)
        self.runmenu.add_command(label="Motif Count")
        self.submenu = Menu(self.runmenu, tearoff=0)
        self.runmenu.add_cascade(label="Clustering", menu=self.submenu)
        self.d2menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="2D", menu=self.d2menu)
        self.d3menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="3D", menu=self.d3menu)
        self.d2menu.add_command(label="K-Means Clustering")
        self.d2menu.add_command(label="Mini-Batch K-Means")
        self.d2menu.add_command(label="Agglomerative Clustering")
        self.d2menu.add_command(label="Spectral Clustering")
        self.d2menu.add_command(label="Birch")
        self.d2menu.add_command(label="Fuzzy-CMeans")
        self.d2menu.add_command(label="Mixture Gaussian")
        self.d2menu.add_command(label="Affinity Propagation")
        self.d2menu.add_command(label="Mean-Shift")

        self.d3menu.add_command(label="K-Means Clustering")
        self.d3menu.add_command(label="Mini-Batch K-Means")
        self.d3menu.add_command(label="Agglomerative Clustering")
        self.d3menu.add_command(label="Spectral Clustering")
        self.d3menu.add_command(label="Birch")
        self.d3menu.add_command(label="Fuzzy-CMeans")
        self.d3menu.add_command(label="Affinity Propagation")
        self.d3menu.add_command(label="Mean-Shift")

        self.toolsmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Tools", menu=self.toolsmenu)
        self.toolsmenu.add_command(label="Take A Note", command=self.take_a_note)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="How To Use?")
        self.helpmenu.add_command(label="About Fasta File")
        self.helpmenu.add_command(label="About Us")

        master.config(menu=self.menubar)

    def do_nothing(self):
        print("Ok, Ok, I Won't !")

    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def ask_quit(self,master):
        if messagebox.askokcancel("EXIT", "Are You Sure?"):
            master.quit()

    def fullscreen(self,master):
        master.attributes('-fullscreen', True)

    def normalscreen(selfs,master):
        master.attributes('-fullscreen', False)

    # destroying the master, so fullscreen must be on root1 , . . .
    def fullscreen_id(self):
        self.fullscreen(self.root1)

    def normalscreen_id(self):
        self.normalscreen(self.root1)

    def new_window(self):
        self.root2 = Tk()
        menu_base2 = MainMenu(self.root2)
        self.root2.mainloop()
    def take_a_note(self):
        fw = open('take_a_note.txt','w')
        fw.close()
        fr = open('take_a_note.txt','r')
        taken_note = fr.read()


class Welcome:

    def __init__(self,master):

        default = Defaults(master)
        self.lbl01 = Label(master,text="DNA-Toolkit(Beta)",font=('Verdana', 50))
        self.lbl02 = Label(master, text="Enter Fasta File Address :", font=('Verdana', 15))
        self.lbl03 = Label(master, text="Enter Excel File Address :", font=('Verdana', 15))
        self.lbl01.place(x=450,y=100)
        self.lbl02.place(x=500,y=275)
        self.lbl03.place(x=500,y=300)

        self.entry01 = Entry(master,width=30)
        self.entry02 = Entry(master, width=30)
        self.entry01.place(x=790,y=282)
        self.entry02.place(x=790, y=306)

        self.btn01 = Button(master, text="Browse",height=1,width=5,bg="Gray",font=('Verdana', 8),command=self.browse_fasta_id)
        self.btn02 = Button(master, text="Browse", height=1, width=5, bg="Gray",font=('Verdana', 8), command=self.browse_excel_id)
        self.btn03 = Button(master, text="Next", height=2, width=8, bg="Red",font=('Verdana', 10),command=self.next_page_id)
        self.btn01.place(x=990,y=281)
        self.btn02.place(x=990, y=301)
        self.btn03.place(x=725, y=450)

    def browse_fasta(self,master):
        master.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                       filetypes=(("Fasta Files", "*.fasta"),("All Files", "*.*")))
        print(master.filename)
        messagebox.showinfo("ACTION","Loading Completed")

    def browse_excel(self,master):
        master.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                       filetypes=(("Excel Files", "*.xlsx"),("All Files", "*.*")))
        print(master.filename)
        messagebox.showinfo("ACTION","Loading Completed")

    def browse_fasta_id(self):
        self.browse_fasta(root)

    def browse_excel_id(self):
        self.browse_excel(root)

    def next_page(self,master):
        self.root1=Tk()
        master.destroy()
        menu_base1 = MainMenu(self.root1)
        self.root1.mainloop()

    def next_page_id(self):
        self.next_page(root)

root = Tk()
welcome = Welcome(root)
root.mainloop()
