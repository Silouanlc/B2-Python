#!/usr/bin/python3.6
import os
from random import randrange
import signal
from time import sleep
import re
import random
import sys

regex = re.compile('[0-9]')

#generation du nombre aléatoire
genenombre=random.randint(0, 100)

#pour quitter proprement avec ctrl c
def end_game(sig, frame):
    ecrire('quitter avec CTRL+C ')
    exit()
signal.signal(signal.SIGINT, end_game)

#on lit dans le fichier texte
def lire():
    file = open("jeu.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg

# Fonctions qui écrire une réponse dans le fichier texte
def ecrire(msg):
    file = open("jeu.txt", "w")
    file.write(msg)
    file.close()

#message de bienvenu
ecrire('Entrez un nombre entre 0 et 100 !')

def jeux(finBoucle):
    while(finBoucle is False):
        saisie = lire()

        if(regex.match(saisie)):
            saisie = int(saisie)

            if(saisie > genenombre):
                ecrire("C'est moins")

            elif(saisie < genenombre):
                ecrire("C'est plus")
            else:
                ecrire('Felicitation\nLa solution etait '+str(genenombre)+'\nAu revoir !')
                finBoucle = True
finBoucle = False
jeux(finBoucle)
