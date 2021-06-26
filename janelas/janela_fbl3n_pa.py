import PySimpleGUI as sg
import sys

def janela_fbl3n_pa():
    sg.theme('DarkGrey14')
    layout = [      
        [sg.Text('Robo para Extração de Relatórios FBL3N', size=(20, 2), justification='center', font=("Helvetica", 23), relief=sg.RELIEF_RIDGE)],
        [sg.Text('')],
        [sg.Text('DATA P/ A POSIÇÃO DOS RELATÓRIOS (DDMMAAAA)', size=(43, 1))],
        [sg.InputText('', background_color='grey', size=(40,1), key='-DATA_RELATORIO-', enable_events=True)],
        [sg.Text('')],
        [sg.Text('RELAÇÃO DAS CONTAS CONCILIÁVEIS')],
        [sg.InputText('', background_color='grey', key='-ARQUIVO_CONTAS-'), sg.FileBrowse('procurar', button_color='black on white')],
        [sg.Text('')],
        [sg.Text('PASTA ONDE SERÃO SALVOS OS RELATÓRIOS', size=(40, 1))],
        [sg.InputText('', background_color='grey', key='-PASTA-'), sg.FolderBrowse('procurar', button_color='black on white')],
        [sg.Text('')],
        [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', button_color='black on white', enable_events=True)]
    ]      

    janela = sg.Window('Robô para Extrair Relatórios FBL3N', layout, default_element_size=(40, 1), element_justification='left', grab_anywhere=False) 

    while True:
        event, values = janela.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            sys.exit()
        if event == '-EXECUTAR_ROBO-':
            if values['-DATA_RELATORIO-'] == '':
                sg.popup('Favor inserir data da posição do relatório', title='Erro')
            elif values['-ARQUIVO_CONTAS-'] == '':
                sg.popup('Favor indicar o arquivo com a relação das contas conciliáveis', title='Erro')
            elif values['-PASTA-'] == '':
                sg.popup('Favor indicar a pasta onde serão salvos os relatórios', title='Erro')
            else:
                break
            
    janela.close()

    return values['-DATA_RELATORIO-'], values['-ARQUIVO_CONTAS-'], values['-PASTA-']
