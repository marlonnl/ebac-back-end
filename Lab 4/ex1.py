valor_venda = []

with open(file='carros.csv', mode='r', encoding='utf8') as arquivo:
	linha = arquivo.readline()
	linha = arquivo.readline()
	while linha:
		valor = linha.split(',')[1]
		valor_venda.append(valor)
		linha = arquivo.readline()

	print(valor_venda)
