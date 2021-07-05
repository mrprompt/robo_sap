# Implimentação/port baseada na macro criada por Fabio Mitsueda (https://fabiomitsueda.com.br)
from janelas import janela_info_sessao_aberta as jisa
from janelas import janela_logon as jl
from pathlib import Path
from sap import verifica_usario_sap_aberto as vusa
import PySimpleGUI as sg
import subprocess
import sys
import time
import win32com.client as win32

sg.theme('DarkGrey14')

class SapGui(object):
    def __init__(self):
        self.path = 'C:/Program Files (x86)/SAP/FrontEnd/SAPgui/saplogon.exe'
        fileObj = Path(path_sap)
        if not fileObj.is_file():
            sg.popup('Não foi possível encontrar o arquivo saplogon.exe', title='ERRO')
        exit()

    def executaSap():
        pass

    def criaInstancia():
        pass

    def fazLogin():
        pass

    


