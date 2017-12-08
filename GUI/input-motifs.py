from tkinter import *



root = Tk()
root.title('DNA-Toolkit (Beta)')


def get_motifs():
    motiflist = []

    # motiflist = []
    motifs = my_entry.get()  # AA,BB,CC
    for i in range(len(motifs)):
        a1 = motifs.split(',')
    motiflist.append(a1)
    n = motiflist[0][0]
    new_motif_list = []
    for i in range(len(motiflist[0])):
        if (i==0):
            continue
        new_motif_list.append(motiflist[0][i])


my_label = Label(root, text = "Now, Please Enter The Motifs :")
my_label.grid(row = 0, column = 1)
my_entry = Entry(root,width=30)
my_entry.grid(row = 1, column = 1)

my_button = Button(root, text = "Submit", command = get_motifs)
my_button.grid(row = 2, column = 1)

root.mainloop()
