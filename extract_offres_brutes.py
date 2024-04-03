#############################
# URL de base pour liste des offres dispo: https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles=&page=
# Paramètres à fournir : mots clés et numéro de page (commence à partir de 0)
# "typesConvention" apparait en auto après chargement de  page, mais n 'est pas utile pour l'URL
#############################

from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driverService = Service(r'C:\Users\myuseraccount\anaconda3\geckodriver.exe')
# obligé de passer par selenium car page dynamique générée par Javascript, ne marche pas
# avec requests ou html-requests

driver = webdriver.Firefox(service=driverService, options=options)

url_page_defaut = "https://www.apec.fr/candidat/recherche-emploi.html/emploi?motsCles="

def trouver_page_max(motscles, url_page=url_page_defaut):
    # On met un numéro de page très élevé car l'APEC affiche le numéro de page max si le paramètre fourni
    # dans la requête dépasse le nombre de page dispo
    driver.get(f"{url_page}{motscles}&page=1000000")
    soup_page = bs(driver.page_source, "lxml")

    # Le numéro de page actif est le numéro de page max
    num_page_max = int(soup_page.select(".page-item.active")[0].text)
    return num_page_max

def extract_liste_offres(motscles, num_page_max, url_page=url_page_defaut):
    liste_liens = []

    #Rappel : Les numéros de pages commencent à l'index 0
    for num_page in range(0, num_page_max):
        driver.get(f"{url_page}{motscles}&page={num_page}")

        # On génère une attente de 5s sinon les données analysées par bs4 n'étaient pas complètes --> temps optimisable ?
        time.sleep(2)

        # pour faire un suivi vue la durée du process
        print(f"Traitement en cours de la page n°{num_page}")
        soup_page = bs(driver.page_source, "lxml")
        page_offres = soup_page.select(".container-result a")

        #L'affichage standard est de 20 offres par page
        offres_par_page = 20


        for i in range(0, offres_par_page):
            if page_offres[i].get("href") is not None:
                liste_liens.append(page_offres[i].get("href"))

            else:
                print(f"\nDernière offre atteinte !\n {len(liste_liens)} liens vers des offres d'emploi",
                "correspondant à vos mots-clés ont été récupérés.\n")
                break
    return liste_liens

#############################
#
# URL mini page d'offres : https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/
# Suivi par numéro de l'offre d'emploi
# Le numéro de l'offre n'apparait que dans div class=container-result puis / <div> /<a href>
#############################
def extract_detail_offres(liste_liens):
    liste_offres = []

    for i, offres in enumerate(liste_liens):
        url_offre = "https://www.apec.fr"
        driver.get(f"{url_offre}{offres}")

        # time.sleep sinon les données analysées par bs4 n'étaient pas complètes
        time.sleep(2)

        #on ne récupère que la partie card-body qui contient toutes les infos de l'offre avec ses métadonnées
        soup_page_body = bs(driver.page_source, "lxml").select(".card-body")

        liste_offres.append(soup_page_body)

        # pour faire un suivi d'avancement vue la durée du process
        print(f"Traitement terminé pour l'offre N°{i+1}/{len(liste_liens)}")

    return liste_offres