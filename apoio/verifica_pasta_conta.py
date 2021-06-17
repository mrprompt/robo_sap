import os

def verifica_pasta_conta(caminho_pasta, conta):
    pastas = os.listdir(caminho_pasta)

    criar_pasta = True

    for pasta in pastas:
        if pasta[0:9] == conta:
            criar_pasta = False
            pasta_a_utilizar = pasta
            break
            
    if criar_pasta:
        os.makedirs(caminho_pasta + '/' + conta)
        pasta_a_utilizar = caminho_pasta + '/' + conta

    return pasta_a_utilizar