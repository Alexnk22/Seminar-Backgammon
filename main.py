from tkinter import *
import random

root = Tk()

root.minsize(width=550,height=550)

canvas = Canvas(root,height=550, width=550)
canvas.pack(side=TOP,fill=BOTH,expand=YES)


spielfeld1 = (2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0)    #white
spielfeld2 = (0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2)    #black


def Ratios (event=NONE):
    canvas.delete("all")
    
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800
         
    else:
        Ratio = root.winfo_height()/800
        
    Feld(Ratio)
    Figuren(Ratio)

#Erstellt das Feld 
def Feld(Ratio):
    
    for u in range (2):
        canvas.create_rectangle((75+u*332.5)*Ratio,75*Ratio,(392.5+u*332.5)*Ratio,650*Ratio,fill="goldenrod",width=2)
        canvas.create_rectangle(75*Ratio,75*Ratio,(725)*Ratio,650*Ratio,width=4)

    for u in range (2):
        for i in range (3):
            canvas.create_polygon((i*106+75+u*333)*Ratio, 75*Ratio, (i*106+100+u*333)*Ratio, 325*Ratio, (i*106+125+u*333)*Ratio, 75*Ratio,fill="red",outline="black",)
            canvas.create_polygon((i*106+127.5+u*333)*Ratio, 75*Ratio, (i*106+152.5+u*333)*Ratio, 325*Ratio, (i*106+177.5+u*333)*Ratio, 75*Ratio)

            canvas.create_polygon((i*106+75+u*333)*Ratio, 650*Ratio, (i*106+100+u*333)*Ratio, 400*Ratio, (i*106+125+u*333)*Ratio, 650*Ratio)
            canvas.create_polygon((i*106+127.5+u*333)*Ratio, 650*Ratio, (i*106+152.5+u*333)*Ratio, 400*Ratio, (i*106+177.5+u*333)*Ratio, 650*Ratio,fill="red",outline="black")

#erstellt die anzahl von keisen die in der liste gefragt sind 
def Figuren(Ratio):

    global spielfeld1

    for u in range(12):
        for i in range(int(spielfeld1[int(u)])):
            if u >= 6:
                r = 15
            else: 
                r = 0
            canvas.create_oval((673-(u*53)-r)*Ratio,(600-(i)*50)*Ratio,(723-(u*53)-r)*Ratio,(650-(i)*50)*Ratio,fill="white",width=1.33)

    for u in range(12):
        for i in range(int(spielfeld1[int(u)+12])):
            if u >= 6:
                r = 15
            else: 
                r = 0
            canvas.create_oval((75+u*53+r)*Ratio,(75+i*50)*Ratio,(125+u*53+r)*Ratio,(125+i*50)*Ratio,fill="white",width=1.33)
    for u in range(12):
        for i in range(int(spielfeld2[int(u)])):
            if u >= 6:
                r = 15
            else: 
                r = 0
            canvas.create_oval((673-(u*53)-r)*Ratio,(600-(i)*50)*Ratio,(723-(u*53)-r)*Ratio,(650-(i)*50)*Ratio,fill="maroon",width=1.33)

    for u in range(12):
        for i in range(int(spielfeld2[int(u)+12])):
            if u >= 6:
                r = 15
            else: 
                r = 0
            canvas.create_oval((75+u*53+r)*Ratio,(75+i*50)*Ratio,(125+u*53+r)*Ratio,(125+i*50)*Ratio,fill="maroon",width=1.33)


def würfel():
    pass
root.bind("<Configure>", Ratios)
root.mainloop()