# csv2omeka

## Présentation

csv2omeka est un outil développé en Python 3 permettant le pivot d’un fichier de données CSV en vue d’un import dans OMEKA. Pour des fichiers comportant une structuration avec le grain page, le script réorganise les données dans une perspective documentaire quel que soit le nombre de colonnes fixes.

Soit un tableau décrivant trois œuvres littéraires et le nombre de page associé :

| AUTEUR         | OEUVRE             | PAGE |
|----------------|--------------------|------|
| Edmond Rostand | Cyrano de Bergerac | 1    |
| Edmond Rostand | Cyrano de Bergerac | 2    |
| Edmond Rostand | Cyrano de Bergerac | 3    |
| Molière        | Le Misanthrope     | 1    |
| Molière        | Le Misanthrope     | 2    |
| Racine         | Bérénice           | 1    |
| Racine         | Bérénice           | 2    |
| Racine         | Bérénice           | 3    |

L’import dans OMEKA nécessite que les données de la colonne « PAGE » pivotent et soient sur la même ligne.

| AUTEUR         | OEUVRE             | PAGE | PAGE | PAGE |
|----------------|--------------------|------|------|------|
| Edmond Rostand | Cyrano de Bergerac | 1 | 2 | 3 |
| Molière        | Le Misanthrope     | 1 | 2 |   |
| Racine         | Bérénice           | 1 | 2 | 3 |

csv2omeka réalise cette conversion et ce quel que soit le nombre de « colonne fixe », ici les métadonnées « AUTEUR » et « OEUVRE ».

## Installation

csv2omeka nécessite une installation Python 3 avec la version 1.2.3 du package Pandas.

Pour vérifier les packages installées :
    
    pip freeze

Pour installer les packages manquants :

    pip install -r path\\to\requirements.txt
    
avec le chemin correspondant au fichier requirements.txt présent dans cet outil.

## Usage

Le fichier « param.py » comporte plusieurs paramètres à configurer suivant les besoins du projet :

* « pathInput » qui fournit le chemin du fichier d’entrée. L’outil comporte par défaut un répertoire « input ».
* « separatorInput » qui définie le séparateur du fichier CSV en entrée. La valeur par défaut est la virgule.
* « colVar » qui indique le numéro de la colonne variable. Dans le fichier « test.csv », il s’agit de la colonne numéro 3.
* « pathOutput » qui fournit le chemin du fichier de sortie. L’outil crée par défaut un répertoire « output » pour l’accueillir.
* « separatorOutput » qui définie le séparateur du fichier CSV en sortie. La valeur par défaut est la virgule.

Une fois les paramètres configurés, importer le fichier CSV dans le répertoire « input ».

Exécuter le fichier « csv2omeka.py ».
