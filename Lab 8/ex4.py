class Pessoa(object):
	def __init__(self, nome: str, idade: int, documento: str):
		self.nome = nome
		self.idade = idade
		self.documento = documento

andre = Pessoa(nome="Andre", idade=30, documento="123")