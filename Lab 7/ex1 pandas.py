import pandas as pd

df = pd.read_csv('./dados/dow_jones_index.csv')

df_ko = df[df['stock'] == 'KO']
df_ko = df_ko[['date', 'open', 'high', 'low', 'close']]

for col in ['open', 'high', 'low', 'close']:
	df_ko[col] = df_ko[col].apply(lambda value: float(value.split('$')[-1]))

print(df_ko)