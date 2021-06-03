# Implimentação/port baseada na macro criada por Fabio Mitsueda (https://fabiomitsueda.com.br)
from pathlib import Path
import PySimpleGUI as sg
import subprocess
import time
import win32com.client as win32

def conectar_sap(ambiente, user, passwd):
    nome_ambiente = ambiente
    usuario = user
    senha = passwd
    path_sap = 'C:/Program Files (x86)/SAP/FrontEnd/SAPgui/saplogon.exe'
    fileObj = Path(path_sap)
    if not fileObj.is_file():
        sg.popup('Não foi possível encontrar o arquivo saplogon.exe', title='ERRO')
        exit()
    
    # abrindo o SAPlogon
    process = subprocess.Popen(path_sap, stdout=subprocess.PIPE)
    time.sleep(5)

    # Carrengado a varial com as propriedades do SAP LOGON
    SapGuiAuto = win32.GetObject('SAPGUI')
    application = SapGuiAuto.GetScriptingEngine
    connection = application.OpenConnection(nome_ambiente, True)
    session = connection.Children(0)
    session.findById("wnd[0]/usr/txtRSYST-BNAME").text = usuario
    session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = senha
    session.findById("wnd[0]").sendVKey(0)

    return session