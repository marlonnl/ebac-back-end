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

# Escreva seu código abaixo

valor_emprestimos_map = map(lambda emprestimo: float(emprestimo['valor_emprestimos']), emprestimos)

valor_emprestimos_lista = list(valor_emprestimos_map)

print(valor_emprestimos_lista)
