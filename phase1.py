import argparse


parser = argparse.ArgumentParser(description= 'Extraction de valeurs historiques pour un ou plusieurs symboles boursiers')


parser.add_argument(
    '-m', '--mode',
    metavar='TYPE',
    dest='mode',
    default='type1',
    choices=['type1', 'type2', 'type3', 'type4'],
    help="Une description de ce que représente cet argument",
)

args = parser.parse_args()

