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
Red_Cap_Piece = 0
White_Cap_Piece = 0


root = Tk()

root.minsize(width=550,height=550)
root.maxsize(width=900,height=900)

canvas = Canvas(root,height=550, width=550)
canvas.pack(side=TOP,fill=BOTH,expand=YES)

spielfeld3 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]    #marker
#spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    #black
spielfeld2 = [1,0,1,0,1,0   ,1,0,1,0,1,0       ,1,0,1,0,1,0,   1,0,1,0,1,0]    #black
#spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    #white
spielfeld1 = [0,1,0,1,0,1   ,0,1,0,1,0,1       ,0,1,0,1,0,1,   0,1,0,1,0,1]    #white

#             1 2 3 4 5 6    7 8 9 1 1 1        1 1 1 1 1 1    1 2 2 2 2 2
#                                  0 1 2        3 4 5 6 7 8    9 0 1 2 3 4
# wird die ganze zeit gerufen wenn etwas neues erscheint 
def Ratios (event=NONE):
    global White_Cap_Piece,Red_Cap_Piece
    canvas.delete("all")
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/800
    else:
        Ratio = root.winfo_height()/800
    Feld(Ratio)
    Figuren(Ratio, spielfeld1, "white",12)
    Figuren(Ratio, spielfeld2, "maroon",12)

    # das nur das fällt markiert wird von der person die am zug ist 
    if movecounter % 2 == 0 and White_Cap_Piece == 0:
        mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")

    elif movecounter % 2 != 0 and Red_Cap_Piece == 0:
        mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")

    show_Würfel(Ratio,Würfel1,0)
    show_Würfel(Ratio,Würfel2,1)
    mark_possible_pos(Ratio, spielfeld3,"yellow",12)
    show_Cap_Piece(Ratio)


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
    if (int(TOPorBOT) in (1, 2)) and (75 < event.x / Ratio < 392.5 or 407.5 < event.x / Ratio < 725) and (Würfel1[0] != 7 or Würfel2[0] != 7) and (Würfel1[0] != 0 or Würfel2[0] != 0):
        Pos1 = 13 - int(Dreieck) if TOPorBOT == 1 else int(Dreieck) + 12

        Ratios()        
        set_possibel_pos()
    

# markiert die position die angeklickt wurde 
# würd 2 mal aufgerufen in Ratios. Ein mal wird die liste durchgegangen mit den weißen steine dan mit den roten 
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
    global Pos21, Pos22, Pos1, movecounter, Pass

    if (Würfel1[0] == 0 and Würfel2[0] == 0) or (Würfel1[0] == 7 and Würfel2[0] == 7) or Pass == True:
        if Pass == False:
            movecounter = movecounter + 1

        spielfeld3[int(Pos21) - 1] = 0
        spielfeld3[int(Pos22) - 1] = 0
        Würfel1.clear()
        Würfel2.clear()
        a, b = random.randint(1, 6), random.randint(1, 6)
        if a == b:
            Würfel1.extend([a, a])
            Würfel2.extend([b, b])
        else:
            Würfel1.extend([a, 1])
            Würfel2.extend([b, 2])
        Ratios()
        Pass = False

   

#lässt den würfel erscheinen. Wird auch wieder 2 mal aufgerufen. Einmal mit dem ersten und dann mit dem zweiten Würfel. die Verschiebung (Ver) macht den unterschied 
def show_Würfel(Ratio, würfel_list, ver):
    for i in range(1, 7):
        if int(würfel_list[0]) == i:
            canvas.create_rectangle(500*Ratio, 335*Ratio, 550*Ratio, 385*Ratio, width=1.2)
            canvas.create_rectangle(580*Ratio, 335*Ratio, 630*Ratio, 385*Ratio, width=1.2)
            if i == 1 or i == 3 or i == 5:
                canvas.create_oval((520+ver*80) * Ratio, 355 * Ratio, (530+ver*80) * Ratio, 365 * Ratio, fill="black")
            for u in range(2):
                if 1 < i < 7:
                    canvas.create_oval(((u*34)+503+ver*80) * Ratio, ((u*35)+338) * Ratio, ((u*34)+513+ver*80) * Ratio, ((u*35)+348) * Ratio, fill="black")
                if 3 < i < 7:
                    canvas.create_oval(((u*34)+503+ver*80) * Ratio, (373-(35*u)) * Ratio, ((u*34)+513+ver*80) * Ratio, (382-(34*u)) * Ratio, fill="black")
                if i == 6:
                    canvas.create_oval(((u*34)+503+ver*80) * Ratio, 355 * Ratio, ((u*34)+513+ver*80) * Ratio, 365 * Ratio, fill="black")

