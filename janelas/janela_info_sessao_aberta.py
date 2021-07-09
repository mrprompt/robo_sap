import PySimpleGUI as sg
import sys

def janela_info_sessao_aberta(sistema, usuario):
    sg.theme('DarkGrey14')
    layout = [
        [sg.Text('Deseja efetuar a execução do robô com a instância abaixo?')],
        [sg.Text('Sistema: ' + sistema)],
        [sg.Text('Usuário: ' + usuario)],
        [sg.Text('')],
        [sg.Button('Sim', button_color='black on white', key='-BOTAO_SIM-'), sg.Button('Não', button_color='black on white', key='-BOTAO_NAO-')]

    ]

    janela = sg.Window('Usar conexão aberta', layout)

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
        elif event == '-BOTAO_SIM-':
            janela.close()  
            return True
        elif event == '-BOTAO_NAO-':
            janela.close()   
            return False
