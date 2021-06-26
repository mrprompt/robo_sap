# --- ROBO PARA CONECTAR E EXECUTAR TRANSACOES NO SAP --- #
import PySimpleGUI as sg
from robos import fbl3n_pa

sg.theme('DarkGrey14')

coluna_esquerda = [[sg.Text('Coleção de Robôs para Geração de IPEs', font=("Helvetica", 25))],
                   [sg.Text('selecione um robôs abaixo', font=("Helvetica", 10))],
                   [sg.Text('')],
                   [sg.Button('FBL3N - PA', size=(10,1), button_color='black on white', key='-FBL3N_PA-'),
                    sg.Button('FBL1N - PA', size=(10,1), button_color='black on white', key='-FBL1N_PA-'),
                    sg.Button('FBL5N - PA', size=(10,1), button_color='black on white', key='-FBL5N_PA-')],
                   [sg.Button('FC10N', size=(10,1), button_color='black on white', key='-FC10N-'),
                    sg.Button('FS10N', size=(10,1), button_color='black on white', key='-FS10N-'),
                    sg.Button('FAGLL03', size=(10,1), button_color='black on white', key='-FAGLL03-')]
]

coluna_direita = [[sg.Image('logotipo3.png', size=(100, 100), key='key1')]
]

layout = [[sg.Column(coluna_esquerda, element_justification='c'), sg.VSeperator(),sg.Column(coluna_direita, element_justification='c')]]

janela= sg.Window('Coleção de Robôs', layout, resizable=True)

while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
        if event == '-FBL3N_PA-':
            fbl3n_pa.executa_robo()
        else:
            break
            
    janela.close()

