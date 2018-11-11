
#!/usr/bin/python3.6
#1a-add.py
#afficher l addition de deux nombre
#Le Cossec Silouan
#15/10/2018

num2 = input('entre le deuxiemes nombre')
num1 = input('Entre le premier nombre: ')
#mon tabl
L = ['0','1','2','3','4','5','6',7','8','9']
#si le nb 1 est dans mon tableau
if num1 in L:
  sum = float(num1) + float(num2)
  print('le total de {0} et de  {1} est {2}'.format(num1, num2, sum))
#copie du num1
if num2 in L:
  sum = float(num1) + float(num2)
  print('le total de {0} et de  {1} est {2}'.format(num1, num2, sum))

else:
  print('ceci n\'est pas un nombre')
