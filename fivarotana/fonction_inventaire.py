
from fonction_lecture import*
global argument

#ajouter

def ajouter_inventaire():
   #compteur = lecture_2()
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    for item in my_tree_inventaire.get_children():
        my_tree_inventaire.delete(item)
    article = entrer_article_inventaire.get()
    prix = int(entrer_prix_inventaire.get())
    nombre = int(entrer_nombre_inventaire.get())
    fitambarany = (article , prix ,nombre,)
    curseur.execute("INSERT INTO inventaire(article,prix,nombre) VALUES(?,?,?)",fitambarany)
    connection.commit()
    entrer_prix_inventaire.delete(0, END)
    entrer_article_inventaire.delete(0, END)
    entrer_nombre_inventaire.delete(0,END)
    connection.close()
    lecture_inventaire()

def ajouter_toucher_inventaire(event):
   #compteur = lecture_2()
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    for item in my_tree_inventaire.get_children():
        my_tree_inventaire.delete(item)
    article = entrer_article_inventaire.get()
    prix = int(entrer_prix_inventaire.get())
    nombre = int(entrer_nombre_inventaire.get())
    fitambarany = (article , prix,nombre,)
    curseur.execute("INSERT INTO inventaire(article,prix,nombre) VALUES(?,?,?)",fitambarany)
    connection.commit()
    entrer_prix_inventaire.delete(0, END)
    entrer_article_inventaire.delete(0, END)
    entrer_nombre_inventaire.delete(0, END)
    connection.close()
    lecture_inventaire()

def selectionner_inventaire():
    global argument
    entrer_article_inventaire.delete(0, END)
    entrer_prix_inventaire.delete(0, END)
    entrer_nombre_inventaire.delete(0, END)
    selecter = my_tree_inventaire.focus()
    values = my_tree_inventaire.item(selecter,'values')
    argument = values[0]
    print(argument)
    entrer_article_inventaire.insert(0,values[0])
    entrer_prix_inventaire.insert(0,values[1])
    entrer_nombre_inventaire.insert(0,values[2])

def selectionner_toucher_inventaire(event):
    global argument
    entrer_article_inventaire.delete(0, END)
    entrer_prix_inventaire.delete(0, END)
    entrer_nombre_inventaire.delete(0,END)
    selecter = my_tree_inventaire.focus()
    values = my_tree_inventaire.item(selecter,'values')
    argument = values[0]
    entrer_article_inventaire.insert(0,values[0])
    entrer_prix_inventaire.insert(0,values[1])
    entrer_nombre_inventaire.insert(0,values[2])

def modifier_inventaire():
    global argument
    article = entrer_article_inventaire.get()
    prix = int(entrer_prix_inventaire.get())
    nombre = int(entrer_nombre_inventaire.get())
    valiny = (article,prix,nombre,argument)
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    curseur.execute("UPDATE inventaire SET article=?,prix=?,nombre=? WHERE article=?",valiny)
    connection.commit()
    connection.close()
    for item in my_tree_inventaire.get_children():
        my_tree_inventaire.delete(item)
    entrer_article_inventaire.delete(0, END)
    entrer_prix_inventaire.delete(0,END)
    entrer_nombre_inventaire.delete(0, END)
    lecture_inventaire()

def supprimer_inventaire():
    selecter = my_tree_inventaire.focus()
    values = my_tree_inventaire.item(selecter, 'values')
    valiny = values[0]
    valiny = (valiny,)
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    curseur.execute("DELETE FROM inventaire WHERE article=?",valiny)
    connection.commit()
    connection.close()
    for item in my_tree_inventaire.get_children():
        my_tree_inventaire.delete(item)
    lecture_inventaire()