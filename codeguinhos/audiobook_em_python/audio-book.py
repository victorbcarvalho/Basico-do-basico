import pyttsx3
import PyPDF2

pdf = open('seu_arquivo.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf)
engine = pyttsx3.init()

for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    engine.save_to_file(text, f'meu_arquivo_pagina{page_num}.mp3')

engine.runAndWait()
pdf.close()