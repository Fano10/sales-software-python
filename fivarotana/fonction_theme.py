from fonction_lecture import*

def theme_defaut():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("defaut","theme")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def theme_blue_white():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("blue_white","theme")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def theme_red_white():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("red_white","theme")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def theme_green_white():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("green_white","theme")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()
