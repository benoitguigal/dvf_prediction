
import os

import pandas as pd
from matplotlib import pyplot as plt

from .loaders import load_dvf
from .definitions import PLOTS_DIR
from .recipes import remove_outliers, filter_apartment, filter_nbre_lots, \
    add_valeur_fonciere_m2


if not os.path.isdir(PLOTS_DIR):
    os.makedirs(PLOTS_DIR)


def plot_valeur_fonciere_hist(city):
    dvf = load_dvf(city)
    dvf["valeur_fonciere"].hist(bins=50, figsize=(20, 15))
    plt.savefig('foo.png')


def plot_map(city):
    dvf = load_dvf(city)
    dvf = filter_apartment(dvf)
    dvf = filter_nbre_lots(dvf)
    #dvf = dvf[dvf['valeur_fonciere'] < 20000000]
    #dvf = remove_outliers(dvf, 'valeur_fonciere', 1.0)
    dvf = add_valeur_fonciere_m2(dvf)
    dvf = dvf[dvf['valeur_fonciere_m2'] < 30000]
    #dvf = remove_outliers(dvf, 'prix_m2', 1.0)
    map_path = os.path.join(PLOTS_DIR, "%s.png" % city)
    dvf.plot(
        title=city,
        kind="scatter",
        x="longitude",
        y="latitude",
        alpha=0.2,
        figsize=(15, 10),
        c="valeur_fonciere_m2",
        cmap=plt.get_cmap("jet"))
    plt.axis('off')
    plt.savefig(map_path, bbox_inches='tight')
