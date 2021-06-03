# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #

# Versão 2
#   Foi feita uma reimplementação, para facilitar a criação de novos robos
#   
#   Foi separado a parte do login, telas de interação com o usuário e a rotina propriamente dita. Ou seja, a biblioteca
#       de login pode ser reaproveitada em qualquer robô SAP.#   
#
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