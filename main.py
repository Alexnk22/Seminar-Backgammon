from tkinter import *
from tkinter import messagebox
import random
ai_difficulty = 3
AI = 1
movecounter = 1
TOPorBOT = 0 
TOPorBOT2 = 0
Dreieck = 0
Dreieck2 = 0
Pos1 = 0    
Pos2 = 0    
Pos3 = 0    
Pos4 = 0    
Würfel1 = [7,7]
Würfel2 = [7,8]
Pos21= -7
Pos22= -7
move_list1 = []
move_list2 = []
würfel_list1 = []
würfel_list2 = []
moves1 = []
moves2 = []
regelcounter = 0
difficulty = 2
White_winning_pos = False
Red_winning_pos = False
skip = False
Red_Cap_Piece = 0
White_Cap_Piece = 0
xx = 0
c = 0
cc = 0
move1 = 0
move2 = 0
colorbeginning = 0
root = Tk()



root.minsize(width=600,height=600)


canvas = Canvas(root,height=600, width=600)
canvas.pack(side=TOP,fill=BOTH,expand=YES)

spielfeld3 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]   
spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    
#spielfeld2 = [1,0,1,0,3,0   ,1,0,3,0,2,0       ,1,0,3,0,3,0,   1,0,1,0,1,0]    
spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    
#spielfeld1 = [0,1,0,1,0,1   ,0,1,0,1,0,2       ,0,2,0,2,0,2,   0,2,0,2,0,2]    


#spielfeld1 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,1,   0,0,3,0,0,1]
#spielfeld2 = [0,5,0,0,0,0   ,1,0,0,0,0,0       ,0,0,0,0,0,0,   0,0,0,0,0,0]

#             1 2 3 4 5 6    7 8 9 1 1 1        1 1 1 1 1 1    1 2 2 2 2 2
#            
#                       0 1 2        3 4 5 6 7 8    9 0 1 2 3 4

def Ratios (event=NONE):
    global White_Cap_Piece,Red_Cap_Piece
    if regelcounter == 0:
        canvas.delete("all")
        if root.winfo_width() < root.winfo_height():
            Ratio = root.winfo_width()/900
        else:
            Ratio = root.winfo_height()/900
        field(Ratio)
        win_progress(Ratio)
        figures(Ratio, spielfeld1, "white",12)
        figures(Ratio, spielfeld2, "maroon",12)
        if movecounter % 2 == 0 and White_Cap_Piece == 0:
                mark_mouse_pos1(Ratio,Pos1,spielfeld1,"green")
        elif movecounter % 2 != 0 and Red_Cap_Piece == 0:
            mark_mouse_pos1(Ratio,Pos1,spielfeld2,"blue")
        show_Würfel(Ratio,Würfel1,0)
        show_Würfel(Ratio,Würfel2,1)
        mark_possible_pos(Ratio, spielfeld3,"yellow",12)
        show_Cap_Piece(Ratio)
    else:
        pass
    

def field(Ratio):
    # Rahmen des spielfeldes 
    canvas.create_rectangle(55*Ratio,55*Ratio,(780)*Ratio,670*Ratio,width=2, fill="darkorange4")
    canvas.create_line(417*Ratio,55*Ratio,417*Ratio,670*Ratio,width=2)
    # Inneres Feld 
    for col in range (2):
        canvas.create_rectangle((75+col*367.5)*Ratio,75*Ratio,(392.5+col*367.5)*Ratio,650*Ratio,fill="goldenrod",width=2) 
    # Dreiecke
    for u in range (2):
        for col in range (3):
            canvas.create_polygon((col*106+75+u*369)*Ratio, 75*Ratio, (col*106+100+u*369)*Ratio, 325*Ratio, (col*106+125+u*369)*Ratio, 75*Ratio,fill="red",outline="black",)
            canvas.create_polygon((col*106+127.5+u*369)*Ratio, 75*Ratio, (col*106+152.5+u*369)*Ratio, 325*Ratio, (col*106+177.5+u*369)*Ratio, 75*Ratio)
            canvas.create_polygon((col*106+75+u*369)*Ratio, 650*Ratio, (col*106+100+u*369)*Ratio, 400*Ratio, (col*106+125+u*369)*Ratio, 650*Ratio)
            canvas.create_polygon((col*106+127.5+u*369)*Ratio, 650*Ratio, (col*106+152.5+u*369)*Ratio, 400*Ratio, (col*106+177.5+u*369)*Ratio, 650*Ratio,fill="red",outline="black")


def win_progress(Ratio):
    if White_winning_pos == True:
        # lehres feld für weiße steine 
        canvas.create_rectangle(800* Ratio,80 * Ratio,875 * Ratio,295 * Ratio, fill="darkorange4",width=2)
        canvas.create_rectangle(810* Ratio,90 * Ratio,865 * Ratio,285 * Ratio, fill="goldenrod",width=2)
        # feld auffühlen mit steinen 
        for total_white_pieces in range (15-sum(spielfeld1)):
            col = 1 if total_white_pieces > 6 else 0
            if total_white_pieces < 14:
                canvas.create_oval((810+col*27.5)*Ratio,((90+total_white_pieces*27.5)- col*27.5*7)*Ratio,(837.5+col*27.5)*Ratio,((117.5+total_white_pieces*27.5)- col*27.5*7)*Ratio, fill="white")
            if total_white_pieces == 14:
                canvas.create_rectangle(810* Ratio,90 * Ratio,865 * Ratio,285 * Ratio, fill="white")
    # selbe funktion nur für rot 
    if Red_winning_pos == True:
        canvas.create_rectangle(800* Ratio,430 * Ratio,875 * Ratio,645 * Ratio, fill="darkorange4",width=2)
        canvas.create_rectangle(810* Ratio,440 * Ratio,865 * Ratio,635 * Ratio, fill="goldenrod",width=2)
        for total_red_pieces in range (15-sum(spielfeld2)):
            col = 1 if total_red_pieces > 6 else 0
            if total_red_pieces < 14:
                canvas.create_oval((810+col*27.5)*Ratio,((607.5-total_red_pieces*27.5)+ col*27.5*7)*Ratio,(837.5+col*27.5)*Ratio,((635-total_red_pieces*27.5)+ col*27.5*7)*Ratio, fill="maroon")
            if total_red_pieces == 14:
                canvas.create_rectangle(810* Ratio,460 * Ratio,865 * Ratio,635 * Ratio, fill="maroon")


def figures(Ratio, spielfeld, color,displacement):
    # platzierung der figuren auf der unteren seite des Spielfeldes 
    for col in range(12):
        # platziert eine figur bis der pieces_count die anzahl der figuren in auf dem feld hat 
        for pieces_count in range(int(spielfeld[col])):
            # bei meht wie 5 Figuren pro Feld werden die Spielsteine versetzt plaziert
            if pieces_count > 4:
                pieces_count -= 4
                h = 1
            else:
                h = 0
            # dient zum ausgleich des Abstandes in der mitte des Feldes 
            r = 65 if col >= 6 else 15
            canvas.create_oval((723-(col*53)-r)*Ratio, (600-(pieces_count)*50+(h*25))*Ratio, 
            (773-(col*53)-r)*Ratio, (650-(pieces_count)*50+(h*25))*Ratio, fill=color, width=1.33)  
    # gleiche vorgehensweiße für die obere seite des Spielfeldes      
    for col in range(12):
        for pieces_count in range(int(spielfeld[int(col)+displacement])):
            if pieces_count > 4:
                pieces_count -= 4
                h = 1
            else:
                h = 0
            r = 50 if col >= 6 else 0
            canvas.create_oval((75+col*53+r)*Ratio, (75+pieces_count*50-(h*25))*Ratio, 
            (125+col*53+r)*Ratio, (125+pieces_count*50-(h*25))*Ratio, fill=color, width=1.33)

