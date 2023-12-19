
from pypdf import PdfWriter, PdfReader
from datetime import datetime
from io import BytesIO
import streamlit as st

st.set_page_config(
	page_title = 'Juntar PDFs',
	page_icon = 'https://www.science.co.il/internet/browsers/PDF-doc-256.png',
	initial_sidebar_state = 'collapsed' 
)

st.header('Juntar e Separar Documentos PDF')

def juntar_pdf_e_exportar(lista_pdfs: list) -> bytes:
	pdf = PdfWriter()
	for i in lista_pdfs:
		pdf.append(i)
	
	bytes_file = BytesIO()
	pdf.write(bytes_file)
	pdf.close()
	
	dados_processados = bytes_file.getvalue()
	return dados_processados

def paginas_pdf(file) -> int:
	try:
		pdf = PdfReader(file)
		return len(pdf.pages) + 1
	except:
		return 1

def cortar_pdf(file, lista_paginas: list) -> bytes:
	if file is not None:
		pdfr = PdfReader(file)
		pdfw = PdfWriter()
	
		for i in lista_paginas:
			pdfw.add_page(pdfr.pages[i - 1])
	
		bytes_file = BytesIO()
		pdfw.write(bytes_file)
		pdfw.close()
	
		dados_processados = bytes_file.getvalue()
		return dados_processados

st.write('#### Juntar PDFs')
arquivos_pdfs = st.file_uploader(
	'Buscar arquivos neste computador',
	'pdf',
	accept_multiple_files = True
)

nome_arquivo1 = st.text_input('Nome do arquivo (1)')
st.download_button(
	label = 'Juntar e Baixar PDF',
	data = juntar_pdf_e_exportar(arquivos_pdfs),
	file_name = f'''{nome_arquivo1}_{int(datetime.now().timestamp())}.pdf'''
)

st.write('#### Cortar PDFs')
arquivo_pdf = st.file_uploader(
	'Buscar arquivo neste computador',
	'pdf'
)

nome_arquivo2 = st.text_input('Nome do arquivo (2)')
paginas = st.multiselect('Páginas selecionadas', options = range(1, paginas_pdf(arquivo_pdf)))

st.download_button(
	label = 'Baixar PDF',
	data = cortar_pdf(arquivo_pdf, paginas),
	file_name = f'''{nome_arquivo2}_{int(datetime.now().timestamp())}.pdf'''
)
