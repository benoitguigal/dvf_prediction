
import os
from urllib.parse import urljoin

import requests
import pandas as pd

from .definitions import DVF_DIR
from .communes import get_code_commune

DVF_BASE_URL = 'https://cadastre.data.gouv.fr/data/etalab-dvf/latest/csv/'


if not os.path.isdir(DVF_DIR):
    os.makedirs(DVF_DIR)

years = ['2016', '2017', '2018']


def fetch_dvf_for_city(city):
    codes_commune = get_code_commune(city)
    dvfs = []
    for year in years:
        for code_commune in codes_commune:
            department = code_commune[:2]
            dvf = fetch_dvf(year, department, code_commune)
            dvfs.append(dvf)
    file_path = os.path.join(DVF_DIR, "%s.csv" % city)
    pd.concat(dvfs).to_csv(file_path)


def fetch_dvf(year, department, code_commune):
    filename = "%s.csv" % code_commune
    filepath = os.path.join(
        str(year),
        'communes',
        str(department),
        filename)
    url = urljoin(DVF_BASE_URL, filepath)
    return pd.read_csv(url)
