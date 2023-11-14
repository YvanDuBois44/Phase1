import argparse


parser = argparse.ArgumentParser(description= 'Extraction de valeurs historiques pour un ou plusieurs symboles boursiers')


parser.add_argument('-d', '--début',help="Date recherché la plus ancienne (format: AAAA-MM-JJ)", metavar='DATE')
parser.add_argument('-f', '--fin',help="Date recherché la plus récente (format: AAAA-MM-JJ)", metavar='DATE')
parser.add_argument('-v', '--valeur',help="La valeur désirée (par default: fermeture)", metavar={'fermeture', 'ouverture', 'min', 'max', 'volume'})


'''
parser.add_argument(
    '-m', '--mode',
    metavar='TYPE',
    dest='mode',
    default='type1',
    choices=['type1', 'type2', 'type3', 'type4'],
    help="Une description de ce que représente cet argument",
)
'''

args = parser.parse_args()

