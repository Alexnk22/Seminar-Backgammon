from tkinter import*
root = Tk()

canvas = Canvas(root,height=300, width=400)
canvas.pack(side=TOP,fill=BOTH,expand=YES)

def open():
    root.destroy()

btn = Button(root,text="Play",command=open).pack()

root.mainloop()