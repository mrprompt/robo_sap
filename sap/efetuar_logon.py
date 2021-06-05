# Implimentação baseada na macro criada por Fabio Mitsueda (https://fabiomitsueda.com.br)
import win32com.client as win32
from sap import verifica_usario_sap_aberto as vusa
from janelas import janela_info_sessao_aberta as jisa
from janelas import janela_logon as jl
import time
import PySimpleGUI as sg
import sys

def efetuar_logon():
    # Verifica se o SAP está no caminho padrão
    vSap = vusa.verifica_usario_sap_aberto()

    # 'vSap é uma variante que na linha anterior recebeu valores da função GetSapUserOpen, 
    # quando não existe nenhuma instancia Sap aberta. Essa função retorna Empty, ou seja
    #  nada, na linha abaixo testo se a função não retornou nada é porque existe conexões abertas.
    if vSap != '':

        # Pergunta se o usuário quer utilizar a Instância já aberta
        usar_instancia_aberta = jisa.janela_info_sessao_aberta(vSap[0][1], vSap[0][2])

        if usar_instancia_aberta == True:
            # verifica se a janela SAP está na tela inicial
            if vSap[0][3] == True:
                objConnection = vSap[0][4]
                Session = vSap[0][5]
                # Procurando a janela incial dentro das possíveis janelas abertas nessa conexão
                for Session in objConnection.Children:
                    if Session.Busy == False:
                        if Session.Info.Transaction == 'SESSION_MANAGER':
                            return Session
                            break
                
            # Caso não tenha uma janela na tela iniciar, cria uma nova janela para a transação
            else:
                # Caso o usuário responde que quer reutilizar a conexão existente, verifica se já há 6 janelas abertas
                #   (o que impossibilita a criação de uma nova). Se houver, encerra a execução
                if vSap[0][0] == 6:
                    sg.popup('Este usuário já possui 6 janelas SAP abertas. Impossível abrir uma nova')
                    sys.exit()
                else:
                    objConnection = vSap[0][4]
                    Session = vSap[0][5]
                    # Criando a nova janela
                    Session.createSession()
                    time.sleep(2)
                    for Session in objConnection.Children:
                        if Session.Busy == False:
                            if Session.Info.Transaction == 'SESSION_MANAGER':
                                return Session
                                break
        # Caso o usuário opte por iniciar uma nova instância, abre a tela de Login
        else:
            info_logon = jl.janela_logon()

    # Caso não exista uma instância Sap aberta, abre a tela de login
    info_logon = jl.janela_logon()

    return info_logon