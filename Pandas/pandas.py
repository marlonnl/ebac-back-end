import pandas as pd

# Criando um dataframe a partir de um dicionário
venda = {
	'data': ['15/02/2021', '16/02/2021'],
	'valor': [500, 300],
	'produto': ['feijão', 'arroz'],
	'qtde': [50, 70]
}

vendas_df = pd.DataFrame(venda)
# print(vendas_df)

titanic_df = pd.read_csv('titanic.csv')

print(titanic_df) # 10 primeiras linhas da tabela
# print(titanic_df.shape) # (891,12)
# print(titanic_df.describe()) # count, mean, std, min, 25%, 50%, 75%, max

# Pegar apenas uma coluna (pd.Series = uma coluna)
fare = titanic_df['Fare']
# print(fare)

## Para duas colunas
id_e_survived = titanic_df[['PassengerId', 'Survived']]
# print(id_e_survived)


# Metodo loc
# retorna uma linha, linhas de acordo com alguma condicao, linhas e colunas especificas, 1 valor especifico
# df.loc[linha, coluna]

## Uma linha especifica
one_line = titanic_df.loc[0]
two_lines = titanic_df.loc[0:1]

# Pegar linhas de acordo com a condicao
# pegar todos de classe 2 ou mais
coluna = 'Pclass'
classe_2_e_3 = titanic_df.loc[titanic_df[coluna] >= 2]
# print(condicao)

# Pegar várias linhas e colunas
# pegar de quem era 2 ou 3 classe e sobreviveu (1)
filtro = titanic_df.loc[titanic_df[coluna] >= 2, ['Survived', 'Pclass']]
# print(filtro)


# Adicionar coluna

# coluna que ja existe
# titanic_df['Coluna nova'] = titanic_df['Fare'] * 0.5

# coluna com valor padrao
titanic_df.loc[:, 'Coluna nova'] = 0


# Excluir linhas e colunas
# axis = 1 coluna
# axis = 0 linha (default)

titanic_df = titanic_df.drop('Pclass', axis=1)