def Position1(event):
    global Dreieck, TOPorBOT, Pos1,Pos22,Pos21, Pos3, Pos4, spielfeld3, Pos2, movecounter, Pass, regelcounter
    if AI == 0 or (AI == 1 and movecounter %2 == 0):

        Pos21, Pos22, Pos3, Pos4 = -7, -7, 0, 0
        spielfeld3 = [0] * 24
        if root.winfo_width() < root.winfo_height():
            Ratio = root.winfo_width()/900         
        else:
            Ratio = root.winfo_height()/900
        for i in range (1,13):
            r = 50 if i > 6 else 0
            if (event.x/Ratio-27-r)//52 == i:
                Dreieck = i
        if   0 < (event.y/Ratio-75) < 250:
            TOPorBOT = 2    #oben
        elif 325 < (event.y/Ratio-75) < 575:
            TOPorBOT = 1    #unten
        else:
            TOPorBOT = 0
        if (int(TOPorBOT) in (1, 2)) and (75 < event.x / Ratio < 392.5 or 442.5 < event.x / Ratio < 760) and (Würfel1[0] != 7 or Würfel2[0] != 7) and (Würfel1[0] != 0 or Würfel2[0] != 0) :
            Pos1 = 13 - int(Dreieck) if TOPorBOT == 1 else int(Dreieck) + 12
            Pos3 = 0
            Ratios()        
            set_possibel_pos()
        elif ((392.5< event.x / Ratio < 442.5) and (290 < event.y / Ratio < 340) and Red_Cap_Piece != 0 and movecounter % 2 != 0 and (Würfel1[0] != 0 or Würfel2[0] != 0)) or ((392.5 < event.x / Ratio < 442.5) and (350 < event.y / Ratio < 400) and White_Cap_Piece != 0 and movecounter % 2 == 0 and (Würfel1[0] != 0 or Würfel2[0] != 0)):
            Pos1 = -2
            Pos3 = 1 if movecounter % 2 != 0 else 2
            Ratios()
            set_Cap_possible_pos()
            if Pos3 == 1:
                canvas.create_oval(392.5 * Ratio, 290 * Ratio, 442.5 * Ratio, 340 * Ratio, outline="blue", width=4)
            else:
                canvas.create_oval(392.5 * Ratio, 350 * Ratio, 442.5 * Ratio, 400 * Ratio, outline="green", width=4)
        else:
            Pos1,Pos2 = 0, 0
            Ratios()
        if regelcounter == 1 and  0 < event.x < 100 and 0 < event.y < 100: 
            canvas.create_rectangle(0,0,40,40,fill="red")
            regelcounter = 0
            Ratios()
        else:
            pass
    


def mark_mouse_pos1 (Ratio,Pos1,spielfeld, farbe):
        global Pos3
        if 0 < Pos1 < 13 :
            i = spielfeld[Pos1 - 1] - 4 if spielfeld[Pos1 - 1] > 4 else 0
            h = 1 if spielfeld[Pos1 - 1] > 4 else 0
            r = 15 if 6 < Pos1 < 13 else -35
            if spielfeld[Pos1-1] != 0 and spielfeld[Pos1-1] <= 5:   
                canvas.create_oval((725-(Pos1*53)-r)*Ratio, (650-(int(spielfeld[Pos1-1]))*50)*Ratio, (775-(Pos1*53)-r)*Ratio, (700-(int(spielfeld[Pos1-1]))*50)*Ratio, width=4,outline=farbe)
            elif spielfeld[Pos1-1] != 0 and spielfeld[Pos1-1] > 5:
                canvas.create_oval((725-(Pos1*53)-r)*Ratio, (650-(i)*50+(h*25))*Ratio, (775-(Pos1*53)-r)*Ratio, (700-(i)*50+(h*25))*Ratio, width=4,outline=farbe)

        elif 12 < Pos1 < 25 : 
            i = spielfeld[Pos1 - 1] - 4 if spielfeld[Pos1 - 1] > 4 else 0
            h = 1 if spielfeld[Pos1 - 1] > 4 else 0
            r = 0 if 12 < Pos1 < 19 else 50
            if spielfeld[Pos1-1] != 0 and spielfeld[Pos1-1] <= 5:
                canvas.create_oval((75+((Pos1-13)*53)+r)*Ratio, (25+int(spielfeld[Pos1-1])*50)*Ratio, (125+((Pos1-13)*53)+r)*Ratio, (75+int(spielfeld[Pos1-1])*50)*Ratio, width=4,outline=farbe)
            elif spielfeld[Pos1-1] != 0 and spielfeld[Pos1-1] > 5:
                canvas.create_oval((75+(Pos1-13)*53+r)*Ratio, (25+int(i)*50-(h*25))*Ratio, (125+(Pos1-13)*53+r)*Ratio, (75+int(i)*50-(h*25))*Ratio, width=4,outline=farbe)
        

  
def Würfel_wurf():
    global Pos21, Pos22, Pos1, movecounter, Pass, move_list1, move_list2, würfel_list1,würfel_list2, xx, c, skip, cc 
    xx = 0
    c = 0
    cc = 0
    if ((Würfel1[0] == 0 and Würfel2[0] == 0) or (Würfel1[0] == 7 and Würfel2[0] == 7) or skip == True) and movecounter != 0:
        if movecounter == 1:
            movecounter = 2
        if skip == True:
            movecounter = movecounter + 1
        
        if Pos21 > 24:
            Pos21 = -7
        if Pos22 > 24:
            Pos22 = -7
        spielfeld3[Pos21 - 1] = spielfeld3[Pos22 - 1] = 0
        Würfel1.clear()
        Würfel2.clear()
        a, b = random.randint(1, 6), random.randint(1, 6)
        if a == b:
            Würfel1.extend([a, a])
            Würfel2.extend([b, b])
        else:
            Würfel1.extend([a, 7])
            Würfel2.extend([b, 8])
        moves1.clear()
        moves2.clear()
        move_list1.extend(spielfeld1)
        move_list2.extend(spielfeld2) 
        würfel_list1.extend(Würfel1)
        würfel_list2.extend(Würfel2)
        skip = False
        if AI == 1:    
            fish_moves()
        Ratios()
        disable_starter()
        disable_difficulty()
        

   
