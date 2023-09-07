import sqlite3
from class_style import Styl
from tkinter import*
from tkinter import ttk
root = Tk()
    #style de notre treeview

style = Styl()

        #inventaire
tree_frame_inventaire = Frame(root)
my_scrollbar = Scrollbar(tree_frame_inventaire, orient=VERTICAL)
my_tree_inventaire = ttk.Treeview(tree_frame_inventaire, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_tree_inventaire.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
#Colonne
my_tree_inventaire['columns'] = ("article", "prix", "nombre")
my_tree_inventaire.column("#0", width=90, minwidth=35)
my_tree_inventaire.column("article", anchor=W, width=200,minwidth=190)
my_tree_inventaire.column("prix", anchor=CENTER,width=110,minwidth=100)
my_tree_inventaire.column("nombre", anchor=CENTER, width=75,minwidth=70)

#en tete
my_tree_inventaire.heading("#0", text="Numero", anchor=W)
my_tree_inventaire.heading("article", text="Artcile", anchor=W)
my_tree_inventaire.heading("prix", text="Prix/Ar", anchor=CENTER)
my_tree_inventaire.heading("nombre", text="Nombre", anchor=CENTER)
my_tree_inventaire.tag_configure('font', font=('Arial','15','bold italic'))
#les themes
my_tree_inventaire.tag_configure('defaut',background="#C0C0C0")
my_tree_inventaire.tag_configure('white',background="white")
my_tree_inventaire.tag_configure('blue',background="#0080C0")
my_tree_inventaire.tag_configure('red',background="#FF0000")
my_tree_inventaire.tag_configure('green',background="#00FF00")

#Corps
frame_inventaire = Frame(root)
entrer_article_inventaire = Entry(frame_inventaire,font=('Arial',20))
entrer_prix_inventaire = Entry(frame_inventaire,font=('Arial',20),width=15)
entrer_nombre_inventaire = Entry(frame_inventaire,font=('Arial',20),width=10)

frame_bouton_inventaire = Frame(root)

        #commande
tree_frame_commande = Frame(root)
my_scrollbar = Scrollbar(tree_frame_commande, orient=VERTICAL)
my_tree_commande = ttk.Treeview(tree_frame_commande, yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_tree_commande.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
#Colonne
my_tree_commande['columns'] = ("article", "prix", "quantiter", "total")
my_tree_commande.column("#0", width=90, minwidth=35)
my_tree_commande.column("article", anchor=W, width=200,minwidth=190)
my_tree_commande.column("prix", anchor=CENTER,width=110,minwidth=100)
my_tree_commande.column("quantiter", anchor=CENTER, width=75,minwidth=70)
my_tree_commande.column("total", anchor=CENTER, width=75,minwidth=70)

#en tete
my_tree_commande.heading("#0", text="Numero", anchor=W)
my_tree_commande.heading("article", text="Artcile", anchor=W)
my_tree_commande.heading("prix", text="Prix", anchor=CENTER)
my_tree_commande.heading("quantiter", text="Quantiter", anchor=CENTER)
my_tree_commande.heading("total", text="Total", anchor=CENTER)
my_tree_commande.tag_configure('font', font=('Arial','15','bold italic'))

frame_commande = Frame(root)
frame_client = Frame(root)
entrer_article_commande = Entry(frame_commande,font=('Arial',20))
entrer_quantiter_commande = Entry(frame_commande,font=('Arial',20),width=15)
entrer_nom_de_client = Entry(frame_client,font=('Arial',20),width=25)
resultat = Listbox(root,bg="#D8D8D8",height=1,width=10,font=("Helvetica",25))

frame_box = Frame(root)
my_scrollbar_box = Scrollbar(frame_box, orient=VERTICAL)
liste_box = Listbox(frame_box,width=50, yscrollcommand=my_scrollbar_box.set)
my_scrollbar_box.config(command=liste_box.yview)
toppings = []


frame_bouton_commande = Frame(root)











