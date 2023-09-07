
from fonction_inventaire import*
from fonction_relation import *

root.geometry("600x600")

mainmenu = Menu(root)
mainmenu.configure(background="red")

fichier = Menu(mainmenu, tearoff=0)

edition = Menu(mainmenu, tearoff=0)

triage = Menu(mainmenu,tearoff=0)
outils = Menu(mainmenu,tearoff=0)
aide = Menu(mainmenu,tearoff=0)

mainmenu.add_cascade(label="Fichier",menu=fichier,background="red")
mainmenu.add_cascade(label="Édition",menu=edition)
mainmenu.add_cascade(label="Triage",menu=triage)
mainmenu.add_cascade(label="Outils",menu=outils)
mainmenu.add_cascade(label="Aide",menu=aide)
tree_frame_inventaire.place(x=500, y=310)
my_tree_inventaire.pack()
lecture_inventaire()


frame_inventaire.place(x=450, y=200)
label_article = Label(frame_inventaire,text="Article",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_article.grid(row=0, column=0)
label_prix = Label(frame_inventaire,text="Prix",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_prix.grid(row=0, column=1)
label_nombre = Label(frame_inventaire,text="Nombre",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_nombre.grid(row=0, column=2)
entrer_article_inventaire.grid(row=1, column=0)
entrer_prix_inventaire.grid(row=1, column=1)
entrer_nombre_inventaire.grid(row=1, column=2)

frame_bouton_inventaire.place(x=1100,y=390)

bouton_ajouter = Button(frame_bouton_inventaire,text="Ajouter",width=30,border=5,font=(2),command=ajouter_inventaire)
bouton_ajouter.pack()

bouton_supprimer = Button(frame_bouton_inventaire,text="Supprimer",width=30,border=5,font=(2),command=supprimer_inventaire)
bouton_supprimer.pack()

bouton_selectionner = Button(frame_bouton_inventaire,text="Selectionner",width=30,border=5,font=(2),command=selectionner_inventaire)
bouton_selectionner.pack()

bouton_modifier = Button(frame_bouton_inventaire,text="Modifier",width=30,border=5,font=(2),command=modifier_inventaire)
bouton_modifier.pack()

entrer_nombre_inventaire.bind('<Return>',ajouter_toucher_inventaire)
my_tree_inventaire.bind('<Double 1>',selectionner_toucher_inventaire)


bouton_inventaire = Button(root,text="Inventaire",width=20,border=3,font=(2),command=inventaire)
bouton_inventaire.place(x=500,y=70)
bouton_commande = Button(root,text="Commande",width=20,border=3,font=(2),command=commande)
bouton_commande.place(x=900,y=70)












root.config(menu=mainmenu)
root.mainloop()