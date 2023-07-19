from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.colors import PCMYKColor
from PIL import Image
import PyPDF2
import os

image_path = "CAPA_IMAGEM.png"

estado =""
estado_x = 60  # Coordenada X do texto no PDF
estado_y = 300  # Coordenada Y do texto no PDF

ano = "2023"
ano_x = 465  # Coordenada X do texto no PDF
ano_y = 718  # Coordenada Y do texto no PDF

tipo_lista = "RESIDENCIAL"

tipo_lista_x = 340  # Coordenada X do texto no PDF
tipo_lista_y = 690  # Coordenada Y do texto no PDF

def testeBotao():
    print('cliquei no botão lá')



def create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, output_path,pagina_origem, pagina_destino):

    c = canvas.Canvas(output_path, pagesize=A4)

    # Adiciona a imagem ao PDF
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Calcula as dimensões da imagem para ocupar a área toda do PDF
    pdf_width, pdf_height = A4
    img_ratio = img_width / img_height
    pdf_ratio = pdf_width / pdf_height

    if img_ratio > pdf_ratio:
        new_width = pdf_width
        new_height = pdf_width / img_ratio
    else:
        new_width = pdf_height * img_ratio
        new_height = pdf_height

    c.drawImage(image_path, 0, 0, width=new_width, height=new_height)

    # Adiciona o texto ao PDF
    text_color = PCMYKColor(0, 0, 0, 10)  # Cor do texto em CMYK (branco apagado)
    c.setFillColor(text_color)
    font_path = "FONTES\Cousine-Bold.ttf"
    font_name_estado_e_tipo_lista = "minha_fonte_estado_e_tipo_lista"  # Nome da fonte
    pdfmetrics.registerFont(TTFont(font_name_estado_e_tipo_lista, font_path))
    c.setFont(font_name_estado_e_tipo_lista, 25)
    c.drawString(estado_x, estado_y, estado)
    c.setFont(font_name_estado_e_tipo_lista, 29)
    c.drawString(tipo_lista_x, tipo_lista_y, tipo_lista)

    font_path = "FONTES\FONT_ANO.ttf"
    font_name_ano = "minha_fonte_ano"  # Nome da fonte
    pdfmetrics.registerFont(TTFont(font_name_ano, font_path))
    c.setFont(font_name_ano, 29)
    c.drawString(ano_x, ano_y, ano)


    c.showPage()
    c.save()
    adicionar_primeira_pagina(pagina_origem, pagina_destino)
    remover_segunda_pagina(pagina_destino)



def criarCapaBaseadaNasListasJaCriadas(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas):
    for sigla in siglas:
        if (sigla == 'AC'):
            estado = "ACRE"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AL'):
            estado = "ALAGOAS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AM'):
            estado = "AMAZONAS"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AP'):
            estado = "AMAPÁ"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'BA'):
            estado = "BAHIA"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'CE'):
            estado = "CEARÁ"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'DF'):
            estado = "DISTRITO FEDERAL"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'ES'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'GO'):
            estado = "GOIÁS"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MA'):
            estado = "MARANHÃO"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MG'):
            estado = "MINAS GERAIS"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MS'):
            estado = "MATO GROSSO DO SUL"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MT'):
            estado = "MATO GROSSO"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PA'):
            estado = "PARÁ"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PB'):
            estado = "PARAÍBA"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PE'):
            estado = "PERNAMBUCO"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PI'):
            estado = "PIAUÍ"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PR'):
            estado = "PARANÁ"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RJ'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RN'):
            estado = "RIO GRANDE DO NORTE"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RO'):
            estado = "RONDÔNIA"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RR'):
            estado = "RORAIMA"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RS'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'SC'):
            estado = "SANTA CATARINA"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'SE'):
            estado = "SERGIPE"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == 'TO'):
            estado = "TOCANTINS"
            output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""
            break

def criarCapaListaPorUFNaoResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas):
    for sigla in siglas:
        if (sigla == 'AC'):
            estado = "ACRE"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem, pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AL'):
            estado = "ALAGOAS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AM'):
            estado = "AMAZONAS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'AP'):
            estado = "AMAPÁ"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'BA'):
            estado = "BAHIA"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'CE'):
            estado = "CEARÁ"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'DF'):
            estado = "DISTRITO FEDERAL"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'ES'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'GO'):
            estado = "GOIÁS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MA'):
            estado = "MARANHÃO"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MG'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MS'):
            estado = "MATO GROSSO DO SUL"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'MT'):
            estado = "MATO GROSSO"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PA'):
            estado = "PARÁ"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PB'):
            estado = "PARAÍBA"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PE'):
            estado = "PERNAMBUCO"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PI'):
            estado = "PIAUÍ"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'PR'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RJ'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RN'):
            estado = "RIO GRANDE DO NORTE"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RO'):
            estado = "RONDÔNIA"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RR'):
            estado = "RORAIMA"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'RS'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'SC'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == 'SE'):
            estado = "SERGIPE"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == 'TO'):
            estado = "TOCANTINS"
            output_path = "CAPA_POR_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_UF_NAO_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""
            break

def criarCapaListaPorDDDResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas):
    for sigla in siglas:
        if (sigla == '21'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '22'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '24'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '27'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '28'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '31'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '32'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '33'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '34'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '35'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '37'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '38'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '41'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '42'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '43'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '44'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '45'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '46'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '47'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '48'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '49'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '51'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '53'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '54'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '55'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '61'):
            estado = "DISTRIRO FEDERAL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '62'):
            estado = "GOIÁS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '63'):
            estado = "TOCANTINS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '64'):
            estado = "GOIÁS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '65'):
            estado = "MATO GROSSO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '66'):
            estado = "MATO GROSSO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '67'):
            estado = "MATO GROSSO DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '68'):
            estado = "ACRE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '69'):
            estado = "RONDÔNIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '71'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '73'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '74'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '75'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '77'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '79'):
            estado = "SERGIPE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '81'):
            estado = "PERNAMBUCO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '82'):
            estado = "ALAGOAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '83'):
            estado = "PARAÍBA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '84'):
            estado = "RIO GRANDE DO NORTE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '85'):
            estado = "CEARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '86'):
            estado = "PIAUÍ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '87'):
            estado = "PERNAMBUCO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '88'):
            estado = "CEARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '89'):
            estado = "PIAUÍ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '91'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '92'):
            estado = "AMAZONAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '93'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '94'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '95'):
            estado = "RORAIMA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '96'):
            estado = "AMAPÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '97'):
            estado = "AMAZONAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == '98'):
            estado = "MARANHÃO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == '99'):
            estado = "MARANHÃO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            break

def criarCapaListaPorDDDNaoResidencial(image_path, estado_x, estado_y, ano, ano_x, ano_y, tipo_lista, tipo_lista_x, tipo_lista_y, siglas):
    for sigla in siglas:
        if (sigla == '21'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '22'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '24'):
            estado = "RIO DE JANEIRO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '27'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '28'):
            estado = "ESPÍRITO SANTO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '31'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '32'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '33'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '34'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '35'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '37'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '38'):
            estado = "MINAS GERAIS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '41'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '42'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '43'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '44'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '45'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '46'):
            estado = "PARANÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '47'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '48'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '49'):
            estado = "SANTA CATARINA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '51'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '53'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '54'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            estado = ""

        if (sigla == '55'):
            estado = "RIO GRANDE DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '61'):
            estado = "DISTRIRO FEDERAL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '62'):
            estado = "GOIÁS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '63'):
            estado = "TOCANTINS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '64'):
            estado = "GOIÁS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '65'):
            estado = "MATO GROSSO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '66'):
            estado = "MATO GROSSO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '67'):
            estado = "MATO GROSSO DO SUL"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '68'):
            estado = "ACRE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '69'):
            estado = "RONDÔNIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '71'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '73'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '74'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '75'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '77'):
            estado = "BAHIA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '79'):
            estado = "SERGIPE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '81'):
            estado = "PERNAMBUCO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '82'):
            estado = "ALAGOAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '83'):
            estado = "PARAÍBA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '84'):
            estado = "RIO GRANDE DO NORTE"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '85'):
            estado = "CEARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '86'):
            estado = "PIAUÍ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '87'):
            estado = "PERNAMBUCO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '88'):
            estado = "CEARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '89'):
            estado = "PIAUÍ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '91'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "R.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '92'):
            estado = "AMAZONAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '93'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '94'):
            estado = "PARÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '95'):
            estado = "RORAIMA"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '96'):
            estado = "AMAPÁ"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""
        if (sigla == '97'):
            estado = "AMAZONAS"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == '98'):
            estado = "MARANHÃO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)

            estado = ""

        if (sigla == '99'):
            estado = "MARANHÃO"
            output_path = "CAPA_POR_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            pagina_origem = output_path
            pagina_destino = "LISTA_DDD_RESIDENCIAL\LTOG" + sigla + "NR.pdf"
            create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                           tipo_lista, tipo_lista_x, tipo_lista_y, output_path, pagina_origem,
                                           pagina_destino)
            print(estado + " criado com o caminho e o nome de " + output_path)
            break


