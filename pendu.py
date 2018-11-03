#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from random import choice
from fonctions import vLettre, rTLettre, rFLettre, sauvegarde, vSauvegarde, restauration, delSauvegarde

print("Bienvenu dans le jeu du pendu :)")
prenom = input("Entrez votre prénom : \n")

if vSauvegarde(prenom):
    restaurer = input("Un fichier de sauvegarde a été trouvé à votre prénom.\n\
Tapez c : pour le charger\ns : pour le supprimer\nr : pour jouer sans fichier de sauvegarde\n")
    restaurer = restaurer.upper()
    if restaurer == "C":
        score = restauration(prenom)
    elif restaurer == "S":
        delSauvegarde(prenom)
        score = 0
    elif restaurer == "R":
        score = 0
        pass
else:
    score = int()

replay = True
while replay:
    from donnees import  listeMots, rMot, lettresT, fLettres, chances
    mot = choice(listeMots)
    longueurMot = mot.__len__()
    print("Le mot à deviner contient {} lettres.".format(longueurMot))

    while rMot != mot and chances > 0:
        x = input("Entrez une autre lettre : ")
        x = vLettre(x) # x prend la valeur de la majuscule de la lettre saisie
        if x in mot:
            while x in lettresT:
                print("Vous avez déjà trouvé cette lettre")
                x = input("Entrez une autre lettre : ")
                x = vLettre(x)
            if not(x in lettresT):
                rMot, lettresT = rTLettre(x, mot, lettresT)
                print("Bravo! Le mot à deviner contient la lettre {} : \n{}".format(x, rMot))
        else:
            if  x in fLettres:
                print("Vous avez déjà saisi cette lettre!!!")
                x = input("Entrez une autre lettre : ")
                x = vLettre(x)
            elif not(x in fLettres):
                chances -= 1
                rMot = rFLettre(x, mot,lettresT,fLettres)
                print("Pas de bol! La lettre {} ne figure pas dans le mot à deviner.\n {}".format(x, rMot))
                print("Il vous manque {} chance(s)".format(chances))
            print("Fausses lettres déjà saisies : {} ".format(fLettres))

    if chances == 0:
        print("Dommage {} :(, vous avez épuisé toutes vos chances. \nLe mot à deviné était : {}".format(prenom, mot))
    if rMot == mot:
        score = chances + score
        print("Félicitations {} :), vous avez trouvé le mot!".format(prenom))
        print("Vous avez gagné {} points \n".format(chances))

    rejouer = input("Voulez-vous rejouer une autre partie ? Oui/Non\n")
    rejouer = rejouer.upper()
    if rejouer == "NON" or "N":
        replay = False
        print("Votre score est de : {} points".format(score))

        sauvegarder = input("Voulez-vous sauvegarder cette partie ? Oui/Non")
        sauvegarder = sauvegarder.upper()
        if sauvegarder == "OUI" or "O":
            sauvegarde(prenom, score)

print("\nCe jeu a été développé par Bernel Dahssi le 02 Novembre\nTous droits réservés. Copyright © 2018")

os.system("pause")
