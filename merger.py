from PyPDF2 import PdfFileMerger


import fitz                          # <-- PyMuPDF
doc = fitz.open("beschreibung.pdf")          # open the PDF
rect = fitz.Rect(450,20,550,120)     # where to put image: use upper left corner

for page in doc:
    page.insertImage(rect, filename = "GOS.png")

doc.saveIncr()                       # do an incremental save


pdfs = ['beschreibung.pdf',  'plots.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(fileName, 'wb') as fout:
    merger.write(fout)
