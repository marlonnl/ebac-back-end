import wget
import zipfile
import os

wget.download(url='https://archive.ics.uci.edu/ml/machine-learning-databases/00312/dow_jones_index.zip', out='./dados.zip')

with zipfile.ZipFile('./dados.zip', 'r') as fp:
	fp.extractall('./dados')

os.rename('./dados/dow_jones_index.data', './dados/dow_jones_index.csv')