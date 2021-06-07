import os

def verifica_pasta(caminho):

    if not os.path.isdir(caminho):
        os.makedirs(caminho)
