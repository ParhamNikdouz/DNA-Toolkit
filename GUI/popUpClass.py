from GUI.mainMenuClass import *
from tkinter import Label
from GUI.welcomeClass import *


class PopUp:
    fasta_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\ebola.fasta')
    excel_ad = ('E:\MY CODES\PYTHON\DNA-Toolkit\Files\motif_count.xlsx')

    def __init__(self, master):

        master.title("Enter The Motif's Info")
        master.resizable(width=False, height=False)
        width = 375
        height = 100
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws / 4) - (width / 4)
        y = (hs / 4) - (height / 4)
        master.geometry('%dx%d+%d+%d' % (width,height,x,y))

        self.motif_label = Label(master, text="Enter The Motifs :")
        self.plot_label = Label(master, text="Enter X,Y,Z For Plot :")
        self.cluster_label = Label(master, text="Enter The Number Of Clusters :")

        self.motif_label.grid(row=0, column=0)
        self.plot_label.grid(row=1, column=0)
        self.cluster_label.grid(row=2, column=0)

        self.motif_entry = Entry(master, width=30)
        self.plot_entry = Entry(master, width=30)
        self.cluster_entry = Entry(master, width=30)

        self.motif_entry.grid(row=0, column=1)
        self.plot_entry.grid(row=1, column=1)
        self.cluster_entry.grid(row=2, column=1)

        self.submit_button = Button(master, text="Submit", command=self.get_info)
        self.submit_button.grid(row=3,column=1)

    def get_info(self):

        self.motif_object = Motif(self.fasta_ad, self.excel_ad)
        self.cluster_number = self.cluster_entry.get()
        self.plot_dim = self.plot_entry.get()
        self.plot_dim = self.plot_dim.split(',')
        self.motif_info = self.motif_entry.get()
        self.motif_info = self.motif_info.split(',')

        if (len(self.plot_dim) == 0):
            self.motif_info.resetF()
        else:
            if (len(self.plot_dim) == 2):
                self.motif_object.setPlotFields(self.plot_dim[0], self.plot_dim[1], sf3=None)
            elif (len(self.plot_dim) == 3):
                self.motif_object.setPlotFields(self.plot_dim[0], self.plot_dim[1], self.plot_dim[2])

        print(self.motif_info)
        print(self.plot_dim)
        print(self.cluster_number)
        return [self.motif_object, self.motif_info, self.plot_dim, self.cluster_number]


