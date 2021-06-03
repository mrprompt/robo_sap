import PySimpleGUI as sg
from sap import conectar_sap as cs

def janela_logon():
    sg.theme('Light Blue 2')
    layout = [
        [sg.Text('Nome da Conexão', size=(15,1)), sg.InputText('', key='-NOME_CONEXAO-')],
        [sg.Text('Usuário SAP', size=(15,1)), sg.InputText('', key='-USUARIO_SAP-')],
        [sg.Text('Senha', size=(15,1)), sg.InputText('', key='-SENHA-', password_char='*')],
        [sg.Button('Conectar', key='-CONECTAR-')]
    ]

    janela = sg.Window('Logon no SAP', layout)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            exit()
        if event == '-CONECTAR-':
            if values['-NOME_CONEXAO-'] == '':
                sg.popup('Favor inserir nome da conexão', title='Erro')
            elif values['-USUARIO_SAP-'] == '':
                sg.popup('Favor usuário SAP', title='Erro')
            elif values['-SENHA-'] == '':
                sg.popup('Favor inserir a senha', title='Erro')
            else:
                break
    
    janela.close()

    session = cs.conectar_sap(values['-NOME_CONEXAO-'], values['-USUARIO_SAP-'], values['-SENHA-'])

    return session