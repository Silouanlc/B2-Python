#!/usr/bin/python36
# plus ou moins
# plus ou moins auto
# 08/11
# Le Cossec

from random import randint
import os
from random import randrange
import signal
from time import sleep
import re
import random
import sys
import signal

#on lit dans le fichier texte
def lire():
    file = open("jeu.txt", "r")
    msg = file.readline().strip()
    file.close()
    return msg

nombrebCoups = 0
min = 0
max = 100
resultat = ''

def trynumber(min, max):
  return int((max + min)  / 2)


# Fonctions qui écrire une réponse dans le fichier texte
def ecrire(msg):
    file = open("jeu.txt", "w")
    file.write(msg)
    file.close()

#on affiche le plus ou moins
def check():
  if (found == trying):
    return 'Gagné'
  elif (trying < found):
    return 'C est plus'
  else:
    return 'C est moins'


found = randint(min, max)
trying = -1

while (resultat != 'Gagné'):
  trying = trynumber(min, max)
  resultat = check()
  if(resultat == 'C est plus'):
    min = trying
  elif(resultat == 'C est moins'):
    max = trying
  nombrebCoups += 1

#msg de fin avec affichage du nb de coup
ecrire('Le bot a trouvé en ' + str(nombrebCoups) + ' essai')
