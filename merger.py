from PyPDF2 import PdfFileMerger

pdfs = ['beschreibung.pdf',  'plots.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))
print(path)
with open(fileName, 'wb') as fout:
    merger.write(fout)
