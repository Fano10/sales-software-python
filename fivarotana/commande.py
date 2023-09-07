from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Application')
root.geometry("1000x600")
root.config(bg="#7A9A88")

def nombre_de_ligne(file):
    boucle = 1
    while 1 < 2:
        valiny = file.readline()
        nb = len(valiny)
        if nb > 1:
            isa = valiny[nb-1]
            if isa == '\n' and nb-1 != 0:
                boucle = boucle + 1
            else:
                break
        else:
            boucle = boucle - 1
            break
    file.close()
    return boucle

def mamaky(file,choix):
    choix_1 = choix + '\n'
    a = 0
    while 1 < 2 :
        valiny = file.readline()
        isa = len(valiny)
        if(valiny[isa-1] != '\n'):
            valiny = valiny + '\n'
        a = a + 1
        if valiny == choix_1 or valiny == choix:
            break
    file.close()
    return a

def vidiny(file,boucle):
    a = 0
    while a < boucle:
        valiny = file.readline()
        a= a + 1
    file.close()
    return valiny



def open_text():
    text_file = open("commande.txt", "w")
    text_file.write(my_text.get(1.0, END))
    text_file_prix = open("isa.txt", "w")
    text_file_prix.write(prix_text.get(1.0, END))
    text_file.close()
    text_file_prix.close()

    commande = open("commande.txt", "r+")
    boucle_initial = nombre_de_ligne(commande)
    commande = open("commande.txt", "r+")
    boucle = boucle_initial
    a = 0
    b = 0
    total = 0
    while a < boucle_initial:
        commande = open("commande.txt", "r+")
        isa = open("isa.txt", "r+")
        while b < boucle:
            repas = open("article.txt", "r+")
            prix = open("prix.txt", "r+")
            quantite = isa.readline()
            commande_1 = commande.readline()
            vidy = int(vidiny(prix, mamaky(repas, commande_1))) * int(quantite)
            total = total + vidy
            b = b + 1
        a = a + 1
    resultat.delete(0, END)
    resultat.insert(0, total)
    commande.close()
    isa.close()


#principale
my_text = Text(root, width=65, height=23,font=("Helvetica"))
my_text.place(x=100,y=150)

prix_text=Text(root, width=27, height=23,font=("Helvetica"))
prix_text.place(x=800,y=150)

open_bouton = Button(root, text="Total",width=27,border=5,bg="#67E232",fg="white",font=(2), command=open_text)
open_bouton.place(x=1190,y=550)

label_ariary = Label(root,text="Ar",font=("Arial","25","bold italic"),bg="#7A9A88",fg="#D8D8D8")
label_ariary.place(x=1379,y=640)

label_commande = Label(root,text="Commande",font=("Times", "32", "bold italic") ,bg='#7A9A88',fg="#2837BD")
label_commande.place(x=650,y=23)

resultat = Listbox(root,bg="#D8D8D8",height=1,width=10,font=("Helvetica",25))
resultat.place(x=1190, y=640)





root.mainloop()
