import os

def extrai_coluna_csv(nome_arquivo: str, indice_coluna: int, tipo_dado: str):
	coluna = []
	# filename = '../../data/' + nome_arquivo

	with open(nome_arquivo, 'r', encoding='utf-8') as f:
		line = f.readline()
		line = f.readline()
		while line:
			value = line.split(',')[indice_coluna]

			if (tipo_dado == 'str'):
				value = str(value)
			elif (tipo_dado == 'int'):
				value = int(value)

			coluna.append(value)
			line = f.readline()
	
	# leia o arquivo com o comando 'with' utilizando o parametro 'nome_arquivo'.
    # O caminho para o arquivo deve começar com '../../data/'
	# extraia a coluna do arquivo utilizando o parametro 'indice_coluna'
	# use a estrutura de decisão if/elif/else para fazer a conversão do tipo de dados utilizando o parametro 'tipo_dado'

	return coluna

valor_manutencao = extrai_coluna_csv(nome_arquivo='carros.csv', indice_coluna=2, tipo_dado='str')
print(valor_manutencao)
