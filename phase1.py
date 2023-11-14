import argparse
import requests
import json
import datetime


def analyser_commande():
    parser = argparse.ArgumentParser(description= 'Extraction de valeurs historiques pour un ou plusieurs symboles boursiers')
    parser.add_argument('-d', '--début', help="Date recherché la plus ancienne (format: AAAA-MM-JJ)", metavar='DATE', type=datetime.date.fromisoformat)
    parser.add_argument('-f', '--fin', help="Date recherché la plus récente (format: AAAA-MM-JJ)", metavar='DATE', type=datetime.date.fromisoformat)
    parser.add_argument('-v', '--valeur', help="La valeur désirée (par default: fermeture)", choices=['fermeture','ouverture','min','max','volume'])
    parser.add_argument('symbole', nargs='+', help="Nom d'un symbole boursier")
    return parser.parse_args()

print(type(analyser_commande().début))

def produire_historique(symbole, debut, fin, valeur):
    for i in symbole:
        url = f'https://pax.ulaval.ca/action/{i}/historique/'
        params = {'début': debut, 'fin': fin}
        réponse = requests.get(url=url, params=params)
        réponse = json.loads(réponse.text)

        print(f'titre={i}: valeur={valeur}, début={debut}, fin={fin}')


produire_historique(analyser_commande().symbole, analyser_commande().début, analyser_commande().fin, analyser_commande().valeur)

