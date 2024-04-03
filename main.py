'''

# APEC Python Job Extractor
L'objectif du programme est d'extraire les 10 champs lexicaux les plus remontés dans les offres de l'APEC (Agence
Pour l'Emploi des Cadres en France) afin de pouvoir ressortir les compétences clés les plus demandées
 sur le marché du travail pour des mots-clés donnés.
'''

### Besoin
#    1. Analyser l'url de l'APEC où récupérer l'info
#    2. Analyser le code source de la page web pour trouver le lien vers les offres d'emplois
#    3. Déterminer le nombre de pages
#    4. Scanner toutes les pages pour récupérer les liens vers toutes les offres d'emplois dans une liste_liens
#    5. Analyser les pages des offres d'emplois pour récupérer le bloc avec les infos importantes. Cela
#    permettra d'avoir la totalité des données si l'on souhaite extraire d'autresq informations plus tard
#    (salaire, ville, expérience...)
#    6. Ajouter les données de chaque offre dans une liste_offres
#    7. Extraire les données de liste_offres pour créer une liste_imp_infos avec seulement "descriptif du poste" et
#     "profil recherché"


import extract_offres_brutes

print("\n\nL'objectif du programme est d'extraire les 10 champs lexicaux les plus remontés dans les offres de l'APEC",
      "afin de pouvoir ressortir les compétences clés les plus demandées sur le marché du travail pour",
      "une recherche donnée.\n\n")

user_input = input("Quel(s) mots-clés recherchez-vous ?\n")

#récupération du nombre de page max
page_max = extract_offres_brutes.trouver_page_max(motscles=user_input)

#Récupération de la liste des liens vers toutes les offres d'emploi
liste_liens_offres = extract_offres_brutes.extract_liste_offres(motscles=user_input, num_page_max=page_max)

#Récupération des détails de chaque offre d'emploi
liste_offres_detaillees = extract_offres_brutes.extract_detail_offres(liste_liens_offres)

#Sauvegarde des offres au format txt pour exploitation plus tard
with open("sauvegarde_offres_python.txt", "w+", encoding='utf8') as f:
    for elements in liste_offres_detaillees:
        f.write(str(elements))
        f.write("\n\n\n----------------------------------------------------------------------------------\n\n\n")
        f.write("\n\nOFFRE SUIVANTE\n\n")
        f.write("\n\n\n----------------------------------------------------------------------------------\n\n\n")