def show_Würfel(Ratio, würfel_list, ver):
    
    if movecounter % 2 == 0:
        for i in range(9):
            if würfel_list[0] == i and 0 < i < 7:
                canvas.create_rectangle((550+ver*80)*Ratio, 336*Ratio, (600+ver*80)*Ratio, 386*Ratio, width=1.4,fill="white")
                if i == 1 or i == 3 or i == 5:
                    canvas.create_oval((570+ver*80) * Ratio, 355 * Ratio, (580+ver*80) * Ratio, 365 * Ratio, fill="black")
                for u in range(2):
                    if 1 < i < 7:
                        canvas.create_oval(((u*34)+553+ver*80) * Ratio, ((u*35)+338) * Ratio, ((u*34)+563+ver*80) * Ratio, ((u*35)+348) * Ratio, fill="black")
                    if 3 < i < 7:
                        canvas.create_oval(((u*34)+553+ver*80) * Ratio, (373-(35*u)) * Ratio, ((u*34)+563+ver*80) * Ratio, (383-(35*u)) * Ratio, fill="black")
                    if i == 6:
                        canvas.create_oval(((u*34)+553+ver*80) * Ratio, 355 * Ratio, ((u*34)+563+ver*80) * Ratio, 365 * Ratio, fill="black")
            if  würfel_list[1] == i and 0 < i < 7:
                canvas.create_rectangle((480+ver*220)*Ratio, 336*Ratio, (530+ver*220)*Ratio,386*Ratio, width=1.4,fill="white")
                if i == 1 or i == 3 or i == 5:
                    canvas.create_oval((500+ver*220) * Ratio, 355 * Ratio, (510+ver*220) * Ratio, 365 * Ratio, fill="black")
                for u in range(2):
                    if 1 < i < 7:
                        canvas.create_oval(((u*34)+483+ver*220) * Ratio, ((u*35)+338) * Ratio, ((u*34)+493+ver*220) * Ratio, ((u*35)+348) * Ratio, fill="black")
                    if 3 < i < 7:
                        canvas.create_oval(((u*34)+483+ver*220) * Ratio, (373-(35*u)) * Ratio, ((u*34)+493+ver*220) * Ratio, (383-(35*u)) * Ratio, fill="black")
                    if i == 6:
                        canvas.create_oval(((u*34)+483+ver*220) * Ratio, 355 * Ratio, ((u*34)+493+ver*220) * Ratio, 365 * Ratio, fill="black")
    else:
        for i in range(9):
            if würfel_list[0] == i and 0 < i < 7:
                canvas.create_rectangle((150+ver*80)*Ratio, 336*Ratio, (200+ver*80)*Ratio, 386*Ratio, width=1.4,fill="maroon")
                if i == 1 or i == 3 or i == 5:
                    canvas.create_oval((170+ver*80) * Ratio, 355 * Ratio, (180+ver*80) * Ratio, 365 * Ratio, fill="black")
                for u in range(2):
                    if 1 < i < 7:
                        canvas.create_oval(((u*34)+153+ver*80) * Ratio, ((u*35)+338) * Ratio, ((u*34)+163+ver*80) * Ratio, ((u*35)+348) * Ratio, fill="black")
                    if 3 < i < 7:
                        canvas.create_oval(((u*34)+153+ver*80) * Ratio, (373-(35*u)) * Ratio, ((u*34)+163+ver*80) * Ratio, (383-(35*u)) * Ratio, fill="black")
                    if i == 6:
                        canvas.create_oval(((u*34)+153+ver*80) * Ratio, 355 * Ratio, ((u*34)+163+ver*80) * Ratio, 365 * Ratio, fill="black")
            if  würfel_list[1] == i and 0 < i < 7:
                canvas.create_rectangle((80+ver*220)*Ratio, 336*Ratio, (130+ver*220)*Ratio,386*Ratio, width=1.4,fill="maroon")
                if i == 1 or i == 3 or i == 5:
                    canvas.create_oval((100+ver*220) * Ratio, 355 * Ratio, (110+ver*220) * Ratio, 365 * Ratio, fill="black")
                for u in range(2):
                    if 1 < i < 7:
                        canvas.create_oval(((u*34)+83+ver*220) * Ratio, ((u*35)+338) * Ratio, ((u*34)+93+ver*220) * Ratio, ((u*35)+348) * Ratio, fill="black")
                    if 3 < i < 7:
                        canvas.create_oval(((u*34)+83+ver*220) * Ratio, (373-(35*u)) * Ratio, ((u*34)+93+ver*220) * Ratio, (383-(35*u)) * Ratio, fill="black")
                    if i == 6:
                        canvas.create_oval(((u*34)+83+ver*220) * Ratio, 355 * Ratio, ((u*34)+93+ver*220) * Ratio, 365 * Ratio, fill="black")


def set_Cap_possible_pos():
    global Pos21, Pos22,White_Cap_Piece,Red_Cap_Piece, Pos3 
    spielfeld3[Pos21 - 1] = spielfeld3[Pos22 - 1] = 0
    if (White_Cap_Piece != 0 and Pos3 == 2 and movecounter % 2 == 0) or (Red_Cap_Piece != 0 and Pos3 == 1 and movecounter % 2 != 0):
        if Pos3 == 2:
            Pos21 = Würfel1[0]
            Pos22 = Würfel2[0]
            spielfeld = spielfeld1 
            spielfeldx = spielfeld2 
        elif Pos3 == 1:
            Pos21 = 25 - Würfel1[0]
            Pos22 = 25 - Würfel2[0]
            spielfeld = spielfeld2 
            spielfeldx = spielfeld1
        if 0 < Pos21 < 25:
                if spielfeldx[Pos21 - 1] == 0  and Würfel1[0] != 0:
                    spielfeld3[Pos21 - 1] = spielfeld[Pos21 - 1] + 1
                elif spielfeldx[Pos21 - 1] == 1 and spielfeld[Pos21 - 1] == 0 and Würfel1[0] != 0:
                    spielfeld3[Pos21 - 1] = -1
        if 0 < Pos22 < 25:
            if spielfeldx[Pos22 - 1] == 0  and Würfel2[0] != 0:
                    spielfeld3[Pos22 - 1] = spielfeld[Pos22 - 1] + 1
            elif spielfeldx[Pos22 - 1] == 1 and spielfeld[Pos22 - 1] == 0 and Würfel2[0] != 0:
                    spielfeld3[Pos22 - 1] = -1
        Ratios()       

                  
