import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int):
	coluna = []
	# filename = '../../data/' + nome_arquivo

	with open(nome_arquivo, 'r', encoding='utf-8') as f:
		line = f.readline()
		line = f.readline()
		while line:
			value = line.split(',')[indice_coluna]
			coluna.append(value)
			line = f.readline()

	return coluna

valor_manutencao = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=5)
print(valor_manutencao)