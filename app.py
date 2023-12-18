
from pypdf import PdfWriter
from datetime import datetime
from io import BytesIO
import streamlit as st

st.set_page_config(
	page_title = 'Juntar PDFs',
	page_icon = 'https://www.science.co.il/internet/browsers/PDF-doc-256.png',
	initial_sidebar_state = 'collapsed' 
)

def juntar_pdf_e_exportar(lista_pdfs: list) -> bytes:
	pdf = PdfWriter()
	for i in lista_pdfs:
		pdf.append(i)
	
	bytes_file = BytesIO()
	pdf.write(bytes_file)
	pdf.close()
	
	dados_processados = bytes_file.getvalue()
	return dados_processados

st.header('Juntar PDFs')
arquivos_pdfs = st.file_uploader(
	'Juntar PDFs',
	'pdf',
	accept_multiple_files = True
)

nome_arquivo = st.text_input('Nome do Arquivo')
st.download_button(
	label = 'Juntar e Baixar PDF',
	data = juntar_pdf_e_exportar(arquivos_pdfs),
	file_name = f'''{nome_arquivo}_{int(datetime.now().timestamp())}.pdf'''
)
