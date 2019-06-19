from PyPDF2 import PdfFileMerger

pdfs = [r'C:\Users\Hugo Tamini\Desktop\Pavel\gos-telemetry\beschreibung.pdf',  r'C:\Users\Hugo Tamini\Desktop\Pavel\gos-telemetry\plots.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open(r'C:\Users\Hugo Tamini\Desktop\Pavel\gos-telemetry\ergebnisse.pdf', 'wb') as fout:
    merger.write(fout)
