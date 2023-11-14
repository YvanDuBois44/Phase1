import argparse



def analyser_commande():
    parser = argparse.ArgumentParser(description= 'Extraction de valeurs historiques pour un ou plusieurs symboles boursiers')
    parser.add_argument('-d', '--début',help="Date recherché la plus ancienne (format: AAAA-MM-JJ)", metavar='DATE')
    parser.add_argument('-f', '--fin',help="Date recherché la plus récente (format: AAAA-MM-JJ)", metavar='DATE')
    parser.add_argument('-v', '--valeur',help="La valeur désirée (par default: fermeture)", choices=['fermeture','ouverture','min','max','volume'])
    parser.add_argument('symbole', nargs='+', help="Nom d'un symbole boursier")
    return parser.parse_args()


def produire_historique(symbole, debut, fin, valeur)
analyser_commande()