from tkinter import *



root = Tk()
root.title('DNA-Toolkit (Beta)')


def get_cluster():
    cluster_numbers = my_entry.get()
    print(cluster_numbers)

my_label = Label(root, text = "Now, Please Enter The Number Of Clusters :")
my_label.grid(row = 0, column = 1)
my_entry = Entry(root,width=30)
my_entry.grid(row = 1, column = 1)

my_button = Button(root, text = "Submit", command = get_cluster)
my_button.grid(row = 2, column = 1)

root.mainloop()
