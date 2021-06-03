# Implimentação/port baseada na macro criada por Fabio Mitsueda (https://fabiomitsueda.com.br)
import win32com.client as win32


def verifica_usario_sap_aberto():
    ###############################
    ### Variáveis
    ###############################

    i = 0
    l = 0
    objSAP = ''
    informacoes_sap = []
    GetSapUserOpen = ''

    ###############################
    ### Logon
    ###############################

    # Verificando se existe alguma instância do SAP em execução, mesmo que não esteja logada.
    while i < 10 and objSAP == '':
        i += 1
        try:
            objSAP = win32.GetObject('SAPGUI')
        except:
            objSAP = ''

    # Descarrengado a variável
    i = 0
    if objSAP != '':
        # Carrendo a variável que representa a janela do SAP
        objSapAPP = objSAP.GetScriptingEngine

        # Percorrendo todas as janels abertas do SAP e capturando as informações pertinentes
        for objConnect in objSapAPP.Children:

            # Se a conexão caiu não executar o teste para a janela
            if not objConnect.DisabledByServer:
                for objSession in objConnect.Children:

                    # Verifica se a sessão está em excecução
                    if objSession.Busy == False:

                        # Verificando se está logado através da transação S000, que é a tela de login
                        if objSession.info.Transaction != 'S000':
                            # Captura o ID do sistema
                            strID = objSession.Info.SystemName
                            # Captura o Login do susuário
                            strUser = objSession.info.user
                            # Caputra a transação da tela, uma vez que já foi verificado que não está na tela de login
                            strTransacao = objSession.Info.Transaction

                            # Verifica se existe janelas disponíveis na tela inicial do SAP logado
                            if strTransacao == 'SESSION_MANAGER':
                                fCheck = True
                            else:
                                fCheck = False

                            # Capturando dandos
                            if i == 0:
                                i += 1
                                l += 1
                                # aqui inseri as informações de usuário (login, senha, objetos de conexão) na lista
                                informacoes_sap.append(
                                    [l, strID, strUser, fCheck, objConnect, objSession]
                                )
                            else:
                                if strID != informacoes_sap[i - 1][1]:
                                    i += 1
                                    l += 1
                                    informacoes_sap.append = [
                                    [l, strID, strUser, fCheck, objConnect, objSession]
                                    ]
                                else:
                                    informacoes_sap[i][0] = (informacoes_sap[i][0] + 1)
                                    if fCheck == True:
                                        informacoes_sap[i][3] = fCheck

            l = 0
            fCheck = False

        if i == 0:
            return ''
        else:
            return informacoes_sap
    else:
        return ''