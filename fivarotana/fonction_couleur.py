from fonction_lecture import*


def couleur_fond_defaut():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("defaut","couleur_fond")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()
def couleur_fond_rouge():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("rouge","couleur_fond")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def couleur_fond_rose():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("rose","couleur_fond")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def couleur_fond_blanc():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("blanc","couleur_fond")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()



