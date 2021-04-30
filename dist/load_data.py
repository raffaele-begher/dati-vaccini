import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style
import git

# Update dataset
def update_dataset():
    repo = git.Repo('../covid19-opendata-vaccini')
    repo.remotes.origin.pull()

# setting style for graphs
def set_styles():
    style.use('ggplot')
    plt.rcParams['figure.figsize'] = (20,10)

# Estrai csv e converti 'data_somminstrazione' in formato datetime
def get_data():
    df = pd.read_csv('../covid19-opendata-vaccini/dati/somministrazioni-vaccini-latest.csv')
    df['data_somministrazione'] = pd.to_datetime(df.data_somministrazione)

    """Seleziona dati nel DF"""
    dati = df[['data_somministrazione', 'prima_dose', 'seconda_dose']]
    dati = dati.groupby('data_somministrazione', as_index = False)['prima_dose', 'seconda_dose'].sum()
    dati.set_index('data_somministrazione')

    """Aggiungi colonna somma prime e seconde dosi"""
    dati['totale_somministrazioni'] = dati['prima_dose'] + dati['seconda_dose']

    x = dati.data_somministrazione
    y = dati.totale_somministrazioni

    matplotlib.use('agg')
    plt.xlabel('Data Somministrazione')
    plt.ylabel('Dosi Somministrate')
    plt.title('Vaccinazioni COVID-19')
    plt.bar(x, y, color = 'blue')
    plt.savefig('vax-die.png')

    msg_body = dati.tail(5).to_string()
    return msg_body


