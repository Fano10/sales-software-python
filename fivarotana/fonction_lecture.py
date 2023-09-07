from main import *


def trie_inventaire():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("triage",)
    donner = curseur.execute("SELECT donner FROM parametre WHERE type=?", origine)
    valiny = donner.fetchone()[0]
    connection.commit()
    connection.close()
    return valiny

def selection_trie():
    donner = trie_inventaire()
    if donner == 'defaut':
        valiny ="SELECT*FROM inventaire"
    elif donner == 'alphabetique':
        valiny ="SELECT* FROM inventaire ORDER BY article ASC"
    elif donner == 'prix':
        valiny = "SELECT*FROM inventaire ORDER BY prix ASC"
    else:
        valiny = "SELECT*FROM inventaire ORDER BY nombre ASC"
    return valiny

def theme():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("theme",)
    donner = curseur.execute("SELECT donner FROM parametre WHERE type=?", origine)
    valiny = donner.fetchone()[0]
    connection.commit()
    connection.close()
    return valiny

def selection_theme():
    donner = theme()
    if donner == 'defaut':
        valiny =['defaut','defaut']
    elif donner == 'blue_white':
        valiny =['blue','white']
    elif donner == 'red_white':
        valiny = ['red','white']
    else:
        valiny = ['green','white']
    return valiny



def lecture_inventaire():
    Styl()
    for item in my_tree_inventaire.get_children():
        my_tree_inventaire.delete(item)
    selection = selection_trie()
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    entana = curseur.execute(selection)
    c = entana.fetchall()
    a = 0
    theme = selection_theme()
    for item in c:
        if a % 2 == 0:
            color = theme[0]
        else:
            color = theme[1]
        my_tree_inventaire.insert(parent='', index='end', iid=a, text=str(a), values=(item[0], item[1],item[2]), tags=(color,))
        a = a + 1
    connection.close()