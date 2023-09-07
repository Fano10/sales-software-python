from tkinter import filedialog
from main import*

global argument
argument = "null"

def espace(l_article,l_prix,l_quantiter):
    longeur_article = l_article
    longeur_prix = l_prix
    longeur_quantiter = l_quantiter
    espace = ' '
    valiny1 = ' '
    valiny2 = ' '
    valiny3 = ' '
    while longeur_article < 18:
        valiny1 = valiny1 + espace
        longeur_article = longeur_article + 1
    while longeur_prix < 9:
        valiny2 = valiny2 + espace
        longeur_prix = longeur_prix + 1
    while longeur_quantiter < 14:
        valiny3 = valiny3 + espace
        longeur_quantiter = longeur_quantiter + 1
    valiny = [valiny1,valiny2,valiny3]
    return valiny

def enregistrer_sous():
    global argument
    file = filedialog.asksaveasfilename(defaultextension=('Text file','*.txt'),
                                        filetypes=(('Text file','*.txt'),('Doc file','*.docx'))
                                        )
    argument = file
    file_open = open(file,'w')
    espace_article = '            '#13
    espace_prix = '      '#7
    espace_quantiter = '      '#7
    file_open.write('                    ' + entrer_nom_de_client.get()+'\n')
    file_open.write('\n'+"Article"+espace_article+"Prix"+espace_prix+"Quantiter"+espace_quantiter+"Total"+'\n')
    for objet in my_tree_commande.get_children():
        valeur = my_tree_commande.item(objet,'values')
        distance = espace(len(valeur[0]),len(valeur[1]),len(valeur[2]))
        file_open.write(valeur[0] + distance[0] + valeur[1] + distance[1] + valeur [2] +distance[2]+ valeur[3]+ '\n')
    file_open.write('\n'+'\t'+'\t'+'Total = '+ str(resultat.get(0,END)[0]))
    file_open.close()

def enregistrer():
    global argument
    if argument == "null":
        enregistrer_sous()
    else:
        file_open = open(argument, 'w')
        espace_article = '            '  # 13
        espace_prix = '      '  # 7
        espace_quantiter = '      '  # 7
        file_open.write(
            "Article" + espace_article + "Prix" + espace_prix + "Quantiter" + espace_quantiter + "Total" + '\n')
        for objet in my_tree_commande.get_children():
            valeur = my_tree_commande.item(objet, 'values')
            distance = espace(len(valeur[0]), len(valeur[1]), len(valeur[2]))
            file_open.write(
                valeur[0] + distance[0] + valeur[1] + distance[1] + valeur[2] + distance[2] + valeur[3] + '\n')

        file_open.close()