def buscar_arquivos_por_siglas(caminho, siglas):
    arquivos_encontrados = {}
    for pasta_atual, _, arquivos in os.walk(caminho):
        for arquivo in arquivos:
            if arquivo.lower().endswith('.pdf'):
                nome_arquivo = os.path.splitext(arquivo)[0]  # Remove a extensão do arquivo
                for sigla in siglas:
                    if (sigla == 'AC'):
                        estado = "ACRE"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'AL'):
                        estado = "ALAGOAS"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'AM'):
                        estado = "AMAZONAS"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'AP'):
                        estado = "AMAPÁ"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'BA'):
                        estado = "BAHIA"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'CE'):
                        estado = "CEARÁ"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'DF'):
                        estado = "DISTRITO FEDERAL"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'ES'):
                        estado = "ESPÍRITO SANTO"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'GO'):
                        estado = "GOIÁS"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'MA'):
                        estado = "MARANHÃO"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'MG'):
                        estado = "MINAS GERAIS"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'MS'):
                        estado = "MATO GROSSO DO SUL"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'MT'):
                        estado = "MATO GROSSO"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'PA'):
                        estado = "PARÁ"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'PB'):
                        estado = "PARAÍBA"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'PE'):
                        estado = "PERNAMBUCO"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'PI'):
                        estado = "PIAUÍ"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'PR'):
                        estado = "PARANÁ"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'RJ'):
                        estado = "RIO DE JANEIRO"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'RN'):
                        estado = "RIO GRANDE DO NORTE"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'RO'):
                        estado = "RONDÔNIA"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'RR'):
                        estado = "RORAIMA"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'RS'):
                        estado = "RIO GRANDE DO SUL"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'SC'):
                        estado = "SANTA CATARINA"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""

                    if (sigla == 'SE'):
                        estado = "SERGIPE"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)

                        estado = ""

                    if (sigla == 'TO'):
                        estado = "TOCANTINS"
                        output_path = "CAPAS_CONFECCIONADAS\LTOG" + sigla + "R.pdf"
                        create_pdf_with_image_and_text(image_path, estado, estado_x, estado_y, ano, ano_x, ano_y,
                                                       tipo_lista, tipo_lista_x, tipo_lista_y, output_path)
                        print(estado + " criado com o caminho e o nome de " + output_path)
                        estado = ""
                        break
            break

    return arquivos_encontrados


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

# Arquivos de entrada
# arquivo_origem = 'pagina.pdf'
# arquivo_destino = 'documento.pdf'

# Adiciona a primeira página de 'pagina.pdf' ao início de 'documento.pdf'
# adicionar_primeira_pagina(arquivo_origem, arquivo_destino)
#
# # Remove a segunda página de 'documento.pdf'
# remover_segunda_pagina(arquivo_destino)



#
# # Exemplo de uso
# image_path = "CAPA_IMAGEM.png"
# estado = "GOIÁS"
# estado_x = 80  # Coordenada X do texto no PDF
# estado_y = 300  # Coordenada Y do texto no PDF
#
# ano = "2023"
# ano_x = 100  # Coordenada X do texto no PDF
# ano_y = 300  # Coordenada Y do texto no PDF
#
# tipo_lista = "RESIDENCIAL"
# tipo_lista_x = 200  # Coordenada X do texto no PDF
# tipo_lista_y = 300  # Coordenada Y do texto no PDF
#
# output_path = "arquivo.pdf"
#
# create_pdf_with_image_and_text(image_path, estado,estado_x, estado_y, ano, ano_x, ano_y,tipo_lista,tipo_lista_x, tipo_lista_y, output_path)

caminho_pasta = 'C:/backup2023/OI/LISTA TELEFONICA/UF/RESIDENCIAL'  # Substitua pelo caminho desejado
siglas_desejadas = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'TO']

# arquivos_encontrados = criarCapaBaseadaNasListasJaCriadas(caminho_pasta, siglas_desejadas)

# if arquivo_encontrado:
#     print("Arquivo encontrado:", arquivo_encontrado)
# else:
#     print("Nenhum arquivo encontrado com a sigla na posição desejada.")
