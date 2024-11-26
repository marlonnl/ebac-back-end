emprestimos = []
with open(file='credito.csv', mode='r', encoding='utf8') as fp:
	fp.readline() # cabeçalho
	linha = fp.readline()
	while linha:
		linha_emprestimo = {}
		linha_elementos = linha.strip().split(sep=',')
		linha_emprestimo['id_vendedor'] = linha_elementos[0]
		linha_emprestimo['valor_emprestimos'] = linha_elementos[1]
		linha_emprestimo['quantidade_emprestimos'] = linha_elementos[2]
		linha_emprestimo['data'] = linha_elementos[3]
		emprestimos.append(linha_emprestimo)
		linha = fp.readline()

valor_emprestimos_lista = list(map(lambda x: float(x['valor_emprestimos']), emprestimos))

# Escreva seu código abaixo

valor_emprestimos_filtrado = filter(lambda x: x > 0, valor_emprestimos_lista)

valor_emprestimos_filtrado_lista = list(valor_emprestimos_filtrado)

print(valor_emprestimos_filtrado_lista)
