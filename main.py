from tkinter import *
import random



movecounter = 0
TOPorBOT = 0 
TOPorBOT2 = 0
Dreieck = 0
Dreieck2 = 0
Pos1 = 0
Pos2 = 0
Würfel1 = [7]
Würfel2 = [7]
Pos21= 0
Pos22= 0
padding = 50

root = Tk()

root.minsize(width=550,height=550)
root.maxsize(width=900,height=900)


canvas = Canvas(root,height=550, width=550)
canvas.pack(side=TOP,fill=BOTH,expand=YES)

spielfeld3 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]    #marker
spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    #black
spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    #white
#             1 2 3 4 5 6    7 8 9 1 1 1        1 1 1 1 1 1    1 2 2 2 2 2
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
    mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
    mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")
    show_Würfel(Ratio,Würfel1,0)
    show_Würfel(Ratio,Würfel2,1)
    mark_possible_pos(Ratio, spielfeld3,"yellow",12)
    


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
    global Pos1,Pos22,Pos21
    spielfeld3[int(Pos21)-1] = 0
    spielfeld3[int(Pos22)-1] = 0
    
    
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

    #if   0 < ((spielfeld2[Dreieck+11]*50)-50) < (event.y/Ratio-75) < (spielfeld2[Dreieck+11])*50 or 0 < ((spielfeld1[Dreieck+11]*50)-50) < (event.y/Ratio-75) < (spielfeld1[Dreieck+11])*50:
    #    TOPorBOT = 2    #oben
    
    #elif (575 - ((spielfeld2[13-Dreieck])*50)) < (event.y/Ratio-75) < (525 - ((spielfeld2[13-Dreieck])*50)) < 575 or (575 - ((spielfeld1[13-Dreieck])*50)) < (event.y/Ratio-75) < (525 - ((spielfeld1[13-Dreieck])*50)) < 575:
    #    TOPorBOT = 1    #unten
    
    if (int(TOPorBOT) == 1) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and Würfel1[0] != 7:
        Pos1 = 13 - int(Dreieck)
        Ratios()
        set_possibel_pos()

    elif (int(TOPorBOT) == 2) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and Würfel1[0] != 7:
        Pos1 = int(Dreieck) + 12
        Ratios()        
        set_possibel_pos()

def mark_mouse_pos1 (Ratio,Pos1,spielfeld, farbe):
    
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
            
            
                 
def Würfel_wurf():
    global Pos21,Pos22,Pos1
    Pos1 = 15
    spielfeld3[int(Pos21)-1] = 0
    spielfeld3[int(Pos22)-1] = 0
    a = random.randint(1,6)
    b = random.randint(1,6)
    
    Würfel1.clear()
    Würfel2.clear()

    if a == b:
        Würfel1.append(a)
        Würfel2.append(b)
        Würfel1.append(a)
        Würfel2.append(b)
        Ratios()
        

    else:
        Würfel1.append(a)
        Würfel2.append(b)
        Ratios()
        
    
 #root.bind(<"Controle-w">, Würfel_wurf)  

def show_Würfel(Ratio,Würfel,Ver):
    for i in range (1,7):
        if int(Würfel[0]) == i :
            canvas.create_rectangle(500*Ratio,335*Ratio,550*Ratio,385*Ratio,width=1.2)
            canvas.create_rectangle(580*Ratio,335*Ratio,630*Ratio,385*Ratio,width=1.2)
            

            if i == 1 or i == 3 or i == 5: 
                canvas.create_oval((520+Ver*80)*Ratio,355*Ratio,(530+Ver*80)*Ratio,365*Ratio,fill = "black")

            for u in range (2):
                if 1 < i < 7:
                    canvas.create_oval(((u*34)+503+Ver*80)*Ratio,((u*35)+338)*Ratio,((u*34)+513+Ver*80)*Ratio,((u*35)+348)*Ratio,fill = "black") 
                    
                if 3 < i < 7: 
                    canvas.create_oval(((u*34)+503+Ver*80)*Ratio,(373-(35*u))*Ratio,((u*34)+513+Ver*80)*Ratio,(382-(34*u))*Ratio,fill = "black")
                    
                if i == 6:
                    canvas.create_oval(((u*34)+503+Ver*80)*Ratio,355*Ratio,((u*34)+513+Ver*80)*Ratio,365*Ratio,fill = "black")
                    

