noticia = 'Selic vai a 2,75% e supera expectativas é a primeira alta em 6 anos.'

selic_position = noticia.find('%')
selic = noticia[selic_position -4:selic_position]

ano_position = noticia.find('anos')
ano = noticia[ano_position -2:ano_position -1]

print(selic)
print(ano)