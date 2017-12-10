import os
import sys
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from Algorithm.motifClass import Motif
from GUI.popUpClass import *
from GUI.defaultClass import Defaults


class MainMenu:

    def __init__(self,master):

        default = Defaults(master)
        master.configure(background='gray')

        self.menubar = Menu(master)
        self.filemenu = Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New Window",command=self.new_window)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit")

        # self.editmenu = Menu(self.menubar, tearoff=0)
        # self.menubar.add_cascade(label="Edit")
        # self.editmenu.add_command(label="Undo")
        # self.editmenu.add_command(label="Redo")

        self.viewmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.viewmenu)
        self.viewmenu.add_command(label="Normal Size", command=self.normalscreen_id)
        self.viewmenu.add_command(label="Full Screen", command=self.fullscreen_id)

        self.runmenu = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Run", menu=self.runmenu)
        self.runmenu.add_command(label="Motif Count",command=self.gui_count_motif)
        self.runmenu.add_command(label="Motif Frequency",command=self.gui_motif_frequency)

        self.runmenu.add_separator()
        self.submenu = Menu(self.runmenu, tearoff=0)
        self.runmenu.add_cascade(label="Clustering", menu=self.submenu)

        self.d2menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="2D", menu=self.d2menu)
        self.d3menu = Menu(self.submenu, tearoff=0)
        self.submenu.add_cascade(label="3D", menu=self.d3menu)
        self.d2menu.add_command(label="K-Means Clustering",command=self.k_means_2d)
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
        self.helpmenu.add_command(label="About DNA-Toolkit")
        self.helpmenu.add_command(label="Contact Us")

        master.config(menu=self.menubar)

    def do_nothing(self):
        print("Ok, Ok, I Won't !")

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

    def k_means_2d(self):
        root = Tk()
        pop_up_window = PopUp(root)
        var = pop_up_window.get_info

        #var[0].clustring_kmeans(2,var[2],var[1])
        #self.get_motifs()
        #self.motif_obj.clustring_kmeans(2,['AA','A','C'],2)


        #new_motif_list = self.new_motif_list
        #print(new_motif_list)
        #n = self.n
        #self.motif_obj.clustring_kmeans(2,new_motif_list,n)

    def gui_count_motif(self):
        fasta_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\ebola.fasta')
        excel_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\motif_count.xlsx')

        count_motif = Motif(fasta_ad, excel_ad)
        count_motif.gui_CountMotif()

    def gui_motif_frequency(self):
        fasta_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\ebola.fasta')
        excel_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\motif_count.xlsx')

        motif_frequency = Motif(fasta_ad, excel_ad)
        motif_frequency.numNmersMotifs()
        motif_frequency.gui_FrequencyMotifs()




