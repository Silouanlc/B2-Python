#!/usr/bin/python3.6
#d-mo.py
#jeux du plus ou moins
#Le Cossec Silouan
#23/10/2018

import os
from random import randrange
import signal
from time import sleep
import re

#pour quitter proprement avec ctrl c
def controlc(sig, frame):
    print('va y')
    exit()
signal.signal(signal.SIGINT, controlc)


zqsd = re.compile('^[1-9]?[0-9]{1}$|^100$')

genenombre = ""
nombreadeviner = randrange(0, 100)
genenombre = input("Quel est le nombre ?")

#fonction au revoir pour afficher la soluce lorsque  l on quitte
def aurevoir():
    return print("au revoir, la solution était {0}".format(nombreadeviner))


while genenombre != "q":
    if zqsd.match(genenombre):
        if int(genenombre) < nombreadeviner:
    #Si le nombre est trop petit
            print("C'est trop petit !")
            genenombre = input("Quel est le nombre ?")
    #Sinon si le nombre est trop grand
        elif int(genenombre) > nombreadeviner:
            print("C'est trop grand !\n")
            genenombre = input("Quel est le nombre ?")

        else:
            print("Gagné")
            break
    else:
        print("verifie que tu as bien rentré un nombre")
        genenombre = input("Quel est le nombre ?")
aurevoir()