def set_possibel_pos():
    global Pos21, Pos22,White_Cap_Piece,Red_Cap_Piece, Pos3
    spielfeld3[Pos21 - 1] = spielfeld3[Pos22 - 1] = 0
    if spielfeld1[Pos1 - 1] != 0 and movecounter % 2 == 0 and White_Cap_Piece == 0:
        Pos21 = Pos1 + Würfel1[0]
        Pos22 = Pos1 + Würfel2[0]
        if 0 < Pos21 < 25:
            if spielfeld2[Pos21 - 1] == 0  and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld1[Pos21 - 1] + 1
            elif spielfeld2[Pos21 - 1] == 1 and spielfeld1[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1
        if 0 < Pos22 < 25:
            if spielfeld2[Pos22 - 1] == 0  and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld1[Pos22 - 1] + 1
            elif spielfeld2[Pos22 - 1] == 1 and spielfeld1[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()
    elif spielfeld2[Pos1 - 1] != 0 and movecounter % 2 != 0 and Red_Cap_Piece == 0:
        Pos21 = Pos1 - Würfel1[0]
        Pos22 = Pos1 - Würfel2[0]

        if 0 < Pos21 < 25:
            if spielfeld1[Pos21 - 1] == 0  and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = spielfeld2[Pos21 - 1] + 1
            elif spielfeld1[Pos21 - 1] == 1 and spielfeld2[Pos21 - 1] == 0 and Würfel1[0] != 0:
                spielfeld3[Pos21 - 1] = -1

        if 0 < Pos22 < 25:
            if spielfeld1[Pos22 - 1] == 0  and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = spielfeld2[Pos22 - 1] + 1
            elif spielfeld1[Pos22 - 1] == 1 and spielfeld2[Pos22 - 1] == 0 and Würfel2[0] != 0:
                spielfeld3[Pos22 - 1] = -1
        Ratios()
    

def mark_possible_pos(Ratio,spielfeld,farbe,verschiebung):
    global Pos4, difficulty
    for u in range(12):
        r = 15 if u >= 6 else -35
        if spielfeld[u] != -1 and spielfeld[u] != 0 and spielfeld[u] <= 5:
            canvas.create_oval((673 - (u * 53) - r) * Ratio, (600 - (spielfeld[u]-1) * 50) * Ratio, (723 - (u * 53) - r) * Ratio, (650 - (spielfeld[u]-1) * 50) * Ratio, fill=farbe, width=1)
        elif spielfeld[u] != -1 and spielfeld[u] != 0 and spielfeld[u] > 5:
            i = spielfeld[u] - 4 
            h = 1
            canvas.create_oval((673-(u*53)-r)*Ratio, (650-(i)*50+(h*25))*Ratio, (723-(u*53)-r)*Ratio, (700-(i)*50+(h*25))*Ratio, fill=farbe, width=1)
        elif spielfeld[u] == -1:
            canvas.create_oval((683 - (u * 53) - r) * Ratio, (610) * Ratio, (713 - (u * 53) - r) * Ratio, (640) * Ratio, fill=farbe, width=1)
    for u in range(12):
        r = 50 if u >= 6 else 0 
        if spielfeld[u + verschiebung] != -1 and spielfeld[u+verschiebung] != 0 and spielfeld[u+verschiebung] <= 5:
            canvas.create_oval((75 + u * 53 + r) * Ratio, (75 + (spielfeld[u+verschiebung]-1) * 50) * Ratio, (125 + u * 53 + r) * Ratio, (125 + (spielfeld[u+verschiebung]-1) * 50) * Ratio, fill=farbe, width=1)
        elif spielfeld[u+ verschiebung] != -1 and spielfeld[u+ verschiebung] != 0 and spielfeld[u+ verschiebung] > 5:          
            i = spielfeld[u+verschiebung] - 4 
            h = 1
            canvas.create_oval((75+u*53+r)*Ratio, (25+i*50-(h*25))*Ratio, (125+u*53+r)*Ratio, (75+i*50-(h*25))*Ratio, fill=farbe, width=1)
        elif spielfeld[u + verschiebung] == -1:
            canvas.create_oval((85 + u * 53 + r) * Ratio, (85) * Ratio, (115 + u * 53 + r) * Ratio, (115) * Ratio, fill=farbe, width=1)

    if difficulty == 1:
        if White_winning_pos == True and (Pos21 > 24 or Pos22 > 24)and Pos1 != 0 and movecounter % 2 == 0:
            canvas.create_rectangle(800* Ratio,80 * Ratio,875 * Ratio,295 * Ratio,outline="yellow",width=4)
            Pos4 = 1
        elif Red_winning_pos == True and ( -6 < Pos21 < 1 or -6 < Pos22 < 1) and Pos1 != 0 and movecounter % 2 != 0:    
            canvas.create_rectangle(800* Ratio,430 * Ratio,875 * Ratio,645 * Ratio, outline="yellow",width=5)
            Pos4 = 2
    elif difficulty == 2 or difficulty == 3:
        if White_winning_pos == True and (Pos21 == 25 or Pos22 == 25)and Pos1 != 0 and movecounter % 2 == 0:
            canvas.create_rectangle(800* Ratio,80 * Ratio,875 * Ratio,295 * Ratio,outline="yellow",width=4)
            Pos4 = 1
        elif Red_winning_pos == True and (Pos21 == 0 or Pos22 == 0) and Pos1 != 0 and movecounter % 2 != 0:    
            canvas.create_rectangle(800* Ratio,430 * Ratio,875 * Ratio,645 * Ratio, outline="yellow",width=5)
            Pos4 = 2


def Position2(event=NONE):
    global Dreieck2, TOPorBOT2, Pos2, Pos1, Pos4    
    if root.winfo_width() < root.winfo_height():
        Ratio = root.winfo_width()/900         
    else:
        Ratio = root.winfo_height()/900
    for i in range (1,13):
        r = 50 if i > 6 else 0
        if (event.x/Ratio-27-r)//52 == i:
            Dreieck2 = i
    if   0 < (event.y/Ratio-75) < 250:
        TOPorBOT2 = 2    #oben
    elif 325 < (event.y/Ratio-75) < 575:
        TOPorBOT2 = 1    #unten
    else:
        TOPorBOT2 = 0
    if (int(TOPorBOT2) in (1, 2)) and (75 < event.x / Ratio < 392.5 or 442.5 < event.x / Ratio < 760) and (Würfel1[0] != 7 or Würfel2[0] != 7) and (Würfel1[0] != 0 or Würfel2[0] != 0):
        Pos2 = 13 - int(Dreieck2) if TOPorBOT2 == 1 else int(Dreieck2) + 12
        pasch()
        move()
    
    if (800 < event.x / Ratio < 875) and (80 < event.y/Ratio < 275) and White_winning_pos == True  and (Würfel1[0] != 0 or Würfel2[0] != 0) and Pos4 == 1:
        Pos2 = -1
        spielfeld1[Pos1-1] = spielfeld1[Pos1-1]-1
        if difficulty == 1:
            if Pos21 > 24:
                if Würfel1[1] == Würfel2[1]:
                    Würfel1[0], Würfel1[1] = Würfel1[1], 0
                else:
                    Würfel1[0] = 0
            else:
                if Würfel1[0] == 0 and Würfel1[1] == 0:
                    Würfel2[0], Würfel2[1] = Würfel2[1], 0
                else:
                    Würfel2[0] = 0
        if difficulty == 2 or difficulty == 3:
            if Pos21 == 25:
                if Würfel1[1] == Würfel2[1]:
                    Würfel1[0], Würfel1[1] = Würfel1[1], 0
                else:
                    Würfel1[0] = 0
            else:
                if Würfel1[0] == 0 and Würfel1[1] == 0:
                    Würfel2[0], Würfel2[1] = Würfel2[1], 0
                else:
                    Würfel2[0] = 0

        Ratios() 
        move()
    if (800 < event.x / Ratio < 875) and (450 < event.y /Ratio < 645) and Red_winning_pos ==True and (Würfel1[0] != 0 or Würfel2[0] != 0) and Pos4 == 2 : 
        Pos2 = -1
        spielfeld2[Pos1-1] = spielfeld2[Pos1-1]-1
        if difficulty == 1:
            if -6 < Pos21 < 0:     
                if Würfel1[1] == Würfel2[1]:
                    Würfel1[0], Würfel1[1] = Würfel1[1], 0
                else:
                    Würfel1[0] = 0    
            else:
                if Würfel1[0] == 0 and Würfel1[1] == 0:
                    Würfel2[0], Würfel2[1] = Würfel2[1], 0
                else:
                    Würfel2[0] = 0     
        if difficulty == 2 or difficulty == 3:
            if -6 < Pos21 < 0:     
                if Würfel1[1] == Würfel2[1]:
                    Würfel1[0], Würfel1[1] = Würfel1[1], 0
                else:
                    Würfel1[0] = 0    
            else:
                if Würfel1[0] == 0 and Würfel1[1] == 0:
                    Würfel2[0], Würfel2[1] = Würfel2[1], 0
                else:
                    Würfel2[0] = 0 

        Ratios() 
        move()

def pasch():
    global Pos1, movecounter,Pos2, Pos21, Pos22, spielfeld3,White_Cap_Piece,Red_Cap_Piece, Pos3
    if Pos2 == Pos21 and ((movecounter % 2 == 0 and (spielfeld2[Pos2-1] == 0 or spielfeld2[Pos2-1] == 1) ) or (movecounter % 2 != 0 and (spielfeld1[Pos2-1] == 0 or spielfeld1[Pos2-1] == 1) )):
        if Würfel1[1] == Würfel2[1]:
            Würfel1[0], Würfel1[1] = Würfel1[1], 0
        else:
            Würfel1[0] = 0
    elif Pos2 == Pos22 and ((movecounter % 2 == 0 and (spielfeld2[Pos2-1] == 0 or spielfeld2[Pos2-1] == 1) ) or(movecounter % 2 != 0 and (spielfeld1[Pos2-1] == 0 or spielfeld1[Pos2-1] == 1) )):
        if Würfel1[0] == 0 and Würfel1[1] == 0:
            Würfel2[0], Würfel2[1] = Würfel2[1], 0
        else:
            Würfel2[0] = 0

def move():
    global Pos1, movecounter,Pos2, Pos21, Pos22, spielfeld3,White_Cap_Piece,Red_Cap_Piece, Pos3, Pos4, backcounter
   
    if spielfeld3[Pos2-1] != 0 and ((Pos3 == 2 and White_Cap_Piece != 0) or (Pos3 == 1 and Red_Cap_Piece != 0)):
        spielfeld = spielfeld1 if Pos3 == 2 else spielfeld2
        spielfeldx = spielfeld2 if Pos3 == 2 else spielfeld1
        spielfeld[Pos2 - 1] += 1
        if Pos3 == 2:
            White_Cap_Piece = White_Cap_Piece - 1
        else:
            Red_Cap_Piece = Red_Cap_Piece - 1 
        if spielfeld3[Pos2-1] == -1:
            spielfeldx[Pos2-1] = 0
            if spielfeld == spielfeld1:
                Cap_Pieces(0)
            else:
                Cap_Pieces(1)

    elif spielfeld3[Pos2 - 1] != 0 and ((spielfeld1[Pos1 - 1] != 0 and White_Cap_Piece == 0) or (spielfeld2[Pos1 - 1] != 0 and Red_Cap_Piece == 0)):
        spielfeld = spielfeld1 if spielfeld1[Pos1 - 1] != 0 else spielfeld2
        spielfeldx = spielfeld2 if spielfeld1[Pos1 - 1] != 0 else spielfeld1
        spielfeld[Pos1 - 1] -= 1
        spielfeld[Pos2 - 1] += 1
        if spielfeld3[Pos2 - 1] == -1:
            spielfeldx[Pos2 - 1] = 0
            if spielfeld == spielfeld1:
                Cap_Pieces(0)
            else:
                Cap_Pieces(1)
    if Würfel1[0] == 0 and Würfel2[0] == 0:
        movecounter = movecounter +1
        if AI == 1 and movecounter % 2 != 0:
            Würfel_wurf()

    spielfeld3, Pos21, Pos22, Pos2, Pos1, Pos3, Pos4 = [0] * 24, -7, -7, 0, 0, 0, 0       
    Check_winning_pos()
    winner()
    Ratios()

def Cap_Pieces(x):
    global White_Cap_Piece, Red_Cap_Piece
    if x == 0:
        Red_Cap_Piece = Red_Cap_Piece + 1 
    else:
        White_Cap_Piece = White_Cap_Piece + 1 
    Ratios()


def show_Cap_Piece(Ratio):
    for i in range(Red_Cap_Piece):
        if i < 6:
            canvas.create_oval(392.5 * Ratio, (290 - 50 * i) * Ratio, 442.5 * Ratio, (340 - 50 * i) * Ratio, fill="maroon")
        else:
            canvas.create_oval(392.5 * Ratio, (290 - 50 * 5) * Ratio, 442.5 * Ratio, (340 - 50 * 5) * Ratio, fill="maroon")
    for i in range(White_Cap_Piece):
        if i < 6:
            canvas.create_oval(392.5 * Ratio, (350 + 50 * i) * Ratio, 442.5 * Ratio, (400 + 50 * i) * Ratio, fill="white")
        else:
            canvas.create_oval(392.5 * Ratio, (350 + 50 * 5) * Ratio, 442.5 * Ratio, (400 + 50 * 5) * Ratio, fill="white")

def Back_move():
        global spielfeld1, AI, spielfeld2, skip, move_list1, move_list2,spielfeld3, Würfel1, Würfel2, würfel_list1, würfel_list2, movecounter, backcounter,White_Cap_Piece,Red_Cap_Piece, c ,cc ,xx 
        xx = c = xx = 0
        if movecounter != 0 and movecounter != 1:
            if AI == 0:
                if (Würfel1[0] != 0 and Würfel2[0] != 0):
                    move_list1 = move_list1[:-24]
                    move_list2 = move_list2[:-24]
                    würfel_list1 = würfel_list1[:-2]
                    würfel_list2 = würfel_list2[:-2]
                if (Würfel1[0] == 0 and Würfel2[0] == 0) or (Würfel1[0] != 0 and Würfel2[0] != 0):
                    movecounter = movecounter - 1   
                spielfeld1 = move_list1[-24:]
                spielfeld2 = move_list2[-24:]
                Würfel1 = würfel_list1[-2:]
                Würfel2 = würfel_list2[-2:]
                for i in range (15):
                    if 15-int(sum(spielfeld1)) == i and Red_winning_pos == False:
                        White_Cap_Piece = i
                    if 15-int(sum(spielfeld2)) == i and Red_winning_pos == False:
                        Red_Cap_Piece = i  
                spielfeld3 = 24*[0]
                Check_winning_pos()
                Ratios()
            else:
                if skip == True:
                    move_list1 = move_list1[:-24]
                    move_list2 = move_list2[:-24]
                    würfel_list1 = würfel_list1[:-2]
                    würfel_list2 = würfel_list2[:-2]
                    spielfeld1 = move_list1[-24:]
                    spielfeld2 = move_list2[-24:]
                    Würfel1 = würfel_list1[-2:]
                    Würfel2 = würfel_list2[-2:]
                    movecounter = movecounter - 1 
                    for i in range (15):
                        if 15-int(sum(spielfeld1)) == i and Red_winning_pos == False:
                            White_Cap_Piece = i
                        if 15-int(sum(spielfeld2)) == i and Red_winning_pos == False:
                            Red_Cap_Piece = i  
                    spielfeld3 = 24*[0]
                    skip = False
                    Check_winning_pos()
                    Ratios()
                else:

                    if (Würfel1[0] == 0 and Würfel2[0] == 0) or (Würfel1[0] != 0 and Würfel2[0] != 0) and movecounter > 2:
                        move_list1 = move_list1[:-24]
                        move_list2 = move_list2[:-24]
                        würfel_list1 = würfel_list1[:-2]
                        würfel_list2 = würfel_list2[:-2]
                        spielfeld1 = move_list1[-24:]
                        spielfeld2 = move_list2[-24:]
                        Würfel1 = würfel_list1[-2:]
                        Würfel2 = würfel_list2[-2:]
                        movecounter = movecounter - 1 
                        for i in range (15):
                            if 15-int(sum(spielfeld1)) == i and Red_winning_pos == False:
                                White_Cap_Piece = i
                            if 15-int(sum(spielfeld2)) == i and Red_winning_pos == False:
                                Red_Cap_Piece = i  
                        spielfeld3 = 24*[0]
                        skip = True
                        Back_move()

                    else:
                        spielfeld1 = move_list1[-24:]
                        spielfeld2 = move_list2[-24:]
                        Würfel1 = würfel_list1[-2:]
                        Würfel2 = würfel_list2[-2:]
                        
                        for i in range (15):
                            if 15-int(sum(spielfeld1)) == i and Red_winning_pos == False:
                                White_Cap_Piece = i
                            if 15-int(sum(spielfeld2)) == i and Red_winning_pos == False:
                                Red_Cap_Piece = i  
                        spielfeld3 = 24*[0]
                        
                        Check_winning_pos()
                        Ratios()

          
def winner():
    if all(x == 0 for x in spielfeld1[18:25]) and White_winning_pos == True:
        messagebox.showinfo("", "Weiß Gewinnt")
        File()
        
    if all(x == 0 for x in spielfeld2[:7]) and Red_winning_pos == True:
        messagebox.showinfo("", "Rot Gewinnt")
        File()
        

def key(event):
    global backcounter,spielfeld2,spielfeld1,movecounter,TOPorBOT,TOPorBOT2,Dreieck,Dreieck2,spielfeld3,Pos1,Pos2,Pos21,Pos22,Pos3,Pos4,Red_Cap_Piece,White_Cap_Piece,Red_winning_pos,White_winning_pos,Würfel1,Würfel2
    if event.char == "w":
        Würfel_wurf()
    elif event.char == "p":
        Pass_turn()
    elif event.char == "z":
        Back_move()
    elif event.char == "ü":
        spielfeld2 = [2,0,0,0,0,5   ,0,3,0,0,0,5       ,0,0,0,0,0,0,   0,0,0,0,0,0]    #black
        spielfeld1 = [0,0,0,0,0,0   ,0,0,0,0,0,0       ,0,0,0,0,0,1,   6,4,3,0,1,0]    #white

        movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2,spielfeld3 = 1, 0, 0, 0, 0, [0]*24,
        Pos1, Pos2, Pos21, Pos22, Pos3, Pos4 = 0, 0, -7, -7, 0, 0
        Red_Cap_Piece = 0
        White_Cap_Piece = 0
        Red_winning_pos = False
        White_winning_pos = False
        Würfel1, Würfel2 = [7,7], [7,8]
        Ratios()

def File():
    global spielfeld1, spielfeld2, spielfeld3, movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2, Pos1, Pos2, Würfel1, Würfel2, Pos21, Pos22, Pos3, Pos4, White_Cap_Piece, Red_Cap_Piece, Red_winning_pos, White_winning_pos
    if movecounter != 0:
        spielfeld2 = [0,0,0,0,0,5   ,0,3,0,0,0,0       ,5,0,0,0,0,0,   0,0,0,0,0,2]    #black
        spielfeld1 = [2,0,0,0,0,0   ,0,0,0,0,0,5       ,0,0,0,0,3,0,   5,0,0,0,0,0]    #white
        movecounter, TOPorBOT, TOPorBOT2, Dreieck, Dreieck2,spielfeld3 = 1, 0, 0, 0, 0, [0]*24,
        Pos1, Pos2, Pos21, Pos22, Pos3, Pos4 = 0, 0, -7, -7, 0, 0
        Red_Cap_Piece = 0
        White_Cap_Piece = 0
        Red_winning_pos = False
        White_winning_pos = False
        Würfel1, Würfel2 = [7,7], [7,8]
        mein_menu.entryconfig("Starter", state="normal")
        mein_menu.entryconfig("Difficulty", state="normal")
        Ratios()
    else:
        pass

def Ai():
    global AI 
    AI = 1
    Game_mode_menu.entryconfig("Player vs. AI", state="disabled")
    Game_mode_menu.entryconfig("Player  vs. Player", state="normal")

def PvP():
    global AI
    AI = 0
    Game_mode_menu.entryconfig("Player  vs. Player", state="disabled")
    Game_mode_menu.entryconfig("Player vs. AI", state="normal")

def Pass_turn():
    global Pass, movecounter, Pos1, spielfeld3, Würfel1, Würfel2, Pos4, c , xx ,cc
    if movecounter != 0:
        for i in range (15):
            if 15-int(sum(spielfeld1)) == i and Red_winning_pos == False:
                White_Cap_Piece = i
            if 15-int(sum(spielfeld2)) == i and Red_winning_pos == False:
                Red_Cap_Piece = i  
        movecounter, Würfel1, Würfel2, Pos1, spielfeld3, Pos4 = movecounter + 1, [0,7], [0,8], 0, [0]*24, 0
        xx = c = xx = 0
        Ratios()
        
    else:
        pass

def Check_winning_pos():
    global White_winning_pos, Red_winning_pos, spielfeld1, spielfeld2
    if all(x == 0 for x in spielfeld1[:18]) and White_Cap_Piece == 0:
        White_winning_pos = True
    else:
        White_winning_pos = False
        
    if all(x == 0 for x in spielfeld2[6:25]) and Red_Cap_Piece == 0:
        Red_winning_pos = True 
    else:
        Red_winning_pos = False

def disable_starter():
    if movecounter > 1:
        mein_menu.entryconfig("Starter", state="disabled")

def starter2():
    global movecounter, Pass
    movecounter = 3
    movecounter_menu.entryconfig("Red", state="disabled")
    movecounter_menu.entryconfig("white", state="normal")
    Ratios()
    Pass = True

def starter1():
    global movecounter,Pass
    movecounter = 2 
    movecounter_menu.entryconfig("white", state="disabled")
    movecounter_menu.entryconfig("Red", state="normal")
    Ratios()
    Pass = True



def show_regeln():
    global regelcounter, Pos22, Pos21, Pos2, Pos1
    if regelcounter == 0:
        canvas.delete("all")
        Pos1,Pos2,Pos21,Pos22 = 0,0,-1,-1
        regelcounter = 1 
        spielregeln_text = """
                                                            Backgammon Regeln


        Gespielt wird Backgammon mit zwei sechsseitigen würfeln und einem Spielbrett 
        bestehend aus 24 Dreiecken mit jeweils 12 Dreiecken pro Seite. Die Ausgangs-
        position gibt die Position der 15 weißen und 15 schwarzen Figuren fest vor. 
        Die weißen Spielsteine bewegen sich im Uhrzeigersinn, während die schwarzen 
        Spielsteine entgegen dem Uhrzeigersinn ziehen. Die Augenzahl der Würfel wird 
        einzeln und nacheinander gefahren und bei einem Pasch darf mit jedem Würfel 
        die entsprechende Augenzahl zwei Mal gefahren werden. Es darf nur auf 
        Positionen gezogen werden, wo entweder maximal eine Figur der gegnerischen 
        Farbe steht oder unbegrenzt viele Figuren der eigenen Farbe platziert sind. 
        Alleinstehende Figuren können von einer gegnerischen Figur geschlagen werden 
        und werden in die Mitte des Spielbrettes befördert. Geschlagene Figuren starten 
        wieder vom Anfang und müssen, sofern möglich, im nächsten Zug wieder in das 
        Spielfeld zurückgebracht werden. Wenn dies nicht möglich ist, muss eine Runde 
        ausgesetzt werden. Sobald sich alle Figuren einer Farbe auf den letzten 6 Feldern 
        seiner Laufbahn befinden, beginnt für diesen Spieler das „Rauswürfeln“. Hierbei 
        darf eine Figur auf das 25te bzw. 0te Feld gezogen werden und wird dadurch aus 
        dem spiel genommen. Das Spiel ist gewonnen so bald alle 15 Figuren eines Spielers 
        auf diese Art von dem Spielfeld beseitigt wurden. 

        [w]-Taste drücken zum Würfeln 

        [p]-Taste drücken um einen Zug auszusetzen 
        
        [z]-Taste drücken um einen Zug zurück zu gehen
        """

        canvas.create_text(0, 10, anchor=NW, text=spielregeln_text, font=("Helvetica", 12))
        canvas.create_rectangle(0,0,40,40,fill="")
        canvas.create_line(30,10,10,20,width=2)
        canvas.create_line(30,30,10,20,width=2)
    elif regelcounter == 1:
        regelcounter = 0
        Ratios()
difficultycounter = 0

def easy():
    global difficulty, difficultycounter
    difficulty = 1
    difficulty_menu.entryconfig("Easy ",state="disabled")
    difficulty_menu.entryconfig("Hard",state="normal")
    difficultycounter = 1


def hard():
    global difficulty, difficultycounter
    difficulty = 3

    difficulty_menu.entryconfig("Easy ",state="normal")
    difficulty_menu.entryconfig("Hard",state="disabled")
    difficultycounter = 1
    

def disable_difficulty():
    if movecounter > 1:
        mein_menu.entryconfig("Difficulty", state="disabled")
        
def ai_difficulty1():
    global ai_difficulty
    ai_difficulty = 1
def ai_difficulty2():
    global ai_difficulty
    ai_difficulty = 2
def ai_difficulty3():
    global ai_difficulty
    ai_difficulty = 3


def fish_moves():
    if movecounter % 2 == 0:
        if White_Cap_Piece == 0:
            if White_winning_pos == False:
                for i in range (24):
                    if spielfeld1[i] != 0:
                        if Würfel1[0]+i+1 < 25:
                            if(spielfeld2[Würfel1[0]+i] == 0 or spielfeld2[Würfel1[0]+i] == 1) :
                                moves1.append(Würfel1[0]+i+1)
                        if Würfel2[0]+i+1 < 25:
                            if (spielfeld2[Würfel2[0]+i] == 0 or spielfeld2[Würfel2[0]+i] == 1):
                                moves2.append(Würfel2[0]+i+1)
            elif White_winning_pos == True and difficulty == 1:
                for i in range (24):
                    if spielfeld1[i] != 0:
                        if Würfel1[0]+i+1 < 25:
                            if(spielfeld2[Würfel1[0]+i] == 0 or spielfeld2[Würfel1[0]+i] == 1) :
                                moves1.append(Würfel1[0]+i+1)
                        else:
                            moves1.append(25)
                        if Würfel2[0]+i+1 < 25:
                            if (spielfeld2[Würfel2[0]+i] == 0 or spielfeld2[Würfel2[0]+i] == 1):
                                moves2.append(Würfel2[0]+i+1)
                        else:
                            moves2.append(25)
            elif White_winning_pos == True and (difficulty == 2 or difficulty == 3):
                for i in range (24):
                    if spielfeld1[i] != 0:
                        if Würfel1[0]+i+1 < 25:
                            if(spielfeld2[Würfel1[0]+i] == 0 or spielfeld2[Würfel1[0]+i] == 1) :
                                moves1.append(Würfel1[0]+i+1)
                        elif Würfel1[0]+i+1 == 25:
                            moves1.append(25)
                        if Würfel2[0]+i+1 < 25:
                            if (spielfeld2[Würfel2[0]+i] == 0 or spielfeld2[Würfel2[0]+i] == 1):
                                moves2.append(Würfel2[0]+i+1)
                        elif Würfel2[0]+i+1 == 25:
                            moves2.append(25)
        elif White_Cap_Piece != 0:
            if(spielfeld2[Würfel1[0]-1] == 0 or spielfeld2[Würfel1[0]-1] == 1):
                moves1.append(Würfel1[0])
            if(spielfeld2[Würfel2[0]-1] == 0 or spielfeld2[Würfel2[0]-1] == 1):
                moves2.append(Würfel2[0])

    else:
        if Red_Cap_Piece == 0:
            if Red_winning_pos == False:
                for i in range (24):
                    if spielfeld2[i] != 0:
                        if i+1-Würfel1[0] > 0:
                            if (spielfeld1[i-Würfel1[0]] == 0 or spielfeld1[i-Würfel1[0]] == 1) :
                                moves1.append(1+i-Würfel1[0])
                        if i+1-Würfel2[0] > 0:
                            if (spielfeld1[i-Würfel2[0]] == 0 or spielfeld1[i-Würfel2[0]] == 1) :
                                moves2.append(1+i-Würfel2[0])
            elif Red_winning_pos == True and difficulty == 1:
                for i in range (24):
                    if spielfeld2[i] != 0:
                        if i+1-Würfel1[0] > 0:
                            if (spielfeld1[i-Würfel1[0]] == 0 or spielfeld1[i-Würfel1[0]] == 1) :
                                moves1.append(1+i-Würfel1[0])
                        else:
                            moves1.append(0)
                        if i+1-Würfel2[0] > 0:
                            if (spielfeld1[i-Würfel2[0]] == 0 or spielfeld1[i-Würfel2[0]] == 1) :
                                moves2.append(1+i-Würfel2[0])
                        else: 
                            moves2.append(0)
            elif Red_winning_pos == True and (difficulty == 2 or difficulty == 3):
                for i in range (24):
                    if spielfeld2[i] != 0:
                        if i+1-Würfel1[0] > 0:
                            if (spielfeld1[i-Würfel1[0]] == 0 or spielfeld1[i-Würfel1[0]] == 1) :
                                moves1.append(1+i-Würfel1[0])
                        elif i+1-Würfel1[0] == 0:
                            moves1.append(0)
                        if i+1-Würfel2[0] > 0:
                            if (spielfeld1[i-Würfel2[0]] == 0 or spielfeld1[i-Würfel2[0]] == 1) :
                                moves2.append(1+i-Würfel2[0])
                        elif i+1-Würfel2[0] == 0:
                            moves2.append(0)
        elif Red_Cap_Piece != 0:
            if(spielfeld1[24-Würfel1[0]] == 0 or spielfeld1[24-Würfel1[0]] == 1):
                moves1.append(25-Würfel1[0])
            if(spielfeld1[24-Würfel2[0]] == 0 or spielfeld1[24-Würfel2[0]] == 1):
                moves2.append(25-Würfel2[0])
        pick_move_ai()


def AI_move_W(i,moves,W):
        global Pos1, Pos2, Pos3, Pos4, xx, c, movecounter, Pass, Würfel1, Würfel2, skip, cc 
        if Red_Cap_Piece == 0 and Red_winning_pos == False:
            
            Pos1 = moves[i-1]+W[0]
            Pos2 = moves[i-1]
            set_possibel_pos()
            move()
        if Red_Cap_Piece != 0 and Red_winning_pos == False:
            Pos3 = 1 
            Pos1 = moves[i-1]+W[0]
            Pos2 = moves[i-1]
            set_Cap_possible_pos()   
            move()
        if Red_Cap_Piece == 0 and Red_winning_pos == True:
            if moves[i-1] == 0:
                if difficulty == 1: 
                    for u in range (7):
                        if spielfeld2[u] != 0:
                            spielfeld2[u] = spielfeld2[u]-1
                            Ratios()
                            move()
                            break
                elif difficulty == 2 or difficulty == 3:
                    spielfeld2[int(W[0])-1] = spielfeld2[int(W[0])-1]-1
                    Ratios()
                    move()
            else:
                Pos1 = moves[i-1]+W[0]
                Pos2 = moves[i-1]
                set_possibel_pos()
                move()
        if c == 0 or xx == 0:
            moves1.clear()
            moves2.clear()
            fish_moves()
            
        if c == 1 and xx == 1: 
            if Würfel1[0] == Würfel2[0] and cc == 0:
                c = 0
                xx = 0
                cc = 1 
                moves1.clear()
                moves2.clear()
                fish_moves()
            else:
                skip = True 


            
def pick_move_ai():
    global spielfeld2, c, xx, moves1, moves2, Würfel1, Würfel2, skip

    if len(moves1) != 0 and c == 0:
        move1 = choose_move_ai(moves1,Würfel1)
        c = 1
        AI_move_W(move1, moves1, Würfel1)

    elif len(moves2) != 0 and xx == 0:
        move2 = choose_move_ai(moves2,Würfel2)
        xx = 1
        AI_move_W(move2, moves2, Würfel2)

    else:
        skip = True

def choose_move_ai(moves,W):
    
    global spielfeld1, spielfeld2, ai_difficulty
    print(ai_difficulty)
    if ai_difficulty == 2:
        for i in reversed(range(len(moves))):
            if moves[0] == 0:
                return 1    
            elif spielfeld1[int(moves[i])-1] == 1: 
                return i+1     
            elif spielfeld2[int(moves[i])-1] != 0: 
                return i+1   
        return len(moves)   
    elif ai_difficulty == 1:
        return random.randint(1, len(moves))
    elif ai_difficulty == 3:
        for i in reversed(range(len(moves))):
            if moves[0] == 0:
                return 1  
            elif 17 < moves[i] < 25:
                if spielfeld1[int(moves[i])-1] == 1: 
                    return i+1 
                elif spielfeld2[int(moves[i])-1] == 1: 
                    return i+1
                elif spielfeld2[int(moves[i])-1] > 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                    return i+1
            elif 11 < moves[i] < 18:
                if spielfeld2[int(moves[i])-1] == 1: 
                    return i+1
                elif spielfeld1[int(moves[i])-1] == 1: 
                    return i+1 
                elif spielfeld2[int(moves[i])-1] > 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                    return i+1

            elif 0 < moves[i] < 12:
                if sum(spielfeld1[12:24]) == 15 and sum(spielfeld2[0:12]) == 15 and Red_winning_pos == False:
                    if 0 < moves[i] < 7:
                        return i+1
                    elif 6 < moves[i] < 12:
                        return len(moves)
                else:
                    if 6 < moves[i] < 12:
                            if spielfeld2[int(moves[i])-1] == 1: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] > 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld1[int(moves[i])-1] == 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1 
                    elif 0 < moves[i] < 7:
                        if Red_winning_pos == True:
                            if spielfeld2[int(moves[i])-1] == 0 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 0: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 2 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 3 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] > 1 and spielfeld2[int(moves[i])-1+W[0]] > 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 1: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 2: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] == 3: 
                                return i+1
                            elif spielfeld2[int(moves[i])-1] > 1: 
                                return i+1
                        else:
                            if sum(spielfeld1[12:24]) == 15:
                                return len(moves)
                            else:
                                if spielfeld2[int(moves[i])-1] == 1: 
                                    return i+1
        return len(moves) 
                   


