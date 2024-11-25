import os

def extrai_linha_txt(nome_arquivo: str, numero_linha: int):

	palavras_linha = []

	with open(nome_arquivo, 'r', encoding='utf-8') as f:
		line = f.readlines()
		palavras_linha = line[numero_linha-1].split(' ')

	return palavras_linha

linha10 = extrai_linha_txt(nome_arquivo='musica.txt', numero_linha=10)
print(linha10)