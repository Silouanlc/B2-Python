#!/usr/bin/python3.6
import os
from random import randrange
import signal
from time import sleep
import re

#generation du nombre aléatoire
genenombre=random.randint(0, 100)

#pour quitter proprement avec ctrl c
def ctrl(sig, frame):
	ecriture("vous avez quittez la partie avec ctrl+c")
	sys.exit(0)

#Fonction qui lis dans du fichier
def lecture():
	file = open(path_file, "r")
	input = file.readline().strip()
	file.close()
	return input

#Fonction qui écrit dans un fichier
def ecriture(msg):
	file = open(path_file, "w")
	file.write(msg)
	file.close()

def aurevoir():
	ecriture("au revoir, la solution était {0}".format(genenombre))

while input != "q":
    input = ecriture()
#Si le nombre est trop petit
        if int(input) < genenombre:
            ecriture("C'est trop petit !")
#Sinon si le nombre est trop grand
        elif int(input) > genenombre:
            ecriture("C'est trop grand !\n")
        else:
            ecriture("Gagné")
            break
aurevoir()
