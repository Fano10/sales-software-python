from main import *

global count
count = 0


def prix_uniter(nom_article):
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    article = (nom_article,)
    prix_unique = curseur.execute('SELECT prix FROM inventaire WHERE article = ?',article)
    valiny = prix_unique.fetchone()
    connection.close()
    return valiny[0]

def total_uniter(nom_article,fois):
    prix = prix_uniter(nom_article)
    valiny = prix*int(fois)
    return valiny


def ajouter_commande():
    global count
    prix_unique = prix_uniter(entrer_article_commande.get())
    total_unique = total_uniter(entrer_article_commande.get(),entrer_quantiter_commande.get())
    my_tree_commande.insert(parent='', index='end', iid=count, text=str(count), values=(entrer_article_commande.get(),prix_unique, entrer_quantiter_commande.get(),total_unique))
    count = count + 1
    entrer_quantiter_commande.delete(0, END)
    entrer_article_commande.delete(0, END)

def selectionner_commande():
    entrer_quantiter_commande.delete(0, END)
    entrer_article_commande.delete(0, END)
    #azo le indice
    selecter = my_tree_commande.focus()
    #ampiasaina
    values = my_tree_commande.item(selecter,'values')
    entrer_article_commande.insert(0,values[0])
    entrer_quantiter_commande.insert(0,values[2])

def modifier_commande():
    selecter = my_tree_commande.focus()
    #save nez data
    prix_unique = prix_uniter(entrer_article_commande.get())
    total_unique = total_uniter(entrer_article_commande.get(),entrer_quantiter_commande.get())
    my_tree_commande.item(selecter, text=str(selecter),values=(entrer_article_commande.get(),prix_unique,entrer_quantiter_commande.get(),total_unique))
    entrer_article_commande.delete(0, END)
    entrer_quantiter_commande.delete(0, END)

def total_commande ():
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    isa = 0
    for item in my_tree_commande.get_children():
        isa = isa + 1
    boucle = 0
    total = 0
    while boucle < isa:
        article = my_tree_commande.item(boucle,'values')
        quantiter = int(article[2])
        prend = (article[0],)
        prix = curseur.execute("SELECT prix FROM inventaire WHERE article=?",prend)
        fois = prix.fetchone()[0] * quantiter
        total = total + fois
        boucle = boucle + 1
    resultat.delete(0, END)
    resultat.insert(0, total)
    connection.close()
def supprimer_commande():
    isa = 0
    a = 0
    global count
    for item in my_tree_commande.selection():
        count = count - 1
        print(item)
        my_tree_commande.delete(item)
        a = int(item)
        while a < count:
            suivant = my_tree_commande.item((a+1),'values')
            my_tree_commande.insert(parent='', index='end', iid=a, text=str(a),values=(suivant[0], suivant[1]))
            #print(a)
            my_tree_commande.delete((a+1))
            a = a + 1


def mameno_valiny():
    valiny = []
    connection = sqlite3.connect("base.db")
    curseur = connection.cursor()
    entana = curseur.execute("SELECT article FROM inventaire")
    c = entana.fetchall()
    for item in c:
        valiny.append(item[0])
    connection.close()
    return valiny

def update(data):
    #fafana
    liste_box.delete(0, END)
    #azoutena le zavatra
    for item in data:
        liste_box.insert(END, item)

def fillout(vaovao):
    entrer_article_commande.delete(0, END)
    entrer_article_commande.insert(0, liste_box.get(ACTIVE))
    frame_box.place_forget()
def check(vaovao):
    reponse = mameno_valiny()
    typed = entrer_article_commande.get()
    if typed =='':
        valiny = reponse
        frame_box.place_forget()
    else:
        valiny = []
        for item in reponse:
            if typed.lower() in item.lower():
                valiny.append(item)
                frame_box.place(x=450, y=274)
                liste_box.pack()
    update(valiny)

def ajouter_toucher_commande(event):
    global count
    prix_unique = prix_uniter(entrer_article_commande.get())
    total_unique = total_uniter(entrer_article_commande.get(),entrer_quantiter_commande.get())
    my_tree_commande.insert(parent='', index='end', iid=count, text=str(count), values=(entrer_article_commande.get(),prix_unique, entrer_quantiter_commande.get(),total_unique))
    count = count + 1
    entrer_quantiter_commande.delete(0, END)
    entrer_article_commande.delete(0, END)

def selectionner_toucher_commande(event):
    entrer_quantiter_commande.delete(0, END)
    entrer_article_commande.delete(0, END)
    #azo le indice
    selecter = my_tree_commande.focus()
    #ampiasaina
    values = my_tree_commande.item(selecter,'values')
    entrer_article_commande.insert(0,values[0])
    entrer_quantiter_commande.insert(0,values[2])