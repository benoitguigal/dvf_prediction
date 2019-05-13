
import itertools

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

from .loaders import load_dvf
from .recipes import filter_apartment, filter_nbre_lots, \
    add_valeur_fonciere_m2, keep_columns, remove_outliers, \
    add_year


def run():

    #dvf = load_dvf('paris')
    dvf = load_dvf('paris')

    # keep only records for apartment
    dvf = filter_apartment(dvf)

    # keep only records where there is only one "lot"
    dvf = filter_nbre_lots(dvf)

    # compute valeur_fonciere_by_m2
    dvf = add_valeur_fonciere_m2(dvf)

    # remove outliers
    dvf = remove_outliers(dvf)

    # add year
    dvf = add_year(dvf)

    # select specific columns
    columns = [
        'valeur_fonciere',
        'latitude',
        'longitude',
        'lot1_surface_carrez',
        'nombre_pieces_principales',
        'year'
    ]
    dvf = keep_columns(dvf, columns)

    train_set, test_set = train_test_split(dvf, test_size=0.2, random_state=42)

    dvf = train_set.drop("valeur_fonciere", axis=1)
    dvf_labels = train_set["valeur_fonciere"].copy()

    imputer = SimpleImputer(strategy="median")

    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
    ])

    dvf_prepared = pipeline.fit_transform(dvf)

    lin_reg = LinearRegression()
    lin_reg.fit(dvf_prepared, dvf_labels)

    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(dvf_prepared, dvf_labels)

    forest_reg = RandomForestRegressor(random_state=42)
    forest_reg.fit(dvf_prepared, dvf_labels)

    def display_scores(scores):
        print('Scores: ', scores)
        print('Mean: ', scores.mean())
        print('Standard Deviation: ', scores.std())

    # scores = cross_val_score(
    #     tree_reg,
    #     dvf_prepared,
    #     dvf_labels,
    #     scoring="neg_mean_squared_error",
    #     cv=10)

    # tree_rmse_scores = np.sqrt(-scores)


    # print("Decision Tree")
    # display_scores(tree_rmse_scores)
    # print("\n")

    # scores = cross_val_score(
    #     lin_reg,
    #     dvf_prepared,
    #     dvf_labels,
    #     scoring="neg_mean_squared_error",
    #     cv=10)

    # lin_rmse_scores = np.sqrt(-scores)

    # print("Linear")
    # display_scores(lin_rmse_scores)
    # print("\n")

    # scores = cross_val_score(
    #     forest_reg,
    #     dvf_prepared,
    #     dvf_labels,
    #     scoring="neg_mean_squared_error",
    #     cv=10)

    # forest_rmse_scores = np.sqrt(-scores)
    # print("Random Forest")
    # display_scores(forest_rmse_scores)
    # print("\n")

    longchamp = {
        'latitude': [48.878695],
        'longitude': [2.372154],
        'lot1_surface_carrez': [30.0],
        'nombre_pieces_principales': [1.0],
        'year': [2017]
    }

    longchamp_df = pd.DataFrame.from_dict(longchamp)

    #longchamp_df = dvf.iloc[:5]
    print(longchamp_df.info())

    longchamp_df_prepared = pipeline.transform(longchamp_df)

    longchamp_prediction = forest_reg.predict(longchamp_df_prepared)

    print("Longchamp prediction: ", longchamp_prediction)

