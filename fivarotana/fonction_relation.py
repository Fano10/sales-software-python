from main import*
from fonction_commande import*


def inventaire():
    Styl()
    #oublier
    tree_frame_commande.place_forget()
    frame_commande.place_forget()
    frame_box.place_forget()
    frame_bouton_commande.place_forget()
    #montrer
    tree_frame_inventaire.place(x=500, y=310)
    frame_inventaire.place(x=450, y=200)
    frame_bouton_inventaire.place(x=1100,y=390)
    my_tree_inventaire.pack()



def commande():
    Styl()
    #oublier
    tree_frame_inventaire.place_forget()
    frame_inventaire.place_forget()
    frame_bouton_inventaire.place_forget()
    my_tree_inventaire.pack_forget()
    #montrer
    tree_frame_commande.place(x=500, y=310)
    frame_commande.place(x=450, y=200)
    frame_bouton_commande.place(x=1100, y=310)
    #fonction
    mameno_valiny()