import pandas as pd

import sys
import os

# Ajouter le répertoire principal au sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def load_data():
    df = pd.read_csv('transformed_data.csv')
