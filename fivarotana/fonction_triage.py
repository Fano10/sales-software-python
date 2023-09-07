from fonction_lecture import*

def triage_defaut():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("defaut","triage")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def triage_alphabetique():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("alphabetique","triage")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def triage_prix():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("prix","triage")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def triage_nombre():
    connection = sqlite3.connect("systeme.db")
    curseur = connection.cursor()
    origine = ("nombre","triage")
    curseur.execute("UPDATE parametre SET donner=? WHERE type=?", origine)
    connection.commit()
    connection.close()
    lecture_inventaire()

def triage_plus_vendu():
    pass