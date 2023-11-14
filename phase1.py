#Valeur de titres boursier 
import argparse
import json
import datetime
import requests

#Analyse de la ligne de commande
def analyser_commande():
    parser = argparse.ArgumentParser(description=
                                     'Extraction de valeurs historiques pour un ou plusieurs symboles boursiers')
    parser.add_argument('-d', '--début', help="Date recherché la plus ancienne (format: AAAA-MM-JJ)", metavar='DATE',
                        type=datetime.date.fromisoformat)
    parser.add_argument('-f', '--fin', help="Date recherché la plus récente (format: AAAA-MM-JJ)", metavar='DATE',
                        type=datetime.date.fromisoformat)
    parser.add_argument('-v', '--valeur', help="La valeur désirée (par default: fermeture)",
                        choices=['fermeture','ouverture','min','max','volume'])
    parser.add_argument('symbole', nargs='+', help="Nom d'un symbole boursier")
    return parser.parse_args()

#Production de l'historique de la bourse
def produire_historique(symbole, debut, fin, valeur):
    if fin is None:
        fin = datetime.date.today()
    if debut is None:
        debut = fin
    if valeur is None:
        valeur = 'fermeture'

    for compagnie in symbole:
        url = f'https://pax.ulaval.ca/action/{compagnie}/historique/'
        params = {'début': debut, 'fin': fin}
        réponse = requests.get(url=url, params=params)
        réponse = json.loads(réponse.text)
        liste = []
        for j in réponse['historique']:
            liste.append(((datetime.datetime.strptime(j, '%Y-%m-%d')).date(), 
                          réponse['historique'][j][valeur]))

    print(f'titre={compagnie}: valeur={valeur}, début={repr(debut)}, fin={repr(fin)}', liste)

args = analyser_commande()
produire_historique(args.symbole, args.début, args.fin, args.valeur)