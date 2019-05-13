
import numpy as np
import pandas as pd


def remove_outliers(df):
    valeur_fonciere_m2 = df['valeur_fonciere_m2']
    df = df[valeur_fonciere_m2 <= 30000]
    mean = valeur_fonciere_m2.mean()
    std = valeur_fonciere_m2.std()
    return df[np.abs(valeur_fonciere_m2 - mean) <= 2 * std]


def filter_apartment(df):
    return df[df['type_local'] == 'Appartement']


def filter_nbre_lots(df):
    return df[df['nombre_lots'] == 1]


def add_valeur_fonciere_m2(df):
    df['valeur_fonciere_m2'] = df['valeur_fonciere'] / df['lot1_surface_carrez']
    return df


def add_year(df):
    dt = pd.to_datetime(df['date_mutation'], infer_datetime_format=True)
    df['year'] = dt.map(lambda x: x.year)
    return df


def keep_columns(df, columns):
    return df[columns]