#! FEHLER ENTDECKT WENN DIE POS21 ODER POS22 AU?ERHALB RANGE SIND KANN ICH NUR RECHTSKLICK MACHEN NICHT LINKSKLICK 

# wird von Position gerufen also wird bei jedem richtigen klick getriggert                     
def set_possibel_pos():
    global Pos21, Pos22,White_Cap_Piece,Red_Cap_Piece

    spielfeld3[Pos21 - 1] = spielfeld3[Pos22 - 1] = 0
    
    if spielfeld1[Pos1 - 1] != 0 and movecounter % 2 == 0 and White_Cap_Piece == 0:
        Pos21 = Pos1 + Würfel1[0]
        Pos22 = Pos1 + Würfel2[0]

        if 0 < Pos21 < 25:
            if spielfeld2[Pos21 - 1] == 0 and spielfeld1[Pos21 - 1] < 5 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld1[Pos21 - 1] + 1
            elif spielfeld2[Pos21 - 1] == 1 and spielfeld1[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1

        if 0 < Pos22 < 25:
            if spielfeld2[Pos22 - 1] == 0 and spielfeld1[Pos22 - 1] < 5 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld1[Pos22 - 1] + 1
            elif spielfeld2[Pos22 - 1] == 1 and spielfeld1[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()
    # 3te and weg und hinmachen das wenn dir neu erscheinende kreis angeklickt wird der vlaue True abgefragt wird abuch bei vorletzter el if 
    elif White_Cap_Piece != 0 and movecounter % 2 == 0 and spielfeld1[Pos1 - 1] != 0:
        Pos21 = Würfel1[0]
        Pos22 = Würfel2[0]
        if 0 < Pos21 < 25:
            if spielfeld2[Pos21 - 1] == 0 and spielfeld1[Pos21 - 1] < 5 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld1[Pos21 - 1] + 1
            elif spielfeld2[Pos21 - 1] == 1 and spielfeld1[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1

        if 0 < Pos22 < 25:
            if spielfeld2[Pos22 - 1] == 0 and spielfeld1[Pos22 - 1] < 5 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld1[Pos22 - 1] + 1
            elif spielfeld2[Pos22 - 1] == 1 and spielfeld1[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()

    elif spielfeld2[Pos1 - 1] != 0 and movecounter % 2 != 0 and Red_Cap_Piece == 0:
        Pos21 = Pos1 - Würfel1[0]
        Pos22 = Pos1 - Würfel2[0]

        if 0 < Pos21 < 25:
            if spielfeld1[Pos21 - 1] == 0 and spielfeld2[Pos21 - 1] < 5 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld2[Pos21 - 1] + 1
            elif spielfeld1[Pos21 - 1] == 1 and spielfeld2[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1

        if 0 < Pos22 < 25:
            if spielfeld1[Pos22 - 1] == 0 and spielfeld2[Pos22 - 1] < 5 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld2[Pos22 - 1] + 1
            elif spielfeld1[Pos22 - 1] == 1 and spielfeld2[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()
    elif Red_Cap_Piece != 0 and movecounter % 2 != 0 and spielfeld2[Pos1 - 1] != 0:
        Pos21 = 25 - Würfel1[0]
        Pos22 = 25 - Würfel2[0]
        if 0 < Pos21 < 25:
            if spielfeld1[Pos21 - 1] == 0 and spielfeld2[Pos21 - 1] < 5 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld2[Pos21 - 1] + 1
            elif spielfeld1[Pos21 - 1] == 1 and spielfeld2[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1

        if 0 < Pos22 < 25:
            if spielfeld1[Pos22 - 1] == 0 and spielfeld2[Pos22 - 1] < 5 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld2[Pos22 - 1] + 1
            elif spielfeld1[Pos22 - 1] == 1 and spielfeld2[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()


def mark_possible_pos(Ratio,spielfeld,farbe,verschiebung):
    for u in range(12):
        r = 15 if u >= 6 else 0
        if spielfeld[u] != -1 and spielfeld[u] != 0:
            canvas.create_oval((673 - (u * 53) - r) * Ratio, (600 - (spielfeld[u]-1) * 50) * Ratio, (723 - (u * 53) - r) * Ratio, (650 - (spielfeld[u]-1) * 50) * Ratio, fill=farbe, width=1)

        elif spielfeld[u] == -1:
            canvas.create_oval((673 - (u * 53) - r) * Ratio, (610) * Ratio, (723 - (u * 53) - r) * Ratio, (640) * Ratio, fill=farbe, width=1)
        
    for u in range(12):
        r = 15 if u >= 6 else 0 
        if spielfeld[u + verschiebung] != -1 and spielfeld[u+verschiebung] != 0:
            canvas.create_oval((75 + u * 53 + r) * Ratio, (75 + (spielfeld[u+verschiebung]-1) * 50) * Ratio, (125 + u * 53 + r) * Ratio, (125 + (spielfeld[u+verschiebung]-1) * 50) * Ratio, fill=farbe, width=1)
                  
        elif spielfeld[u + verschiebung] == -1:
            canvas.create_oval((75 + u * 53 + r) * Ratio, (85) * Ratio, (125 + u * 53 + r) * Ratio, (115) * Ratio, fill=farbe, width=1)
        
        
# bei einem rechtsklick getriggert 
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
    if (int(TOPorBOT2) in (1, 2)) and (75 < event.x / Ratio < 392.5 or 407.5 < event.x / Ratio < 725) and (Würfel1[0] != 7 or Würfel2[0] != 7) and (Würfel1[0] != 0 or Würfel2[0] != 0):
        Pos2 = 13 - int(Dreieck2) if TOPorBOT2 == 1 else int(Dreieck2) + 12
        move()
        
def move():
    global Pos1, movecounter,Pos2, Pos21, Pos22, spielfeld3,White_Cap_Piece,Red_Cap_Piece
    # prüfft ob das feld was man anklickt (Pos2) mit der Possible position (Pos21 nd Pos22)übereinstimmt. Wenn ja setzt es den jewiligen würfel auf 0.
    if Pos2 == Pos21 and ((movecounter % 2 == 0 and (spielfeld2[Pos2-1] == 0 or spielfeld2[Pos2-1] == 1) and spielfeld1[Pos2-1] < 5) or
                          (movecounter % 2 != 0 and (spielfeld1[Pos2-1] == 0 or spielfeld1[Pos2-1] == 1) and spielfeld2[Pos2-1] < 5)):
        if Würfel1[1] == Würfel2[1]:
            Würfel1[0], Würfel1[1] = Würfel1[1], 0
        else:
            Würfel1[0] = 0

    elif Pos2 == Pos22 and ((movecounter % 2 == 0 and (spielfeld2[Pos2-1] == 0 or spielfeld2[Pos2-1] == 1) and spielfeld1[Pos2-1] < 5) or
                            (movecounter % 2 != 0 and (spielfeld1[Pos2-1] == 0 or spielfeld1[Pos2-1] == 1) and spielfeld2[Pos2-1] < 5)):
        if Würfel1[0] == 0 and Würfel1[1] == 0:
            Würfel2[0], Würfel2[1] = Würfel2[1], 0
        else:
            Würfel2[0] = 0

    # Prüft spielfeld3 ob die angeklickte position möglich ist 
    # zweite nedingung schaut ob die angeklickte figur eine weise figur ist und somit in spielfeld1 nicht 0 ist.
    if (spielfeld3[Pos2-1] != 0 ) and spielfeld1[Pos1-1] != 0 and White_Cap_Piece == 0:
        # zieht eine figur von der Pos1 ab 
        spielfeld1[Pos1-1] = spielfeld1[Pos1-1]-1
        # füght eine figur bei Pos2 hinzu 
        spielfeld1[Pos2-1] = spielfeld1[Pos2-1]+1
        if spielfeld3[Pos2-1] == -1:
            spielfeld2[Pos2-1] = 0
            Cap_Pieces(0)
        #setzt spielfeld3 zurück 
    elif (spielfeld3[Pos2-1] != 0 ) and spielfeld1[Pos1-1] != 0 and White_Cap_Piece != 0:
        spielfeld1[Pos2-1] = spielfeld1[Pos2-1]+1
        White_Cap_Piece = White_Cap_Piece - 1
        if spielfeld3[Pos2-1] == -1:
            
            spielfeld2[Pos2-1] = 0
            Cap_Pieces(0)
    # gleiche nur schaut nun ob das angeklickte feld rot ist 
    elif (spielfeld3[Pos2-1] != 0 ) and spielfeld2[Pos1-1] != 0 and Red_Cap_Piece == 0:
        spielfeld2[Pos1-1] = spielfeld2[Pos1-1]-1
        spielfeld2[Pos2-1] = spielfeld2[Pos2-1]+1
        if spielfeld3[Pos2-1] == -1:
            spielfeld1[Pos2-1] = 0
            Cap_Pieces(1)

    elif (spielfeld3[Pos2-1] != 0 )  and spielfeld2[Pos1-1] != 0 and Red_Cap_Piece != 0:
        spielfeld2[Pos2-1] = spielfeld2[Pos2-1]+1
        Red_Cap_Piece = Red_Cap_Piece - 1
        if spielfeld3[Pos2-1] == -1:
            spielfeld1[Pos2-1] = 0
            Cap_Pieces(1)
        
    # damit nach der Ratios() die markierung weg ist bei der angeklickten figur
    spielfeld3, Pos21, Pos22, Pos2, Pos1 = [0] * 24, 0, 0, 0, 0
    Ratios()


def Cap_Pieces(x):
    global White_Cap_Piece, Red_Cap_Piece
    if x == 0:
        Red_Cap_Piece = Red_Cap_Piece + 1 
    else:
        White_Cap_Piece = White_Cap_Piece + 1 
    Ratios()
    
def show_Cap_Piece(Ratio):
    if Red_Cap_Piece != 0:
        canvas.create_oval(175*Ratio,332.5*Ratio,225*Ratio,382.5*Ratio,fill="maroon")
    if White_Cap_Piece != 0:
        canvas.create_oval(250*Ratio,332.5*Ratio,300*Ratio,382.5*Ratio,fill="white")

#lässt einen mit "w" würfeln
def key(event):
    if event.char == "w":
        Würfel_wurf()
    elif event.char == "p":
        Pass_turn()
    

def File():
    global spielfeld1, spielfeld2, spielfeld3, movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2, Pos1, Pos2, Würfel1, Würfel2, Pos21, Pos22
    spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    #black
    spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    #white
    movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2,spielfeld3 = 1, 0, 0, 0, 0, [0]*24
    Pos1, Pos2, Pos21, Pos22 = 0, 0, 0, 0
    Würfel1, Würfel2 = [7], [7]
    Ratios()

def AI():
    pass
def PvP():
    pass
def Pass_turn():
    global Pass, movecounter, Pos1, spielfeld3, Würfel1, Würfel2
    movecounter, Würfel1, Würfel2, Pos1, spielfeld3 = movecounter + 1, [0], [0], 0, [0]*24
    Ratios()
    Pass = True


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
#!!! wenn man nach dem schlagen nicht mehr raus kann stürtzt das game ab 
#!!! einrichten von einem kreis der erscheind unten wenn eine figur geschlagen wird 
#----------> wenn man diesen kreis drückt sollen die possible positions angezeigt werden (siehe kommentar Posspible_pos)