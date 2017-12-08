from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os
import sys
from ALGORITHM.motifClass import Motif


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
        fastaAddr = ('E:\MY CODES\PYTHON\DNA-Toolkit\IMPORT-FILES\ebola.fasta')
        excelAddr = ('E:\MY CODES\PYTHON\DNA-Toolkit\IMPORT-FILES\motif_count.xlsx')
        self.motif_obj = Motif(fastaAddr,excelAddr)
        default = Defaults(master)
        master.configure(background='gray')

        self.menubar = Menu(master)

        self.filemenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New Window",command=self.new_window)
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
        self.runmenu.add_command(label="Motif Count",command=self.gui_count_motif)
        self.runmenu.add_separator()
        self.submenu = Menu(self.runmenu, tearoff=0)
        self.runmenu.add_cascade(label="Clustering", menu=self.submenu)

        self.d2menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="2D", menu=self.d2menu)
        self.d3menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="3D", menu=self.d3menu)
        self.d2menu.add_command(label="K-Means Clustering",command=self.k_means_2d)
        self.d2menu.add_command(label="Mini-Batch K-Means",command=self.clustring_MiniBatchKMeans_2d)
        self.d2menu.add_command(label="Agglomerative Clustering")
        self.d2menu.add_command(label="Spectral Clustering")
        self.d2menu.add_command(label="Birch")
        self.d2menu.add_command(label="Fuzzy-CMeans")
        self.d2menu.add_command(label="Mixture Gaussian")
        self.d2menu.add_command(label="Affinity Propagation")
        self.d2menu.add_command(label="Mean-Shift",command=self.mean_shift_2d)

        self.d3menu.add_command(label="K-Means Clustering",command=self.k_means_3d)
        self.d3menu.add_command(label="Mini-Batch K-Means",command=self.clustring_MiniBatchKMeans_2d)
        self.d3menu.add_command(label="Agglomerative Clustering")
        self.d3menu.add_command(label="Spectral Clustering")
        self.d3menu.add_command(label="Birch")
        self.d3menu.add_command(label="Fuzzy-CMeans")
        self.d3menu.add_command(label="Affinity Propagation")
        self.d3menu.add_command(label="Mean-Shift",command=self.mean_shift_3d)

        self.toolsmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Tools", menu=self.toolsmenu)
        self.toolsmenu.add_command(label="Take A Note", command=self.take_a_note)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)
        self.helpmenu.add_command(label="How To Use?")
        self.helpmenu.add_command(label="About DNA-Toolkit")
        self.helpmenu.add_command(label="Contact Us")

        master.config(menu=self.menubar)

    def do_nothing(self):
        print("Ok, Ok, I Won't !")


    def ask_quit(self):
        if messagebox.askokcancel("EXIT", "Are You Sure?"):
            python = sys.executable
            os.execl(python, python, *sys.argv)

    def fullscreen(self,master):
        master.attributes('-fullscreen', True)

    def normalscreen(selfs,master):
        master.attributes('-fullscreen', False)

    # destroying the master, so fullscreen must be on root1 , . . .
    def fullscreen_id(self):
        self.fullscreen(self.root2)

    def normalscreen_id(self):
        self.normalscreen(self.root2)

    def new_window(self):
        self.root2 = Tk()
        self.root2.title('DNA-Toolkit (Beta)(2)')
        menu_base2 = MainMenu(self.root2)
        self.root2.mainloop()
    def take_a_note(self):
        fw = open('take_a_note.txt','w')
        fw.close()
        fr = open('take_a_note.txt','r')
        taken_note = fr.read()
    def about_program(self):
        file=open()

    def get_motifs(self):
        self.motiflist = []
        self.motifs = self.my_entry.get()  # AA,BB,CC
        for i in range(len(self.motifs)):
            self.a1 = self.motifs.split(',')
            self.motiflist.append(self.a1)
        self.n = self.motiflist[0][0]
        self.new_motif_list = []
        for i in range(len(self.motiflist[0])):
            if (i == 0):
                continue
            self.new_motif_list.append(self.motiflist[0][i])


    def k_means_2d(self):
        #self.get_motifs()
        self.motif_obj.clustring_kmeans(2,['AA','A','C'],2)

        #new_motif_list = self.new_motif_list
        #print(new_motif_list)
        #n = self.n
        #self.motif_obj.clustring_kmeans(2,new_motif_list,n)

    def k_means_3d(self):
        #self.get_motifs()
        self.motif_obj.clustring_kmeans(3,['AA','A','C'],3)

    def clustring_MiniBatchKMeans_2d(self):
        self.motif_obj.clustring_MiniBatchKMeans(2,['AA','GGGGG','AC'],2)

    def clustring_MiniBatchKMeans_3d(self):
        self.motif_obj.clustring_MiniBatchKMeans(3,['AC','AA','B',2])

    def mean_shift_2d(self):
        self.motif_obj.clustring_meanshift(2,['AA','GGGGG','AC'])
    def mean_shift_3d(self):
        self.motif_obj.clustring_meanshift(3,['AA','GGGGG','AC'])

    def gui_count_motif(self):


        #count_motif_root = Tk()
        #my_label = Label(count_motif_root, text="Now, Please Enter The Motifs :")
        #my_label.grid(row=0, column=1)
        #my_entry = Entry(root, width=30)
        #my_entry.grid(row=1, column=1)

        #my_button = Button(root, text="Submit", command=get_motifs)
        #my_button.grid(row=2, column=1)

        self.motif_obj.gui_CountMotif(1)
        #messagebox.showinfo("ACTION", "HTML File Saved In The Project Directory.")


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
        #messagebox.showinfo("ACTION","Loading Completed")

    def browse_excel(self,master):
        master.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Select file",
                                                       filetypes=(("Excel Files", "*.xlsx"),("All Files", "*.*")))
        print(master.filename)
        #messagebox.showinfo("ACTION","Loading Completed")

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
