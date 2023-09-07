from fonction_inventaire import*
from fonction_relation import *
from fonction_triage import*
from fonction_theme import *
from fonction_couleur import*
from fonction_fichier import*

mameno_valiny()

root.geometry("600x600")

mainmenu = Menu(root)
mainmenu.configure(background="red")



edition = Menu(mainmenu, tearoff=0)
    #fichier
fichier = Menu(mainmenu, tearoff=0)
fichier.add_command(label="Enregister",command=enregistrer)
fichier.add_command(label="Enregister sous",command=enregistrer_sous)

mainmenu.add_cascade(label="Fichier",menu=fichier)
    #triage
triage = Menu(mainmenu,tearoff=0)
triage.add_command(label="Defaut",command=triage_defaut)
triage.add_command(label="Alphabetique",command=triage_alphabetique)
triage.add_command(label="Prix", command=triage_prix)
triage.add_command(label="Nombre",command=triage_nombre)
triage.add_command(label="le plus vendu",command=triage_plus_vendu)
mainmenu.add_cascade(label="Triage",menu=triage)
    #Outils
#theme
theme = Menu(mainmenu,tearoff=0)
theme.add_command(label="Defaut",command=theme_defaut)
theme.add_command(label="Bleu blanc",command=theme_blue_white)
theme.add_command(label="Rouge blanc",command=theme_red_white)
theme.add_command(label="Vert Blanc",command=theme_green_white)
#couleur
couleur_fond = Menu(mainmenu,tearoff=0)
couleur_fond.add_command(label="Defaut",command=couleur_fond_defaut)
couleur_fond.add_command(label="Rouge",command=couleur_fond_rouge)
couleur_fond.add_command(label="Blanc",command=couleur_fond_blanc)
couleur_fond.add_command(label="Rose",command=couleur_fond_rose)
#couleur_fond.add_command(label="Bleu",command=couleu)


#outils
outils = Menu(mainmenu,tearoff=0)
outils.add_cascade(label="theme",menu=theme)
outils.add_cascade(label="couleur de fond",menu=couleur_fond)
mainmenu.add_cascade(label="Outils",menu=outils)


aide = Menu(mainmenu,tearoff=0)


mainmenu.add_cascade(label="Édition",menu=edition)
mainmenu.add_cascade(label="Aide",menu=aide)
my_tree_commande.pack()
tree_frame_commande.place(x=500, y=310)

frame_commande.place(x=450, y=200)
label_article = Label(frame_commande,text="Article",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_article.grid(row=0, column=0)
label_quantiter = Label(frame_commande,text="Quantiter",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_quantiter.grid(row=0, column=1)
frame_client.place(x=30, y=380)
label_client = Label(frame_client,text="Client",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_client.pack()


frame_commande.place(x=450, y=200)
entrer_article_commande.grid(row=1, column=0)
entrer_quantiter_commande.grid(row=1, column=1)
entrer_nom_de_client.pack()

frame_bouton_commande.place(x=1100,y=310)
bouton_ajouter_commande = Button(frame_bouton_commande,text="Ajouter",width=30,border=5,font=(2),command=ajouter_commande)
bouton_ajouter_commande.pack()

bouton_supprimer_commande = Button(frame_bouton_commande,text="Supprimer",width=30,border=5,font=(2),command=supprimer_commande)
bouton_supprimer_commande.pack()

bouton_selectionner_commande = Button(frame_bouton_commande,text="Selectionner",width=30,border=5,font=(2),command=selectionner_commande)
bouton_selectionner_commande.pack()

bouton_modifier_commande = Button(frame_bouton_commande,text="Modifier",width=30,border=5,font=(2),command=modifier_commande)
bouton_modifier_commande.pack()
bouton_total_commande = Button(frame_bouton_commande,text="Totals",width=30,border=5,font=(2),command=total_commande)
bouton_total_commande.pack()

resultat.place(x=1100,y=630)
my_scrollbar_box.pack(side=RIGHT, fill=Y)
liste_box.bind('<Double 1>',fillout)
entrer_article_commande.bind("<KeyRelease>",check)



entrer_quantiter_commande.bind('<Return>',ajouter_toucher_commande)
my_tree_commande.bind('<Double 1>',selectionner_toucher_commande)



bouton_inventaire = Button(root,text="Inventaire",width=20,border=3,font=(2),fg="red",command=inventaire)
bouton_inventaire.place(x=500,y=70)
bouton_commande = Button(root,text="Commande",width=20,border=3,font=(2),fg="red",command=commande)
bouton_commande.place(x=900,y=70)


#3#33-------------------------------------------------------------------------------------------------------------------------------------------------------


#tree_frame_inventaire.place(x=500, y=310)
#my_tree_inventaire.pack()
lecture_inventaire()


#frame_inventaire.place(x=450, y=200)
label_article = Label(frame_inventaire,text="Article",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_article.grid(row=0, column=0)
label_prix = Label(frame_inventaire,text="Prix/Ar",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_prix.grid(row=0, column=1)
label_nombre = Label(frame_inventaire,text="Nombre",font=("Times", "20", "bold italic") ,fg="#2837BD")
label_nombre.grid(row=0, column=2)
entrer_article_inventaire.grid(row=1, column=0)
entrer_prix_inventaire.grid(row=1, column=1)
entrer_nombre_inventaire.grid(row=1, column=2)

#frame_bouton_inventaire.place(x=1100,y=390)

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








root.config(menu=mainmenu)
root.mainloop()