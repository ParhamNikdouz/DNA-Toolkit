from tkinter import *


class GUI:

    def __init__(self,master):

        w = 800
        h = 650
        ws = master.winfo_screenwidth()
        hs = master.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        master.geometry('%dx%d+%d+%d' % (w,h,x,y))
        master.title('DNA-Toolkit (Beta)')

    def labels(self,master,label_txt,label_x,label_y,label_font):

        label = Label(master,text=label_txt,font=label_font)
        label.place(x=label_x,y=label_y)

    def entries(self,master,entry_id,entry_x,entry_y):

        entry_id = Entry(master,width=30)
        entry_id.place(x=entry_x,y=entry_y)

    def buttons(self,master,button_txt,button_x,button_y,button_width,button_height,bg_color,button_font):
        button = Button(master,text=button_txt,height=button_height,width=button_width,bg=bg_color,font=button_font)
        button.place(x=button_x,y=button_y)


root = Tk()
window = GUI(root)
window.labels(root,"DNA-Toolkit(Beta)",450,100,('Verdana', 50))
window.labels(root,"Enter Fasta File Address :",500,275,('Verdana', 15))
window.labels(root,"Enter Excel File Address :",500,300,('Verdana', 15))
window.entries(root,1,790,282)
window.entries(root,2,790,306)
window.buttons(root,"Browse",990,281,5,1,"Gray",('Verdana', 8))
window.buttons(root,"Browse",990,301,5,1,"Gray",('Verdana', 8))
window.buttons(root,"NEXT",725,450,8,2,"Red",('Verdana', 10))
root.mainloop()
