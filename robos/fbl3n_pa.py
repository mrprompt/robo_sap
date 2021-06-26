import time
import pyautogui as pag
import PySimpleGUI as sg
from apoio import verifica_janelas as vj
from apoio import obter_relacao_contas as orc
from apoio import verifica_pasta_existe as vpe
from apoio import verifica_pasta_conta as vpc
from janelas import janela_fbl3n_pa as ja
from sap import efetuar_logon as el
import os


def executa_robo():
    # Chama a janela do robo
    informacoes_janela_fbl3n_pa = ja.janela_fbl3n_pa()

    # Conectar ao SAP (seja por logon ou usando uma sessão já aberta)
    session = el.efetuar_logon()

    # Atribuindo valores as variáveis conforme informações inseridas pelo usuário

    # DATA REFERENCIA - data para a posição do relatório
    data_referencia = informacoes_janela_fbl3n_pa[0]

    # MES REFERENCIA - AAAAMM para inserir no inicio do nome do relatório exportado e no nome do screenshot
    mes_referencia = (informacoes_janela_fbl3n_pa[0][4:] + informacoes_janela_fbl3n_pa[0][2:4])

    # CAMINHA_ARQUIVO_CONTAS_CONCILIAVEIS - indica o path e o caminho para obter a relação de contas conciliáveis
    caminho_arquivo_contas_conciliaveis = informacoes_janela_fbl3n_pa[1]

    # CAMINHA_PASTA_RELATORIOS - indica o path onde serão salvos os relatórios
    caminho_pasta_relatorios = informacoes_janela_fbl3n_pa[2]

    # --- Obtendo contas conciliáveis --- #
    contas_conciliaveis = orc.obter_relacao_contas(caminho_arquivo_contas_conciliaveis)

    # Abrindo a transação FBL3N
    session.findById('wnd[0]').iconify()
    session.findById('wnd[0]').maximize()
    session.findById('wnd[0]/tbar[0]/okcd').text = 'FBL3N'
    session.findById('wnd[0]').sendVKey(0)

    # Laçõ de repetição, executado para cada conta da relação de contas conciliáveis
    for conta in contas_conciliaveis:

        # Insirindo as informações necessárias na tela de Parametros
        session.findById('wnd[0]/usr/ctxtSD_SAKNR-LOW').text = conta
        session.findById('wnd[0]/usr/ctxtSD_BUKRS-LOW').text = 'ESUL'
        session.findById('wnd[0]/usr/ctxtPA_STIDA').text = data_referencia
        session.findById('wnd[0]/usr/chkX_PARK').selected = False
        session.findById('wnd[0]/usr/ctxtPA_VARI').text = '/MD_CO_SECOG'

        # tirando print da parametrização
        screenParametrizacao = pag.screenshot()

        # executa a geração do relatório
        session.findById('wnd[0]').sendVKey(8)

        # Verificando se a execução não teve dados exibidos. Se não houver dados, volta ao inicio do laço
        if session.findById('wnd[0]/sbar').text == 'Nenhuma partida selecionada (ver texto descritivo)':
            # Print resultado
            time.sleep(1)
            screenExecucao = pag.screenshot()
            pasta_para_salvar_os_arquivos = vpc.verifica_pasta_conta(caminho_pasta_relatorios, conta)
            # Salvando os prints tirados
            vpe.verifica_pasta_existe(pasta_para_salvar_os_arquivos + '/prints')
            screenParametrizacao.save(pasta_para_salvar_os_arquivos + '/prints/' + mes_referencia + ' ' + conta + ' 01 parametrizacao.jpg')
            screenExecucao.save(pasta_para_salvar_os_arquivos + '/prints/' + mes_referencia + ' ' + conta + ' 02 resultados.png')
            continue

        # Capturando informações do razão gerado
        # gerando visão totalizada
        session.findById('wnd[0]/mbar/menu[1]/menu[10]').select()
        session.findById('wnd[1]/usr/tblSAPLSKBHTC_WRITE_LIST_820').getAbsoluteRow(0).selected = -1
        session.findById('wnd[1]/usr/btnB_SEARCH').press()
        session.findById('wnd[2]/usr/txtGD_SEARCHSTR').text = 'Conta'
        session.findById('wnd[1]/usr/btnAPP_WL_SING').press()
        session.findById('wnd[1]/tbar[0]/btn[0]').press()
        session.findById('wnd[0]/usr/lbl[5,8]').setFocus()
        session.findById('wnd[0]/usr/lbl[5,8]').caretPosition = 7
        session.findById('wnd[0]/tbar[1]/btn[31]').press()

        # Abrindo tela de informações
        session.findById('wnd[0]').sendVKey(35)
              
        # Esperando um segundo, para dar tempo da janela de informações aparecer antes de tirar o print
        time.sleep(1)

        # Abaixando a tela de informação para não cobrir as informações geradas
        pag.press('alt')
        pag.press('m')
        pag.press('down', presses=40)

        # Print resultado
        screenExecucao = pag.screenshot()
        
        # Fecha a janela
        session.findById('wnd[0]').sendVKey(0)

        #Exportanto para Excel
        pasta_para_salvar_os_arquivos = vpc.verifica_pasta_conta(caminho_pasta_relatorios, conta)
        session.findById('wnd[0]/mbar/menu[0]/menu[3]/menu[1]').select()
        session.findById('wnd[0]').sendVKey(0)
        session.findById('wnd[1]/usr/ctxtDY_PATH').text = pasta_para_salvar_os_arquivos + '/relatorios'
        session.findById('wnd[1]/usr/ctxtDY_FILENAME').text = mes_referencia + ' ' + conta + '.xlsx'
        session.findById('wnd[1]').sendVKey(0)

        # mapeando a janela ativa. Quando detectar que é o Excel, mata o processo.
        janela_ativa = ''
        while janela_ativa != 'EXCEL.EXE':
            time.sleep(1)
            janela_ativa = vj.verifica_janela_ativa()

        # neste ponto, foi detectado que o Excel passou a ser a janela ativa, e com isso o processo é encerrado
        os.system('TASKKILL /F /IM EXCEL.EXE')

        # Espera um segundo, para que o processo seja finalizado
        time.sleep(1)

        # Esvazia a variável, para que no próximo laço ele volte a rodar a detecção
        janela_ativa = ''

        # Salvando os prints tirados
        vpe.verifica_pasta_existe(pasta_para_salvar_os_arquivos + '/prints')
        screenParametrizacao.save(pasta_para_salvar_os_arquivos + '/prints/' + mes_referencia + ' ' + conta + ' 01 parametrizacao.jpg')
        screenExecucao.save(pasta_para_salvar_os_arquivos + '/prints/' + mes_referencia + ' ' + conta + ' 02 resultados.png')
        
        # Volta para a tela de parâmetros
        session.findById('wnd[0]').sendVKey(15)
    
    # encerrar robo
    sg.popup('Execução efetuada com sucesso')