# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 17:12:52 2021

@author: Saignol
"""

import param
import os
import shutil
import pandas as pd


'''
Création d'un dossier
'''
def createDir(path):
  if os.path.exists(path):
  	shutil.rmtree(path)
  os.mkdir(path)


# Lecture du CSV
df = pd.read_csv(param.pathInput, sep=param.separatorInput)

# Récupération de la variable colonne fixe
nbCol = param.colVar - 1

# Création du dictionnaire des données
datas = {} 

# Création des données
for i in range(len(df)): # On parcoure le tableau, avec i étant la ligne
  j = 0 # j est la colonne
  list = []
  while j < nbCol: # Tant que j est une colonne qui précéde la colonne fixe
    list.append(str(df.iloc[i, j])) # On ajoute les celules colonne par colonne
    j += 1
  key = '$'.join(list) # On transforme cette list en string avec un séparateur
  
  # On importe ces données dans le dictionnaires
  if key not in datas:
    datas[key] = "$" + str(df.iloc[i, nbCol])
  else:
    datas[key] += "$" + str(df.iloc[i, nbCol])

# Refontes des données
dataFinal = []
for key, value in datas.items():
  string = key + value
  list = string.split('$')
  dataFinal.append(list)

# Création du dataframe à partir du tableau des données
df = pd.DataFrame(dataFinal)

# Export au format CSV sans les noms de colonne
createDir("output")
df.to_csv(param.pathOutput, sep=param.separatorOutput, header=None, index=False)

print("Done", param.pathInput)