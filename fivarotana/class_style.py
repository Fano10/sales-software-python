from tkinter import ttk
import sqlite3

def couleur_fond():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("couleur_fond",)
    donner = curseur.execute("SELECT donner FROM parametre WHERE type=?", origine)
    valiny = donner.fetchone()[0]
    connection.commit()
    connection.close()
    return valiny

def selection_couleur_fond():
    donner = couleur_fond()
    if donner == 'defaut':
        valiny = '#C7BCB8'
    elif donner == 'rouge':
        valiny ='#F30C2F'
    elif donner == 'rose':
        valiny = '#FF80C0'
    else:
        valiny = 'white'
    return valiny

class Styl:

    def __init__(self):
        couleur_fond = selection_couleur_fond()
        self = ttk.Style()
        self.theme_use("default")
        self.configure("Treeview",
                        background=couleur_fond,
                        foreground="black",
                        rowheight=35,
                        fieldbackground=couleur_fond
                        )
        self.map('Treeview',
                  background=[('selected', 'blue')]
                  )