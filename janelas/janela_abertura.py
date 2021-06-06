import PySimpleGUI as sg
import sys

def janela_abertura():
    sg.theme('Light Blue 2')
    layout = [      
        [sg.Text('Robo para Extrair Relatórios FBL3N', size=(20, 2), justification='center', font=("Helvetica", 23), relief=sg.RELIEF_RIDGE)],
        [sg.Text('')],
        [sg.Frame('DATA PARA A POSIÇÃO DOS RELATÓRIOS',[
            [sg.Text('')],
            [sg.Text('Data (padrão DDMMAAAA)', size=(35, 1))],
            [sg.InputText('', size=(50,1), key='-DATA_RELATORIO-', enable_events=True)],
            [sg.Text('')],])],
        [sg.Text('')],
        [sg.Frame('OBTER RELAÇÃO DAS CONTAS CONCILIÁVEIS',[
            [sg.Text('')],
            [sg.Text('Por lista de contas conciliáveis', size=(35, 1))],
            [sg.InputText('', key='-ARQUIVO_CONTAS-'), sg.FileBrowse('procurar')],
            [sg.Text('')],])],
        [sg.Text('')],
        [sg.Frame('SALVAR RELATÓRIOS E SCREENSHOTS',[
            [sg.Text('')],
            [sg.Text('Pasta onde serão salvos os relatórios', size=(35, 1))],
            [sg.InputText('', key='-PASTA-'), sg.FolderBrowse('procurar')]])],
        [sg.Text('')],
        [sg.Button('Executar Robô', key='-EXECUTAR_ROBO-', enable_events=True)]
    ]      

    janela = sg.Window('Robô para Extrair Relatórios FBL3N', layout, default_element_size=(40, 1), element_justification='right', grab_anywhere=False) 

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
