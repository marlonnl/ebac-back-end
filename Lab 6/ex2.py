import sys
sys.path.insert(0, '/data')
# from arquivo_texto import ArquivoTexto
from ex1 import ArquivoTexto

class ArquivoCSV(ArquivoTexto):

	def __init__(self, arquivo: str):
		super().__init__(arquivo=arquivo)
		self.colunas = self.extrair_nome_colunas()

	def extrair_nome_colunas(self) -> list[str]:
		return list(self.conteudo[0].split(','))

	def extrair_coluna(self, indice_coluna: int) -> list[str]:
		return list(map(lambda x: x.split(',')[indice_coluna-1], self.conteudo[1:]))

arquivocsv = ArquivoCSV('arquivocsv.csv')