from tkinter import *
import random

movecounter = 1
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
Pass=False


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
# wird die ganze zeit gerufen wenn etwas neues erscheint 
def Ratios (event=NONE):
    canvas.delete("all")
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800
    else:
        Ratio = root.winfo_height()/800
    Feld(Ratio)
    Figuren(Ratio, spielfeld1, "white",12)
    Figuren(Ratio, spielfeld2, "maroon",12)

    # das nur das fällt markiert wird von der person die am zug ist 
    if movecounter % 2 == 0:
        mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
    else:
        mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")
    show_Würfel(Ratio,Würfel1,0)
    show_Würfel(Ratio,Würfel2,1)
    mark_possible_pos(Ratio, spielfeld3,"yellow",12)
    
# erstellt das stielfeld ohne Figuren 
def Feld(Ratio):

    if movecounter % 2 != 0 and movecounter != 1:
        canvas.create_rectangle(0,0,70*Ratio,70*Ratio,fill="red")
    elif movecounter % 2 == 0:
        canvas.create_rectangle(0,0,70*Ratio,70*Ratio,fill="white")

    for u in range (2):
        canvas.create_rectangle((75+u*332.5)*Ratio,75*Ratio,(392.5+u*332.5)*Ratio,650*Ratio,fill="goldenrod",width=2)
        canvas.create_rectangle(75*Ratio,75*Ratio,(725)*Ratio,650*Ratio,width=4)

    for u in range (2):
        for i in range (3):
            canvas.create_polygon((i*106+75+u*333)*Ratio, 75*Ratio, (i*106+100+u*333)*Ratio, 325*Ratio, (i*106+125+u*333)*Ratio, 75*Ratio,fill="red",outline="black",)
            canvas.create_polygon((i*106+127.5+u*333)*Ratio, 75*Ratio, (i*106+152.5+u*333)*Ratio, 325*Ratio, (i*106+177.5+u*333)*Ratio, 75*Ratio)

            canvas.create_polygon((i*106+75+u*333)*Ratio, 650*Ratio, (i*106+100+u*333)*Ratio, 400*Ratio, (i*106+125+u*333)*Ratio, 650*Ratio)
            canvas.create_polygon((i*106+127.5+u*333)*Ratio, 650*Ratio, (i*106+152.5+u*333)*Ratio, 400*Ratio, (i*106+177.5+u*333)*Ratio, 650*Ratio,fill="red",outline="black")

#erstellt die Figuren in zusammenarbeit mit der spielfeldliste 1 und 2 
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
                               
# filtert die x und y koordinaten des mausklicks und findet Pos1 heraus 
def Position(event):
    global Dreieck, TOPorBOT, Pos1,Pos22,Pos21
    spielfeld3[int(Pos21)-1] = 0
    spielfeld3[int(Pos22)-1] = 0
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800         
    else:
        Ratio = root.winfo_height()/800

    # wegen der verschiebung in der mitte des feldes 
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
    # ersten and und or bedinungen damit nichts passiert wenn man auserhalb des feldes drückt
    # zweite and und or bedingung damit am anfang man einmal würfel muss damit man etwas machen kann (Würfel = 7 am anfang)
    # drittens and und or damit das wenn beide würfel 0 sind das man nichts meht machen kann bis wieder gewürfeld wird 
    if (int(TOPorBOT) == 1) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and (Würfel1[0] != 7 or Würfel2[0] != 7 ) and (Würfel1[0] != 0 or Würfel2[0] != 0 ):
        Pos1 = 13 - int(Dreieck)
        Ratios()
        set_possibel_pos()

    #das gleiche für die oberen postionen
    elif (int(TOPorBOT) == 2) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and (Würfel1[0] != 7 or Würfel2[0] != 7) and (Würfel1[0] != 0 or Würfel2[0] != 0 ):
        Pos1 = int(Dreieck) + 12
        Ratios()        
        set_possibel_pos()

