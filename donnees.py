#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice

listeMots = [
    'FAMILLE',
    'TIRROIR',
    'MAISON',
    'COUVERCLE',
    'CONSOLE',
    'ORDINATEUR',
    'NEUROCHIRURGIE',
    'PROGRAMMATION',
    'EVOLUTION',
    'ALBUM'
]
rMot = str() # rMot = retour après lettre saisie
lettresT = str() # lettresT = lettres déjà trouvées soyus forme de chaîne de caractères
fLettres = list() # liste de lettres saisies ne faisant pas parties du mot à deviner
chances = 8
