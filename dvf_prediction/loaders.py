import os

import pandas as pd

from .definitions import DVF_DIR


def load_dvf(city):
    csv_path = os.path.join(DVF_DIR, "%s.csv" % city)
    return pd.read_csv(csv_path)
