#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from random import choice
from fonctions import *

print("Bienvenu dans le jeu du pendu :)")
prenom = input("Entrez votre prénom : \n")

if vSauvegarde(prenom):
    restaurer = input("\nUn fichier de sauvegarde a été trouvé à votre prénom.\n\
La dernière fois, vous avez eu un score de : {} points.\n\
Tapez : \nc : pour le charger\ns : pour le supprimer\nr : pour jouer sans fichier de sauvegarde\n".format(restauration(prenom)))
    restaurer = restaurer.upper()
    if restaurer == "C":
        score = restauration(prenom)
        print("\nChargement .......")
    elif restaurer == "S":
        delSauvegarde(prenom)
        print("\nVotre sauvegarde a bien été éffacée, vous commencez une nouvelle partie")
        score = 0
    elif restaurer == "R":
        score = 0
        print("\nVous commencez une nouvelle partie sans chargement")
        pass
else:
    score = int()

replay = True
while replay:
    from donnees import *
    mot = choice(listeMots)
    longueurMot = mot.__len__()
    print("\nLe mot à deviner contient {} lettres.".format(longueurMot))

    while rMot != mot and chances > 0:
        x = input("Entrez une lettre : ")
        x = vLettre(x) # x prend la valeur de la majuscule de la lettre saisie
        if x in mot:
            while x in lettresT:
                print("Vous avez déjà trouvé cette lettre !")
                x = input("Entrez une autre lettre : ")
                x = vLettre(x)
            if not(x in lettresT):
                rMot, lettresT = rTLettre(x, mot, lettresT)
                print("Bravo! Le mot à deviner contient la lettre {} : \n{}\n".format(x, rMot))
        else:
            if  x in fLettres:
                print("Vous avez déjà saisi cette lettre!!!\n")
                x = input("Entrez une autre lettre : ")
                x = vLettre(x)
            elif not(x in fLettres):
                chances -= 1
                rMot = rFLettre(x, mot,lettresT,fLettres)
                print("Pas de bol! La lettre {} ne figure pas dans le mot à deviner.\n {}".format(x, rMot))
                print("Il vous manque {} chance(s)".format(chances))
            print("Fausses lettres déjà saisies : {} \n".format(fLettres))

    if chances == 0:
        print("Dommage {} :(, vous avez épuisé toutes vos chances. \nLe mot à deviné était : {}".format(prenom, mot))
    if rMot == mot:
        score = chances + score
        print("Félicitations {} :), vous avez trouvé le mot!".format(prenom))
        print("Vous avez gagné {} points \n".format(chances))

    rejouer = input("\nVoulez-vous rejouer une autre partie ? Oui/Non\n")
    rejouer = rejouer.upper()
    if rejouer == "NON" or rejouer == "N":
        replay = False
        print("Votre score est de : {} points".format(score))

        sauvegarder = input("\nVoulez-vous sauvegarder cette partie ? Oui/Non\n")
        sauvegarder = sauvegarder.upper()
        if sauvegarder == "OUI" or sauvegarder == "O":
            sauvegarde(prenom, score)
            print("Votre partie a bien été sauvegardée !")

        # if (player() >= 2): """ Faire une fonction qui renvoie le nombre de joueurs """
            # bestPlayer, bestScore = bestOne() """Faire une fonction qui renvoie deux variables : le nom et le score du meilleur joueur """
            # best = input("\nSouhaitez-vous voir le classement des meilleurs joueurs Oui/Non ?\n")
            # best = best.upper()
            # if best == "OUI" or "O":
                # print("Le meilleur joueur est {} avec un score de {} points".format(bestplayer, bestScore / bestOne()))
                # meilleursScores() """ Faire une fonction qui affiche le classement des meilleurs joueurs dans l'ordre décroissant en fonction de leur score """

print("\nCe jeu a été développé par Bernel Dahssi le 02 Novembre\nTous droits réservés. Copyright © 2018")

os.system("pause")
