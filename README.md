# Projet2\_BureauEnGros



\# Projet 2 — Web Scraping Bureau en Gros



\## Description

Ce projet consiste à extraire des informations sur les produits informatiques du site Bureau en Gros, à nettoyer les données avec Python et à les importer dans CouchDB pour effectuer des recherches et des analyses.



\## Technologies utilisées

\- WebScraper

\- Python

\- CouchDB

\- Docker

\- Git et GitHub



\## Extraction des données

Les données ont été extraites du site Bureau en Gros à l'aide de l'extension Chrome webScraper.



Site utilisé :

https://www.bureauengros.com/collections/fr-ordinateurs-89



Le fichier `bureauengros\_brut.csv` contient les données originales.



\## Nettoyage des données

Le script `nettoyage.py` permet de :

\- Nettoyer les espaces inutiles.

\- Convertir les prix en valeurs numériques.

\- Générer un identifiant unique pour chaque produit.

\- Vérifier les doublons.

\- Produire le fichier `donnees.json`.



Après nettoyage, 2505 produits ont été conservés.



\## Base de données CouchDB

Les 2505 produits ont été importés dans la base de données `projet2\_bureauengros`.



\## Requêtes

Le dossier `requetes` contient :

\- `requete1\_filtre.json` : filtre les produits par prix et processeur.

\- `requete2\_tri.json` : affiche les 10 produits les moins chers.

\- `requete3\_mapreduce.json` : compte les produits par tranche de prix.

\- `index\_prix.json` : définit un index sur le prix.



\## Exécution

1\. Installer Python et les bibliothèques nécessaires au script.

2\. Placer `bureauengros\_brut.csv` et `nettoyage.py` dans le même dossier.

3\. Exécuter `python nettoyage.py`.

4\. Démarrer CouchDB.

5\. Créer une base de données nommée `projet2\_bureauengros`.

6\. Importer les documents de `donnees.json` avec l'API `\_bulk\_docs` de CouchDB, après les avoir placés dans un objet JSON contenant la clé `docs`.

7\. Exécuter les requêtes Mango et créer la vue MapReduce.



\## Résultat

Le projet a permis de récupérer et de nettoyer 2505 produits informatiques, puis d'effectuer des recherches et des statistiques avec CouchDB.



