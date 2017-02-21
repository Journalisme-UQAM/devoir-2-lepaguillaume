#coding utf-8

import csv
import re
import string

fichier = "concordia1.csv"
data = open(fichier)

lignes = csv.reader(data)

next(lignes)

# Dictionnaire qui donne pour chaque chiffre/nombre romain ("keys") un chiffre/nombre arabe ("values") / Comprend des erreurs de frappe du .csv que j'ai repérés
d = {
    "i": "1", "ii": "2", "iii": "3", "iv": "4", "ivx": "4", "v": "5", "vi": "6", "vii": "7", "viii": "8",
    "ix": "9", "vix": "9", "viiii": "9", "x": "10", "xi": "11", "xii": "12", "xiii": "13", "xiv": "14", "xv": "15", "xvi": "16",
    "xvii": "17", "xviii": "18", "xix": "19", "xx": "20", "xxi": "21", "xxii": "22", "xxiii": "23",
    "xxiv": "24", "xxv": "25", "xxvi": "26", "xxvii": "27", "xxviii": "28", "xxix": "29", "xxx" : "30", "xxxi": "31", "xxxii": "32",
    "xxxiii": "33", "xxxiv": "34", "xxxv": "35", "xlvii": "47", "lvi": "56"
}

# Attribuer le prénom et nom des auteurs dans ma "loop", inversés pour épouser les conditions de ma phrase finale
for ligne in lignes:
    auteur = "{} {}".format(ligne[1],ligne[0])

# Pour cibler dans une "loop" le nom des thèses et des doctorats
    titre = (ligne[2])
# Pour calculer la longueur du titre
    longTitre = len(ligne[2])
# Je cible avec ma var "pages" la "string" qui me permettra de calculer le nbPages
    pages = (ligne[5])
    nbPages = []
    
# Déterminer parmi les thèses lesquelles sont des maîtrises et lesquelles sont des doctorats
    if "D." in ligne[6]:
        moud = "Le doctorat"
    else:
        moud = "La maîtrise"
    
# Pour les maîtrises et les thèses avec seulement des pages "leaves", j'en extrais le nbPages
    if pages.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
        nbPages = int(pages[0:3])

#Pour celles et ceux qui ont des pages liminaires en début de "string", on poursuit la "loop"        
    elif pages.startswith(("i", "v", "x", "l")):
#J'isole les nb romains avec la fct "split"
       p = pages.split(',',1)
       romain = p[0]
#Je fais intervenir les valeurs de mon dictionnaire dans la "loop" pour faire correspondre une valeur aux chiffres romains 
       rom = int(d[romain])

       araS = p[1]
       ara = araS.split()
       a = ara[0]
      
       a1 = re.sub("[^0-9]","", a)
       a2 = a1.strip()
#Je convertis en "integer" pour pourvoir additionner les valeurs numériques associées au chiffres romains au pages "leaves"
       nbPages = int(float(a2))

# On additionne les chiffres liminaires au "leaves"
       sum = nbPages + rom

#Ultime étape: on insère le contenu des var dans la phrase finale. À noter qu'il y a un espace insécable après la fin du titre que je ne parviens pas à supprimer.       
    print("{} de {} compte {} pages. Son titre est « {}», lequel comporte {} caratères.".format(moud, auteur, sum, titre, longTitre))
    

#Mon script cesse de rouler à la ligne 60, car il n'y pas de nombre associé à "leaves" pour la maîtrise de Nadia Colasurdo. J'ai essayé de trouver une façon d'associer à la ValueError un 0 pour poursuivre le script, mais sans succès.