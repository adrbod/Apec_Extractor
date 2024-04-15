import csv


from bs4 import BeautifulSoup as bs

class Offre:

    def __init__(self, titre, contrat, entreprise, reference, localisation, source_page, salaire, prise_de_poste, experience, metier,
                 statut, zone_deplacement, secteur, teletravail, descriptif, profil):

        self.titre = titre
        self.entreprise = entreprise
        self.contrat = contrat
        self.reference = reference
        self.localisation = localisation
        self.source_page = source_page
        self.salaire = salaire
        self.prise_de_poste = prise_de_poste
        self.experience = experience
        self.metier = metier
        self.statut = statut
        self.zone_deplacement = zone_deplacement
        self.secteur = secteur
        self.teletravail = teletravail
        self.descriptif = descriptif
        self.profil = profil

def traiter_offres(liste_page_offres):
    '''
    r fonction qui transforme une liste de page d'offres d'emploi en objet Offres, pour utilisation en post-traitement
    :param liste_offres: tableau contenant les codes sources affinés (body-card seulement) de chaque offre d'emploi
    :return: une liste d'objet de classe Offre
    '''

    liste_offres_traitees = []

    for i, offres in enumerate(liste_page_offres):
        titre = offres.select("h1")[0].text
        reference = offres.select(".ref-offre")[0].text

        localisation = offres.select(".details-offer-list.mb-20 li")[-1].text
        contrat = offres.select(".details-offer-list.mb-20 li")[-2].text

        #Il arrive que les entreprises ne soient pas précisées (cas des offres qui renvoient à des Jobboards)
        if len(offres.select(".details-offer-list.mb-20 li")) == 3:
            entreprise = offres.select(".details-offer-list.mb-20 li")[-3].text
        else:
            entreprise = "NA"


        source_page = offres
        salaire = offres.select(".col-lg-4 .details-post span")[0].text
        prise_de_poste = offres.select(".col-lg-4 .details-post span")[1].text
        experience = offres.select(".col-lg-4 .details-post span")[2].text
        metier = offres.select(".col-lg-4 .details-post span")[3].text
        statut = offres.select(".col-lg-4 .details-post span")[4].text
        zone_deplacement = offres.select(".col-lg-4 .details-post span")[5].text
        secteur = offres.select(".col-lg-4 .details-post span")[6].text

        #Les possibilités de télétravail ne sont pas toujours indiquées sur les offres
        try:
            teletravail = offres.select(".col-lg-4 .details-post h4")[7].text
        except:
            teletravail = "NA"

        #L'accès au descriptif du poste et au profil demandé demande de rentrer plus profondément dans la hiérarchie de
        # la page. Ces données n'étant pas structurées avec des classes bien définies, il faut utiliser des astuces
        # détournées pour récupérer les blocs de texte du panneau central qui contiennent le descriptif de l'offre
        # ainsi que le profil, les compétences recherchées ou encore la description de l'entreprise demandeuse
        detail_post_centre = offres.select(".col-lg-8 .border-L .details-post")[0]

        #on souhaite isoler les blocs de texte entre 2 balise <h4> qui identifient les sections importantes
        # du panneau central

        h4_modif = str(detail_post_centre).replace("<h4>", "!separator!").replace("</h4>", "!separator!")

        #on réinjecte le texte modifié dans beautifulSoup pour pouvoir utiliser la méthode get_text et avoir un rendu
        # propre, débarrasser des balises HTML
        soup_panneau_ctrl = bs(h4_modif, "html.parser")

        # on découpe le texte obtenu en utilisant le séparateur
        liste_blocs_panneau_ctrl = soup_panneau_ctrl.get_text(separator="\n").split("!separator!")

        #le bloc texte du Descriptif de l'offre est toujours à l'index 2 et le profil à l'index 4

        descriptif = liste_blocs_panneau_ctrl[2]
        profil = liste_blocs_panneau_ctrl[4]

        liste_offres_traitees.append(Offre(titre, contrat, entreprise, reference, localisation, source_page, salaire, prise_de_poste,
                   experience, metier,statut, zone_deplacement, secteur, teletravail, descriptif, profil))


        print(f"Offre {i+1}/{len(liste_page_offres)} traitée !")
    print("-------------------------------------------------")
    print("\nL'ensemble des offres trouvées a été traité !\n")

    return liste_offres_traitees
