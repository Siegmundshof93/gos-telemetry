from PyPDF2 import PdfFileMerger

pdfs = ['beschreibung.pdf',  'plots.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('ergebnisse.pdf', 'wb') as fout:
    merger.write(fout)
