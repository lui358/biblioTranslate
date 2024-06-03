import pdfplumber

def extraer_metadatos(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        texto = first_page.extract_text()
        # Asumimos que el título está en la primera línea
        titulo = texto.split('\n')[0]
        return titulo
