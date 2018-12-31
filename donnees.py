#!/usr/bin/python
# -*- coding: utf-8 -*-

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
    'ALBUM',
    'armoire'.upper(),
    'boucle'.upper(),
    'buisson'.upper(),
    'bureau'.upper(),
    'chaise'.upper(),
    'carton'.upper(),
    'couteau'.upper(),
    'fichier'.upper(),
    'garage'.upper(),
    'glace'.upper(),
    'journal'.upper(),
    'kiwi'.upper(),
    'lampe'.upper(),
    'liste'.upper(),
    'montagne'.upper(),
    'remise'.upper(),
    'sandale'.upper(),
    'taxi'.upper(),
    'vampire'.upper(),
    'volant'.upper(),
]
rMot = str() # rMot = retour après lettre saisie
lettresT = str() # lettresT = lettres déjà trouvées soyus forme de chaîne de caractères
fLettres = list() # liste de lettres saisies ne faisant pas parties du mot à deviner
chances = 8
