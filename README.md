# APEC EXTRACTOR
Le but de ce programme est de pouvoir récupérer les offres d'emplois diffusées sur le site web de l'APEC (Agence Pour l'Emploi des Cadres) 
en France pour un ensemble de mots-clés donné afin de pouvoir analyser les compétences recherchées, les entreprises qui recrutent,
les lieux, etc. Il s'agit donc d'un webscrapper avec un peu de data science.

## Fonctionnement pour la V1.0 : 
  - Apec Extractor vous demande d'abord les mots-clés que vous recherchez. Vous pouvez utiliser plusieurs mots-clés séparés par des
espaces comme sur le module recherche du site de l'APEC.
  - A partir de ces mots-clés, il va récupérer le nombre de pages max qu'il doit parcourir
  - Ensuite, il récupère sur chaque page les liens vers les offres qu'ils stockent dans un tableau
  - Puis, le programme parcourt l'ensemble des liens pour récupérer la section "card-body" contenant toutes les données pour chaque
offre d'emploi
  - Finalement Apec Extractor sauvegarde l'ensemble des données sources récupérées au format html dans un fichier .txt pour analyse
ultérieure

### !!!
  Pensez à modifier le constructeur Service(r'C:\Users\myuseraccount\anaconda3\geckodriver.exe') dans extract_offres_brutes.py avec
le chemin d'accès vers votre moteur Gecko pour que le programme soit fonctionnel.

  Comme tout webscrapper, une évolution de la structure du site web de l'APEC peut nécessiter une mise à jour du programme. A date,
c'est-à-dire au **3 avril 2024**, tout marche correctement.
### !!!

## A venir dans la V2.0 :
- création d'une classe Offre pour favoriser la structuration des données recueillies pour chaque offre et faciliter leur analyse

## Idées à développer ultérieurement:
- Ajouter de la visualisation sur les différentes métadonnées récupérées en utilisant seaborn
- Analyse du profil et des compétences demandées en utilisant du text mining
