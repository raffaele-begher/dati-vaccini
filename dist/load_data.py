import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style
import git
import whatsapp

# Update dataset
repo = git.Repo('covid19-opendata-vaccini')
repo.remotes.origin.pull()

# Init variables
tot_prime_dosi = 0
tot_seconde_dosi = 0

# setting style for graphs
style.use('ggplot')
plt.rcParams['figure.figsize'] = (20,10)

# Estrai csv e converti 'data_somminstrazione' in formato datetime
df = pd.read_csv('covid19-opendata-vaccini/dati/somministrazioni-vaccini-latest.csv')
df['data_somministrazione'] = pd.to_datetime(df.data_somministrazione)

# Seleziona dati nel DataFrame
dati = df[['data_somministrazione', 'prima_dose', 'seconda_dose']]
dati = dati.groupby('data_somministrazione', as_index = False)['prima_dose', 'seconda_dose'].sum()
dati.set_index('data_somministrazione')

# Aggiungi colonna somma prime e seconde dosi
dati['totale_somministrazioni'] = dati['prima_dose'] + dati['seconda_dose']

# Stampa grafico e salva immagine
x = dati.data_somministrazione
y = dati.totale_somministrazioni
# y = dati.prima_dose
print(dati)
msg_body = dati.tail(5).to_string()
whatsapp.send_msg(msg_body)
plt.xlabel('Data Somministrazione')
plt.ylabel('Dosi Somministrate')
plt.title('Vaccinazioni COVID-19')
#plt.figure(figsize=(16, 8), dpi=80)
plt.bar(x, y, color = 'blue')
plt.savefig('prime_dosi.png')
#plt.show()
