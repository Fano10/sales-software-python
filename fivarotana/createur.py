import sqlite3

connection = sqlite3.connect("systeme.db")
curseur = connection.cursor()
origine = ("couleur_fond","defaut")
curseur.execute("INSERT INTO parametre VALUES(?,?)",origine)
connection.commit()

connection.close()
