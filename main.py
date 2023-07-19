import PyPDF2
import os
import PySimpleGUI as sg
import confeccionarCapa as confec

nome_tipo_lista_ao_adicionar_ano = ''
siglas = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'TO']
siglas_ddd = ['21', '22', '24', '27', '28', '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']



layout_escolher_qual_acao = [
    [sg.Text('')],
    [sg.Button('POR UF RESIDENCIAL'), sg.Button('POR UF NÃO RESIDENCIAL')],
    [sg.Text('')],
    [sg.Button('POR DDD RESIDENCIAL'), sg.Button('POR DDD NÃO RESIDENCIAL')],
    [sg.Text('')],
]


layout_inserir_ano_capa = [
    [sg.Text('ATUALIZAÇÃO DO ANO DA CAPA')],
    [sg.Input(key='ano_digitado_input')],
    [sg.Button('PROCESSAR')],
    [sg.Text('', key='ano_digitado_texto')],
]



janela_para_ecolher_qual_tipo_de_lista_vai_ser_alterado = sg.Window('A5 - ATUALIZAÇÃO CAPA TELEFONICA OI', layout=layout_escolher_qual_acao)
def abrir_janela_para_digitar_ano(nome_tipo_lista):
    janela_para_digitar_ano_para_alterar_na_capa = sg.Window(f'DIGITAR ANO {nome_tipo_lista_ao_adicionar_ano}',
                                                             layout=layout_inserir_ano_capa)

while True:
    event, value = janela_para_ecolher_qual_tipo_de_lista_vai_ser_alterado.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'POR UF RESIDENCIAL':
        nome_tipo_lista_ao_adicionar_ano = 'UF RESIDENCIAL'
        janela_para_digitar_ano_para_alterar_na_capa = sg.Window(f'DIGITAR ANO {nome_tipo_lista_ao_adicionar_ano}',
                                                                 layout=layout_inserir_ano_capa)
        while True:
            event2, value2 = janela_para_digitar_ano_para_alterar_na_capa.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == 'PROCESSAR':
                ano_digitado: any = value2['ano_digitado_input']

                image_path = "CAPA_PADRAO/CAPA_IMAGEM.png"
                estado_x = 60  # Coordenada X do texto no PDF
                estado_y = 300  # Coordenada Y do texto no PDF
                estado = ""
                ano = ano_digitado
                janela_para_digitar_ano_para_alterar_na_capa['ano_digitado_texto'].update(
                    f'O ano digitado foi {ano}')
                ano_x = 465  # Coordenada X do texto no PDF
                ano_y = 718  # Coordenada Y do texto no PDF
                output_path = "teste.pdf"
                tipo_lista = "RESIDENCIAL"

                tipo_lista_x = 340  # Coordenada X do texto no PDF
                tipo_lista_y = 690  # Coordenada Y do texto no PDF

                confec.create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                      tipo_lista, tipo_lista_x, tipo_lista_y, output_path)


    elif event == 'POR UF NÃO RESIDENCIAL':
        nome_tipo_lista_ao_adicionar_ano = 'UF NÃO RESIDENCIAL'
        janela_para_digitar_ano_para_alterar_na_capa = sg.Window(f'DIGITAR ANO {nome_tipo_lista_ao_adicionar_ano}',
                                                                 layout=layout_inserir_ano_capa)

        while True:
            event2, value2 = janela_para_digitar_ano_para_alterar_na_capa.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == 'PROCESSAR':
                ano_digitado: any = value2['ano_digitado_input']

                image_path = "CAPA_PADRAO/CAPA_IMAGEM.png"
                estado_x = 60  # Coordenada X do texto no PDF
                estado_y = 300  # Coordenada Y do texto no PDF
                estado = ""
                ano = ano_digitado
                janela_para_digitar_ano_para_alterar_na_capa['ano_digitado_texto'].update(
                    f'O ano digitado foi {ano}')
                ano_x = 465  # Coordenada X do texto no PDF
                ano_y = 718  # Coordenada Y do texto no PDF
                output_path="CAPA_POR_UF_NAO_RESIDENCIAL/"
                tipo_lista = "NÃO RESIDENCIAL"

                tipo_lista_x = 270  # Coordenada X do texto no PDF
                tipo_lista_y = 690  # Coordenada Y do texto no PDF

                confec.criarCapaListaPorUFNaoResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas)

    elif event == 'POR DDD RESIDENCIAL':
        nome_tipo_lista_ao_adicionar_ano = 'DDD NÃO RESIDENCIAL'
        janela_para_digitar_ano_para_alterar_na_capa = sg.Window(f'DIGITAR ANO {nome_tipo_lista_ao_adicionar_ano}',
                                                                 layout=layout_inserir_ano_capa)

        while True:
            event2, value2 = janela_para_digitar_ano_para_alterar_na_capa.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == 'PROCESSAR':
                ano_digitado: any = value2['ano_digitado_input']

                image_path = "CAPA_PADRAO/CAPA_IMAGEM.png"
                estado_x = 60  # Coordenada X do texto no PDF
                estado_y = 300  # Coordenada Y do texto no PDF
                estado = ""
                ano = ano_digitado
                janela_para_digitar_ano_para_alterar_na_capa['ano_digitado_texto'].update(
                    f'O ano digitado foi {ano}')
                ano_x = 465  # Coordenada X do texto no PDF
                ano_y = 718  # Coordenada Y do texto no PDF
                output_path="CAPA_POR_UF_NAO_RESIDENCIAL/"
                tipo_lista = "RESIDENCIAL"

                tipo_lista_x = 340  # Coordenada X do texto no PDF
                tipo_lista_y = 690  # Coordenada Y do texto no PDF

                confec.criarCapaListaPorDDDResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas_ddd)

    elif event == 'POR DDD NÃO RESIDENCIAL':
        nome_tipo_lista_ao_adicionar_ano = 'UF NÃO RESIDENCIAL'
        janela_para_digitar_ano_para_alterar_na_capa = sg.Window(f'DIGITAR ANO {nome_tipo_lista_ao_adicionar_ano}',
                                                                 layout=layout_inserir_ano_capa)

        while True:
            event2, value2 = janela_para_digitar_ano_para_alterar_na_capa.read()
            if event2 == sg.WIN_CLOSED:
                break
            elif event2 == 'PROCESSAR':
                ano_digitado: any = value2['ano_digitado_input']

                image_path = "CAPA_PADRAO/CAPA_IMAGEM.png"
                estado_x = 60  # Coordenada X do texto no PDF
                estado_y = 300  # Coordenada Y do texto no PDF
                estado = ""
                ano = ano_digitado
                janela_para_digitar_ano_para_alterar_na_capa['ano_digitado_texto'].update(
                    f'O ano digitado foi {ano}')
                ano_x = 465  # Coordenada X do texto no PDF
                ano_y = 718  # Coordenada Y do texto no PDF
                output_path = "CAPA_POR_UF_NAO_RESIDENCIAL/"
                tipo_lista = "NÃO RESIDENCIAL"

                tipo_lista_x = 270  # Coordenada X do texto no PDF
                tipo_lista_y = 690  # Coordenada Y do texto no PDF

                confec.criarCapaListaPorDDDNaoResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista,
                                                         tipo_lista_x, tipo_lista_y, siglas_ddd)


