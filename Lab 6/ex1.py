class ArquivoTexto(object):
	def __init__(self, arquivo: str):
		self.arquivo = arquivo
		self.conteudo = self.extrair_conteudo()
	
	def extrair_conteudo(self):
		with open(self.arquivo, 'r', encoding='utf-8') as f:
			return f.read().splitlines()

	def extrair_linha(self, numero_linha: int):
		return self.conteudo[numero_linha -1]

musica = ArquivoTexto('musica.txt')
print(musica.conteudo)
