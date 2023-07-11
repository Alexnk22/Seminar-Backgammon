from tkinter import *
import random

root = Tk()

root.minsize(width=550,height=550)

canvas = Canvas(root,height=550, width=550)
canvas.pack(side=TOP,fill=BOTH,expand=YES)


spielfeld1 = [(2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0)]    #withe 
spielfeld1 = [(2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0)]    #black

#zum Vergrößern(fehler mit dem Würfel knopf)
def Ratios (event=NONE):
    canvas.delete("all")
    
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800
         
    else:
        Ratio = root.winfo_height()/800
        
    Feld(Ratio)

#Erstellt das Feld 
def Feld(Ratio):
    
    for u in range (2):
        canvas.create_rectangle((75+u*332.5)*Ratio,75*Ratio,(392.5+u*332.5)*Ratio,650*Ratio)
        canvas.create_rectangle(75*Ratio,75*Ratio,(725)*Ratio,650*Ratio,width=1.5)

    for u in range (2):
        for i in range (3):
            canvas.create_polygon((i*106+75+u*332.5)*Ratio, 75*Ratio, (i*106+100+u*332.5)*Ratio, 325*Ratio, (i*106+125+u*332.5)*Ratio, 75*Ratio,fill="white",outline="black",)
            canvas.create_polygon((i*106+127.5+u*332.5)*Ratio, 75*Ratio, (i*106+152.5+u*332.5)*Ratio, 325*Ratio, (i*106+177.5+u*332.5)*Ratio, 75*Ratio)

            canvas.create_polygon((i*106+75+u*332.5)*Ratio, 650*Ratio, (i*106+100+u*332.5)*Ratio, 400*Ratio, (i*106+125+u*332.5)*Ratio, 650*Ratio)
            canvas.create_polygon((i*106+127.5+u*332.5)*Ratio, 650*Ratio, (i*106+152.5+u*332.5)*Ratio, 400*Ratio, (i*106+177.5+u*332.5)*Ratio, 650*Ratio,fill="white",outline="black")



root.bind("<Configure>", Ratios)
root.mainloop()