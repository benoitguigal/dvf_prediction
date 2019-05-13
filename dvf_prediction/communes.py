import os
import pandas as pd

from .definitions import ROOT_DIR


code_commune_path = os.path.join(
    ROOT_DIR,
    'data',
    'communes.csv')
code_commune = pd.read_csv(code_commune_path, sep=";")


def get_code_commune(city):
    df = code_commune[
        code_commune['Libelle_acheminement'].str.lower() == city.lower()]
    return list(df['Code_commune_INSEE'].values)