# markiert die position die angeklickt wurde 
# würd 2 mal aufgerufen in Ratios. Ein mal wird die liste durchgegangen mit den weißen steine dan mit den roten 
def mark_mouse_pos1 (Ratio,Pos1,spielfeld, farbe):
    #fpr die verschiebung 
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
    global Pos21,Pos22,Pos1, movecounter, Pass
    Pos1 = 15
    #! es feht das wenn man nicht ziehen kann das man dann trotzdem würfeln kann. dafür muss warscheinlih noch ein or bedingung in abhängigkeit von spielfeld3 kommen.
    if (Würfel1[0] == 0 and Würfel2[0] == 0) or (Würfel1[0] == 7 and Würfel2[0] == 7) or Pass==True:
        if Pass == False:
            movecounter = movecounter + 1 
        # nach jedem Würfel wurf soll die possible Position gelöscht werden da sie ja entweder augebrauht wurden oder der spieler nicht fahren kann 
        spielfeld3[int(Pos21)-1] = 0
        spielfeld3[int(Pos22)-1] = 0

        #movecounter geht bei jedem wurf hoch d.h mit jedem wurf wächstelt der spieler 
        #movecounter = movecounter + 1
        a = random.randint(1,6)
        b = random.randint(1,6)
        
        #löscht die liste jedes mal (nur notwendig wegen den pasch bis jetzt)
        Würfel1.clear()
        Würfel2.clear()
        #! soll für pasch sein. Muss mir was ganz neues dafür überlegen 
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
        Pass = False
        

#lässt den würfel erscheinen. Wird auch wieder 2 mal aufgerufen. Einmal mit dem ersten und dann mit dem zweiten Würfel. die Verschiebung (Ver) macht den unterschied 
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

# wird von Position gerufen also wird bei jedem richtigen klick getriggert                     
def set_possibel_pos():
    global Pos21,Pos22

    #setzt die vorherigen Possible Positions zurück falls ein spieler nicht mit der figur zieht die er als erstes angeklickt hat 
    spielfeld3[int(Pos21)-1] = 0
    spielfeld3[int(Pos22)-1] = 0
    
    # schaut für die weißen steine und da weiß zuerst muss movecounter % 2 == 0. 
    if spielfeld1[Pos1-1] != 0 and movecounter % 2 == 0:
        # < 25 da die Possible Possitions nicht auserhalb der 25 möglichen felder sein darf und da weiß von 0 -> 25 geht muss nicht auf > 0 sein 
        # Pos 21 and Pos 22 sind die möglichen positionen die sich durch den würfel 1 und würfel 2 ergeben  
        if Pos1 + int(Würfel1[0]) < 25:
            Pos21 = Pos1 + int(Würfel1[0])
        else:
            Pos21 = 0
        if Pos1 + int(Würfel2[0]) < 25:
            Pos22 = Pos1 + int(Würfel2[0])
        else:
            Pos21 = 0
        # erste bedingung damit man nicht auf die figur des gegners platzieren kann 
        #! die erste bedingung muss geändert werden zu 1 damit man figuren schlagen kann  
        # 2 bedingung mach ein maximum von 5 stinen pro Dreieck 
        # 3 bedingung löst den fehler das bei 0 keine pos Posiition auf dem gleichen feld angezeigt wird 
        if spielfeld2[int(Pos21)-1] == 0 and spielfeld1[int(Pos21)-1] <5 and int(Würfel1[0]) != 0:
                spielfeld3[int(Pos21)-1] = int((spielfeld1[int(Pos21)-1])+1)
        if spielfeld2[int(Pos22)-1] == 0 and spielfeld1[int(Pos22)-1] <5 and int(Würfel2[0]) != 0:
                spielfeld3[int(Pos22)-1] = int((spielfeld1[int(Pos22)-1])+1)            
        Ratios()
    
    # gleiche für die roten steine 
    elif spielfeld2[Pos1-1] != 0 and movecounter % 2 != 0:
        if Pos1 - int(Würfel1[0]) > 0 :
            Pos21 = Pos1 - int(Würfel1[0])
        else:
            Pos21 = 0
        if  Pos1 - int(Würfel2[0]) > 0:
            Pos22 = Pos1 - int(Würfel2[0])
        else:
            Pos22 = 0
        if spielfeld1[int(Pos21)-1] == 0 and spielfeld2[int(Pos21)-1] <5 and int(Würfel1[0]) != 0:
                spielfeld3[int(Pos21)-1] = int((spielfeld2[int(Pos21)-1])+1)
        if spielfeld1[int(Pos22)-1] == 0 and spielfeld2[int(Pos22)-1] <5 and int(Würfel2[0]) != 0:
                spielfeld3[int(Pos22)-1] = int((spielfeld2[int(Pos22)-1])+1)
        Ratios()