mein_menu = Menu(root)
root.config(menu=mein_menu)

file_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New...", command=File)
file_menu.add_command(label="Exit", command=root.quit)

Würfel_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Dice",command=Würfel_wurf)

Pass_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Pass",command=Pass_turn)

Game_mode_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Game mode", menu=Game_mode_menu)
Game_mode_menu.add_command(label="Player vs. AI", command=Ai)
Game_mode_menu.add_command(label="Player  vs. Player",command=PvP)

AI_lvl_menu = Menu(mein_menu,tearoff = False)
mein_menu.add_cascade(label="AI_difficulty", menu=AI_lvl_menu)
AI_lvl_menu.add_command(label="Easy", command=ai_difficulty1)
AI_lvl_menu.add_command(label="Medium",command=ai_difficulty2)
AI_lvl_menu.add_command(label="Hard", command=ai_difficulty3)

movecounter_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Starter",menu=movecounter_menu)
movecounter_menu.add_command(label="white",command=starter1)
movecounter_menu.add_command(label="Red",command=starter2)

difficulty_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Difficulty",menu=difficulty_menu)
difficulty_menu.add_command(label="Easy ",command=easy)
difficulty_menu.add_command(label="Hard",command=hard)

Regel_menu = Menu(mein_menu,tearoff=False)
mein_menu.add_cascade(label="Rules", command=show_regeln)

canvas.bind("<Button-1>", Position1)
canvas.bind("<Button-3>", Position2)
root.bind("<Key>", key)
root.bind("<Configure>", Ratios)
root.mainloop()
