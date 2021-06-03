def obter_relacao_contas(caminho_arquivo_contas_conciliaveis):
    contas_conciliaveis = []
    #abrindo o arquivo txt com a relação de contas
    with open(caminho_arquivo_contas_conciliaveis) as arquivo_contas:
        #Le o arquivo linha a linha
        for linha in arquivo_contas:
            #para cada linha lida, inseri a conta na relação de contas conciliáveis
            contas_conciliaveis.append(linha.replace('\n', ''))
    #fecha o arquivo
    arquivo_contas.close()

    return contas_conciliaveis