# wird mit spielfeld3 gerufen 
def mark_possible_pos(Ratio,spielfeld,farbe,verschiebung):     
    for u in range(12):
        for i in range(int(spielfeld[u])):
            if u >= 6:
                    r = 15
            else:
                    r = 0
            #erstellt einen gelben kreis bei der pos von spielfeld3 (immer eine nkreis mehr wie die kreise die bisher das sind)
            canvas.create_oval((673-(u*53)-r)*Ratio, (600-(i)*50)*Ratio, (723-(u*53)-r)*Ratio, (650-(i)*50)*Ratio, fill=farbe, width=1)
            
            #feld muss gerufen werden um die unnötigen gelben kreise zu verdecken 
            # dann muss auch die mouse markierung neu sein da es sonst schlecht aussieht 
            # lägt momentan ein bischen wenn der gelbe keits auf einen anderen kreis muss
            Figuren(Ratio, spielfeld1, "white",12)
            Figuren(Ratio, spielfeld2, "maroon",12)
            mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
            mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")   

# gleiche nur oben und nicht unten  
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

# wird bei einem rechtsklick getriggert 
# verwendet den gleichen angloritmus zum finden von Pos2 wie aus Position mit Pos1 
def Position2(event=NONE):
    global Dreieck2, TOPorBOT2, Pos2   
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
        #nach einem rechtsklick muss aber der move passieren und ruft daher move()
        move()
    elif (int(TOPorBOT2) == 2) and (75 < (event.x/Ratio) < 392.5 or 407.5 < (event.x/Ratio) < 725) and Würfel1[0] != 7:
        Pos2 = int(Dreieck2) + 12
        move()
        
def move():
    global Pos1, movecounter
    # prüfft ob das feld was man anklickt (Pos2) mit der Possible position (Pos21 nd Pos22)übereinstimmt. Wenn ja setzt es den jewiligen würfel auf 0.
    if Pos2 == Pos21 :
        Würfel1[0] = 0
        
    elif Pos2 == Pos22 :
        Würfel2[0] = 0
    
    # Prüft spielfeld3 ob die angeklickte position möglich ist 
    # zweite nedingung schaut ob die angeklickte figur eine weise figur ist und somit in spielfeld1 nicht 0 ist.
    if spielfeld3[Pos2-1] != 0 and spielfeld1[Pos1-1] != 0:
        # zieht eine figur von der Pos1 ab 
        spielfeld1[Pos1-1] = spielfeld1[Pos1-1]-1
        # füght eine figur bei Pos2 hinzu 
        spielfeld1[Pos2-1] = spielfeld1[Pos2-1]+1
        #setzt spielfeld3 zurück 
        spielfeld3[int(Pos21)-1] = 0
        spielfeld3[int(Pos22)-1] = 0

    # gleiche nur schaut nun ob das angeklickte feld rot ist 
    elif spielfeld3[Pos2-1] != 0 and spielfeld2[Pos1-1] != 0:
        spielfeld2[Pos1-1] = spielfeld2[Pos1-1]-1
        spielfeld2[Pos2-1] = spielfeld2[Pos2-1]+1
        spielfeld3[int(Pos21)-1] = 0
        spielfeld3[int(Pos22)-1] = 0
    # damit nach der Ratios() die markierung weg ist bei der angeklickten figur 
    
    Pos1 = 0
    Ratios()

#lässt einen mit "w" würfeln
def key(event):
    if event.char == "w":
        Würfel_wurf()
    elif event.char == "p":
        Pass_turn()
    


def File():
    global spielfeld1, spielfeld2, spielfeld3, movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2, Pos1, Pos2, Würfel1, Würfel2, Pos21, Pos22
    spielfeld3 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]    #marker
    spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    #black
    spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    #white
    movecounter = 1
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
    Ratios()

def AI():
    pass
def PvP():
    pass
def Pass_turn():
    global Pass, movecounter,Pos1, spielfeld3
    movecounter = movecounter +1
    Würfel1[0] = 0
    Würfel2[0] = 0
    Pos1 = 0
    spielfeld3 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]
    Ratios()
    Pass=True

mein_menu = Menu(root)
root.config(menu=mein_menu)


file_menu = Menu(mein_menu)
mein_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=File)
file_menu.add_command(label="Exit", command=root.quit)

Würfel_menu = Menu(mein_menu)
mein_menu.add_cascade(label="Dice",command=Würfel_wurf)

Pass_menu = Menu(mein_menu)
mein_menu.add_cascade(label="Pass",command=Pass_turn)

Game_mode_menu = Menu(mein_menu)
mein_menu.add_cascade(label="Game mode", menu=Game_mode_menu)
Game_mode_menu.add_command(label="Player vs. AI", command=AI)
Game_mode_menu.add_command(label="Player  vs. Player",command=PvP)



canvas.bind("<Button-1>", Position)
canvas.bind("<Button-3>", Position2)
root.bind("<Key>", key)
root.bind("<Configure>", Ratios)
root.mainloop()