from functools import reduce

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
valor_emprestimos_filtrado = list(filter(lambda x: x > 0, valor_emprestimos_lista))

# Escreva seu código abaixo

media_valor_emprestimos = reduce(lambda x, y: x + y, valor_emprestimos_filtrado) / len(valor_emprestimos_filtrado)

print(media_valor_emprestimos)