# Função para adicionar a primeira página de um arquivo PDF ao início de outro arquivo PDF
def adicionar_primeira_pagina(origem, destino):
    with open(origem, 'rb') as pdf_origem, open(destino, 'rb') as pdf_destino:
        reader_origem = PyPDF2.PdfReader(pdf_origem)
        reader_destino = PyPDF2.PdfReader(pdf_destino)
        writer = PyPDF2.PdfWriter()

        # Adiciona a primeira página do arquivo de origem ao início do arquivo de destino
        primeira_pagina = reader_origem.pages[0]
        writer.add_page(primeira_pagina)

        # Adiciona as páginas restantes do arquivo de destino
        for pagina in reader_destino.pages:
            writer.add_page(pagina)

        # Sobrescreve o arquivo de destino com o novo conteúdo
        with open(destino, 'wb') as output:
            writer.write(output)

# Função para remover a segunda página de um arquivo PDF
def remover_segunda_pagina(arquivo):
    with open(arquivo, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        # Copia as páginas do arquivo original, exceto a segunda página
        for i, pagina in enumerate(reader.pages):
            if i != 1:  # Ignora a segunda página
                writer.add_page(pagina)

        # Sobrescreve o arquivo original com o novo conteúdo
        with open(arquivo, 'wb') as output:
            writer.write(output)


def percorrendo_as_pastas_de_uf_residencial(caminho, caminho_listas, caminho_capas, siglas):
    arquivos_encontrados={}

    for pasta_atual, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.pdf'):
                nome_arquivo = os.path.splitext(arquivo)[0]
                sigla = nome_arquivo[4:4+2]

                if (sigla == 'AC'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGACR.pdf'
                    arquivo_destino = 'LISTAS\LTOGACR.pdf'
                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'AL'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGALR.pdf'
                    arquivo_destino = 'LISTAS\LTOGALR.pdf'
                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'AM'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGAMR.pdf'
                    arquivo_destino = 'LISTAS\LTOGAMR.pdf'
                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'AP'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGAPR.pdf'
                    arquivo_destino = 'LISTAS\LTOGAPR.pdf'
                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'BA'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGBAR.pdf'
                    arquivo_destino = 'LISTAS\LTOGBAR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'CE'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGCER.pdf'
                    arquivo_destino = 'LISTAS\LTOGCER.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'DF'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGDFR.pdf'
                    arquivo_destino = 'LISTAS\LTOGDFR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'ES'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGESR.pdf'
                    arquivo_destino = 'LISTAS\LTOGESR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'GO'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGGOR.pdf'
                    arquivo_destino = 'LISTAS\LTOGGOR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'MA'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGMAR.pdf'
                    arquivo_destino = 'LISTAS\LTOGMAR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'MG'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGMGR.pdf'
                    arquivo_destino = 'LISTAS\LTOGMGR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'MS'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGMSR.pdf'
                    arquivo_destino = 'LISTAS\LTOGMSR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'MT'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGMTR.pdf'
                    arquivo_destino = 'LISTAS\LTOGMTR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'PA'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGPAR.pdf'
                    arquivo_destino = 'LISTAS\LTOGPAR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'PB'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGPBR.pdf'
                    arquivo_destino = 'LISTAS\LTOGPBR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'PE'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGPER.pdf'
                    arquivo_destino = 'LISTAS\LTOGPER.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'PI'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGPIR.pdf'
                    arquivo_destino = 'LISTAS\LTOGPIR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'PR'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGPRR.pdf'
                    arquivo_destino = 'LISTAS\LTOGPRR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'RJ'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGRJR.pdf'
                    arquivo_destino = 'LISTAS\LTOGRJR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'RN'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGRNR.pdf'
                    arquivo_destino = 'LISTAS\LTOGRNR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'RO'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGROR.pdf'
                    arquivo_destino = 'LISTAS\LTOGROR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'RR'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGRRR.pdf'
                    arquivo_destino = 'LISTAS\LTOGRRR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'RS'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGRSR.pdf'
                    arquivo_destino = 'LISTAS\LTOGRSR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'SC'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGSCR.pdf'
                    arquivo_destino = 'LISTAS\LTOGSCR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)
                if (sigla == 'SE'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGSER.pdf'
                    arquivo_destino = 'LISTAS\LTOGSER.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)

                if (sigla == 'TO'):
                    arquivo_origem = 'CAPA_PARA_ADICIONAR\CAPA_ADD_LTOGTOR.pdf'
                    arquivo_destino = 'LISTAS\LTOGTOR.pdf'

                    print(f'adicionando a capa {arquivo_origem} no arquivo {arquivo_destino}')
                    adicionar_primeira_pagina(arquivo_origem, arquivo_destino)

                    print(f'removendo segunda página do arquivo {arquivo_destino}')
                    remover_segunda_pagina(arquivo_destino)
                    break




    return arquivos_encontrados




# Arquivos de entrada
# arquivo_origem = 'CAPA_ADD_LTOGACR.pdf'
# arquivo_destino = 'LTOGACR.pdf'
# siglas_desejadas = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'TO']
#
# # Adiciona a primeira página de 'pagina.pdf' ao início de 'documento.pdf'
# # adicionar_primeira_pagina(arquivo_origem, arquivo_destino)
# #
# # Remove a segunda página de 'documento.pdf'
# # remover_segunda_pagina(arquivo_destino)
# caminho_pasta = 'C:/backup2023/OI/LISTA TELEFONICA/UF/RESIDENCIAL'
# caminho_listas = 'LISTAS'
# caminho_capas = 'CAPA_PARA_ADICIONAR'
# arquivo_encontrado = percorrendo_as_pastas_de_uf_residencial(caminho_pasta, caminho_listas, caminho_capas, siglas_desejadas)
#
# if arquivo_encontrado:
#     print("Arquivo encontrado:", arquivo_encontrado)
# else:
#     print("Nenhum arquivo encontrado com a sigla na posição desejada.")