def set_possibel_pos():
    global Pos21,Pos22
    spielfeld3[int(Pos21)-1] = 0
    spielfeld3[int(Pos22)-1] = 0
    
    if spielfeld1[Pos1-1] != 0:
        if Pos1 + int(Würfel1[0]) < 25:
            Pos21 = Pos1 + int(Würfel1[0])
        else:
            Pos21 = 0
        if Pos1 + int(Würfel2[0]) < 25:
            Pos22 = Pos1 + int(Würfel2[0])
        else:
            Pos21 = 0

        if spielfeld2[int(Pos21)-1] == 0 and spielfeld1[int(Pos21)-1] <5:
                spielfeld3[int(Pos21)-1] = int((spielfeld1[int(Pos21)-1])+1)
                
        
                
        if spielfeld2[int(Pos22)-1] == 0 and spielfeld1[int(Pos22)-1] <5:
                spielfeld3[int(Pos22)-1] = int((spielfeld1[int(Pos22)-1])+1)
                
        Ratios()
        

    elif spielfeld2[Pos1-1] != 0:
        if Pos1 - int(Würfel1[0]) > 0 :
            Pos21 = Pos1 - int(Würfel1[0])
        else:
            Pos21 = 0
        if  Pos1 - int(Würfel2[0]) > 0:
            Pos22 = Pos1 - int(Würfel2[0])
        else:
            Pos22 = 0
        if spielfeld1[int(Pos21)-1] == 0 and spielfeld2[int(Pos21)-1] <5:
                spielfeld3[int(Pos21)-1] = int((spielfeld2[int(Pos21)-1])+1)
                
        if spielfeld1[int(Pos22)-1] == 0 and spielfeld2[int(Pos22)-1] <5:
                spielfeld3[int(Pos22)-1] = int((spielfeld2[int(Pos22)-1])+1)
        Ratios()
        

        
    

def mark_possible_pos(Ratio,spielfeld,farbe,verschiebung):
        
    for u in range(12):
        for i in range(int(spielfeld[u])):
            
            if u >= 6:
                    r = 15
            else:
                    r = 0

            canvas.create_oval((673-(u*53)-r)*Ratio, (600-(i)*50)*Ratio, (723-(u*53)-r)*Ratio, (650-(i)*50)*Ratio, fill=farbe, width=1)
            
            Figuren(Ratio, spielfeld1, "white",12)
            Figuren(Ratio, spielfeld2, "maroon",12)
            mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
            mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")
            
            

                            
    for u in range(12):
        for i in range(int(spielfeld[int(u)+verschiebung])):
            
            if u >= 6:
                    r = 15
            else:
                    r = 0
        
            canvas.create_oval((75+u*53+r)*Ratio, (75+(i)*50)*Ratio, (125+u*53+r)*Ratio, (125+(i)*50)*Ratio, fill=farbe, width=1)

            Figuren(Ratio, spielfeld1, "white",12)
            Figuren(Ratio, spielfeld2, "maroon",12)
            mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
            mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")


def Position2(event=NONE):
    global Dreieck2
    global TOPorBOT2
    global Pos2
    
     
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
            Dreieck2 = i

    if   0 < (event.y/Ratio-75) < 250:
        TOPorBOT2 = 2    #oben
    elif 325 < (event.y/Ratio-75) < 575:
        TOPorBOT2 = 1    #unten
    else:
        TOPorBOT2 = 0
    
    if (int(TOPorBOT2) == 1) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and Würfel1[0] != 7:
        Pos2 = 13 - int(Dreieck2)
        move()
        

    elif (int(TOPorBOT2) == 2) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and Würfel1[0] != 7:
        Pos2 = int(Dreieck2) + 12
        move()
        
def move():
    global Pos1
    if spielfeld3[Pos2-1] != 0 and spielfeld1[Pos1-1] != 0:
        spielfeld1[Pos1-1] = spielfeld1[Pos1-1]-1
        spielfeld1[Pos2-1] = spielfeld1[Pos2-1]+1
        spielfeld3[int(Pos21)-1] = 0
        spielfeld3[int(Pos22)-1] = 0

    elif spielfeld3[Pos2-1] != 0 and spielfeld2[Pos1-1] != 0:
        spielfeld2[Pos1-1] = spielfeld2[Pos1-1]-1
        spielfeld2[Pos2-1] = spielfeld2[Pos2-1]+1
        spielfeld3[int(Pos21)-1] = 0
        spielfeld3[int(Pos22)-1] = 0

   
    Pos1 = 0
    Ratios()
        



def key(event):
    if event.char == "w":
        Würfel_wurf()


mein_menu = Menu(root)
root.config(menu=mein_menu)

def File():
    pass

file_menu = Menu(mein_menu)
mein_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=File)
file_menu.add_command(label="Exit", command=root.quit)

Würfel_menu = Menu(mein_menu)
mein_menu.add_cascade(label="Würfel",command=Würfel_wurf)




canvas.bind("<Button-1>", Position)
canvas.bind("<Button-3>", Position2)
root.bind("<Key>", key)
root.bind("<Configure>", Ratios)
root.mainloop()