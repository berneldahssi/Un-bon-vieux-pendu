#!/usr/bin/python
# -*- coding: utf-8 -*-

def vLettre(x):
    """"Fonction qui se rassure que l'utilisateur saisit bien
une seule lettre"""

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while not(x.__len__() == 1 and x.upper() in alphabet):
        x = input("\nSVP veuillez entrer une lettre ! :  ")
    x = x.upper()
    return x


def rTLettre(x, mot, lettresT):
    """Fonction qui retourne le mot lorsque l'utilisateur
saisit une lettre contenue dans le mot à deviner"""

    lettresT = x + lettresT
    rMot = str()
    for i in mot:
        if i == x:
            rMot = rMot + i
        elif i in lettresT:
            rMot = rMot + i
        else:
            rMot = rMot + "*"
    return rMot, lettresT


def rFLettre(x, mot, lettresT, fLettres):
    """Fonction qui retourne le mot lorsque l'utilisateur
saisit une lettre qui n'est pas dans le mot à deviner"""

    fLettres.append(x)
    rMot = str()
    for i in mot:
        if i == x:
            rMot = rMot + i
        elif i in lettresT:
            rMot = rMot + i
        else:
            rMot = rMot + "*"
    return rMot


def sauvegarde(prenom, score):
    """Fonction qui enregistre le score et le prenom du joueur
dans un fichier sous forme de dictionnaire"""

    import pickle
    prenom = prenom.upper()
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scores = monDepickler.load()
        scores[prenom] = score
    with open('scores', 'wb') as fichier:
        monPickler = pickle.Pickler(fichier)
    with open('scores', 'wb') as fichier:
        monPickler = pickle.Pickler(fichier)
        monPickler.dump(scores)


def vSauvegarde(prenom):
    """Fonction qui vérifie si un joueur a une sauvegarde à son
nom"""

    import pickle
    prenom = prenom.upper()
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scores = monDepickler.load()
        for i in scores.keys():
            if i == prenom:
                return True
            else:
                return False


def restauration(prenom):
    """Fonction qui vérifie si un joueur a une sauvegarde à son
nom"""

    import pickle
    prenom = prenom.upper()
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scores = monDepickler.load()
        for i in scores.keys():
            if i == prenom:
                return scores[prenom]
            else:
                score = int()
                return score


def delSauvegarde(prenom):
    """"Fonction qui écrase la sauvegarde d'un joueur pour lui
permettre de jouer une nouvelle partie"""

    import pickle
    prenom = prenom.upper()
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
    with open('scores', 'rb') as fichier:
        monDepickler = pickle.Unpickler(fichier)
        scores = monDepickler.load()
        del scores[prenom]
    with open('scores', 'wb') as fichier:
        monPickler = pickle.Pickler(fichier)
    with open('scores', 'wb') as fichier:
        monPickler = pickle.Pickler(fichier)
        monPickler.dump(scores)


# def player(scores):
    # """ Faire une fonction qui renvoie le nombre de joueurs """




# def bestOne(scores):
    # """Faire une fonction qui renvoie deux variables : le nom et le score du meilleur joueur"""




# def meilleursScores(scores):
    # """ Faire une fonction qui affiche le classement des meilleurs joueurs dans l'ordre décroissant en fonction de leur score """
