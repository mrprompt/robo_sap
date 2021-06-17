import os

def verifica_pasta_existe(caminho):

    if not os.path.isdir(caminho):
        os.makedirs(caminho)
