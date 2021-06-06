# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #

from janelas import janela_abertura as ja
from sap import efetuar_logon as el
from robo import robo as rb
import PySimpleGUI as sg

# tela inicial
informacoes_janela_abertura = ja.janela_abertura()

# Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
session = el.efetuar_logon()

# Chamar a rotina
rb.executa_robo(informacoes_janela_abertura, session)

# encerrar robo
sg.popup('Execução efetuada com sucesso')