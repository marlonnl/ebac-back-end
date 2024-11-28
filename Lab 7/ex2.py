import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('./dados/dow_jones_index.csv')

df_ko = df[df['stock'] == 'KO']
df_ko = df_ko[['date', 'open', 'high', 'low', 'close']]

for col in ['open', 'high', 'low', 'close']:
	df_ko[col] = df_ko[col].apply(lambda value: float(value.split('$')[-1]))

fig, axs = plt.subplots(1, figsize=(8, 8))

# Insira se código na linha abaixo. Veja a dica para resolver esse exercício
plot = sns.lineplot(x="date", y="value", hue='variable', data=pd.melt(df_ko, ['date']))

plot.tick_params(axis='x', labelrotation=45)

plt.show()
