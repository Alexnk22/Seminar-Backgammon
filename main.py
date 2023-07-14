from tkinter import *


TOPorBOT = 0 
Dreieck = 0
Pos1 = 0

root = Tk()

root.minsize(width=550,height=550)

canvas = Canvas(root,height=550, width=550)
canvas.pack(side=TOP,fill=BOTH,expand=YES)

spielfeld2 = (0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2)    #black
spielfeld1 = (2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0)    #white
   #          1 2 3 4 5 6    7 8 9 1 1 1        1 1 1 1 1 1    1 2 2 2 2 2
#                                  0 1 2        3 4 5 6 7 8    9 0 1 2 3 4

def Ratios (event=NONE):
    canvas.delete("all")
    
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800
         
    else:
        Ratio = root.winfo_height()/800
    
    
    Feld(Ratio)
    Figuren(Ratio, spielfeld1, "white",12)
    Figuren(Ratio, spielfeld2, "maroon",12)
    Mark(Ratio,Pos1,spielfeld1,"green")
    Mark(Ratio,Pos1,spielfeld2,"blue")
    
    

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



#zuerst aufgerufen mit weiß und dann mit schwarz 
def Figuren(Ratio, spielfeld, farbe,verschiebung):
    for u in range(12):
        for i in range(int(spielfeld[u])):
            if u >= 6:
                r = 15
            else:
                r = 0
            canvas.create_oval((673-(u*53)-r)*Ratio, (600-(i)*50)*Ratio, (723-(u*53)-r)*Ratio, (650-(i)*50)*Ratio, fill=farbe, width=1.33)
           
                               
    for u in range(12):
        for i in range(int(spielfeld[int(u)+verschiebung])):
            if u >= 6:
                r = 15
            else:
                r = 0
            canvas.create_oval((75+u*53+r)*Ratio, (75+i*50)*Ratio, (125+u*53+r)*Ratio, (125+i*50)*Ratio, fill=farbe, width=1.33)
                               


def Position(event):

    global Dreieck
    global TOPorBOT
    global Pos1
    global spielfeld1
    global spielfeld2
    
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800         
    else:
        Ratio = root.winfo_height()/800



    for i in range (1,13):
        if i > 6:
            r = 18
        else:
            r = 0


        if (event.x/Ratio-27-r)//52 == i:
            Dreieck = i


    if   0 < (event.y/Ratio-75) < 250:
        TOPorBOT = 2    #oben
    elif 325 < (event.y/Ratio-75) < 575:
        TOPorBOT = 1    #unten
    else:
        TOPorBOT = 0





#    if   ((spielfeld2[Dreieck+11]*50)-50) < (event.y/Ratio-75) < (spielfeld2[Dreieck+11])*50 or ((spielfeld1[Dreieck+11]*50)-50) < (event.y/Ratio-75) < (spielfeld1[Dreieck+11])*50:
#        TOPorBOT = 2    #oben
#    
#    elif 575 - spielfeld2[13-Dreieck]*(50) < (event.y/Ratio-75) < 575 - spielfeld2[13-Dreieck]*(50)+50 or 575 - spielfeld1[13-Dreieck]*(50) < (event.y/Ratio-75) < 575 - spielfeld1[13-Dreieck]*(50)+50:
#        TOPorBOT = 1    #unten
#    else:
#        TOPorBOT = 0



    if (int(TOPorBOT) == 1) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725):
        Pos1 = 13 - int(Dreieck)
        print(Pos1)
        Ratios(event)

    elif (int(TOPorBOT) == 2) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725):
        Pos1 = int(Dreieck) + 12
        print(Pos1)
        Ratios(event)        
        


def Mark (Ratio,Pos1,spielfeld, farbe):
  
    if 6 < Pos1 < 13 or 18 < Pos1 < 25:
        r = 15
    else:
        r = 0

    if 0 < Pos1 < 13 :
        if spielfeld[Pos1-1] != 0:   
            canvas.create_oval((725-(Pos1*53)-r)*Ratio, (650-(int(spielfeld[Pos1-1]))*50)*Ratio, (775-(Pos1*53)-r)*Ratio, (700-(int(spielfeld[Pos1-1]))*50)*Ratio, width=4,outline=farbe)
    
    if 12 < Pos1 < 25 : 
        if spielfeld[Pos1-1] != 0:
            canvas.create_oval((75+((Pos1-13)*53)+r)*Ratio, (25+int(spielfeld[Pos1-1])*50)*Ratio, (125+((Pos1-13)*53)+r)*Ratio, (75+int(spielfeld[Pos1-1])*50)*Ratio, width=4,outline=farbe)
            
           

    

def würfel():
    pass


canvas.bind("<Button-1>", Position, Mark)
root.bind("<Configure>", Ratios)
root.mainloop()