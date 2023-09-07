from tkinter import*


def modifier():
    liste_box.place_forget()
    prix_box.place_forget()
    bouton_modifier.place_forget()
    liste_texte.place(x=100, y=150)
    prix_texte.place(x=800, y=150)
    bouton_annuler.place(x=1150, y=270)
    sauvegarder.place(x=1150, y=200)
    liste_texte.delete(1.0, END)
    prix_texte.delete(1.0, END)
    article = open("article.txt","r")
    vidiny = open("prix.txt","r")
    valiny_article = article.readlines()
    valiny_vidiny = vidiny.readlines()
    for item in valiny_article:
        liste_texte.insert(END, item)
    for item2 in valiny_vidiny:
        prix_texte.insert(END, item2)
    article.close()
    vidiny.close()



def sauvegarder():
    sauvegarder.place_forget()
    liste_texte.place_forget()
    prix_texte.place_forget()
    bouton_annuler.place_forget()
    liste_box.place(x=100, y=150)
    prix_box.place(x=800, y=150)
    bouton_modifier.place(x=1150, y=200)
    liste_box.delete(0,END)
    prix_box.delete(0,END)
    article = open("article.txt", "w")
    vidiny = open("prix.txt", "w")
    article.write(liste_texte.get(1.0,END))
    vidiny.write(prix_texte.get(1.0,END))
    article.close()
    vidiny.close()
    article = open("article.txt", "r")
    vidiny = open("prix.txt", "r")
    valiny_article = article.readlines()
    valiny_vidiny = vidiny.readlines()
    for item in valiny_article:
        liste_box.insert(END, item)
    for item2 in valiny_vidiny:
        prix_box.insert(END, item2)
    article.close()
    vidiny.close()




def annuler():
    sauvegarder.place_forget()
    liste_texte.place_forget()
    prix_texte.place_forget()
    bouton_annuler.place_forget()
    liste_box.place(x=100, y=150)
    prix_box.place(x=800, y=150)
    bouton_modifier.place(x=1150, y=200)






root = Tk()
root.title('inventaire')
root.geometry("1000x600")
root.config(bg="#7A9A88")
#creation de label
label_inventaire = Label(root,text="Inventaire",font=("Times", "32", "bold italic") ,bg='#7A9A88',fg="#2837BD")
label_inventaire.place(x=650,y=23)
label_article = Label(root,text="Articles",font=("Arial", "20", "bold italic") ,bg='#7A9A88',fg="black")
label_article.place(x=110,y=110)
label_prix = Label(root,text="Ariary",font=("Arial", "20", "bold italic") ,bg='#7A9A88',fg="black")
label_prix.place(x=810,y=110)

#creation de frame pour liste box et son scrollbar
my_frame_box = Frame(root)
my_frame_box_prix = Frame(root)
my_scrollbar_box = Scrollbar(my_frame_box_prix, orient=VERTICAL)


#creation de Listebox
liste_box = Listbox(my_frame_box, width=65, height=23,font=("Helvetica"),yscrollcommand=my_scrollbar_box.set)
prix_box= Listbox(my_frame_box_prix, width=27, height=23,font=("Helvetica"),yscrollcommand=my_scrollbar_box.set)
my_scrollbar_box.config(command=prix_box.yview)
my_scrollbar_box.config(command=liste_box.yview)
my_scrollbar_box.pack(side=RIGHT,fill=Y)
my_frame_box.place(x=100,y=150)
liste_box.pack()
my_frame_box_prix.place(x=800,y=150)
prix_box.pack()

#mameno ny Liste box
article = open("article.txt", "r")
vidiny = open("prix.txt", "r")
valiny_article = article.readlines()
valiny_vidiny = vidiny.readlines()
for item in valiny_article:
    liste_box.insert(END, item)
for item2 in valiny_vidiny:
    prix_box.insert(END, item2)
article.close()
vidiny.close()

#creation de Text
liste_texte = Text(root, width=65, height=23,font=("Helvetica"))
prix_texte = Text(root, width=27, height=23,font=("Helvetica"))

#creation de bouton
sauvegarder = Button(root,text="Sauvegarder",width=30,border=5,bg="#67E232",fg="white",font=(2),command=sauvegarder)
bouton_modifier = Button(root,text="Modifier",width=30,border=5,bg="#67E232",fg="white",font=(2),command=modifier)
bouton_modifier.place(x=1150,y=200)
bouton_annuler = Button(root,text="Annuler",width=30,border=5,bg="#67E232",fg="white",font=(2),command=annuler)


root.mainloop()