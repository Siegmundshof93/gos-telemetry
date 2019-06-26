
#sat identifizirung
zweiSat = np.array(x13).reshape((1, len(df)))
einSat = zweiSat.flatten()
counts = np.bincount(einSat)
sat = np.argmax(counts)


#find picks (*1000 to convert A to mA)
max_x1 = np.around(max(x1), decimals=2) * 1000

min_x1 = np.around(min(x1), decimals=2) * 1000

max_x2 = np.around(max(x2), decimals=2) * 1000

min_x2 = np.around(min(x2), decimals=2) * 1000

max_x3 = np.around(max(x3), decimals=2)

min_x3 = np.around(min(x3), decimals=2)

max_x4 = np.around(max(x4), decimals=2) * 1000

min_x4 = np.around(min(x4), decimals=2) * 1000

max_x5 = np.around(max(x5), decimals=2) * 1000

min_x5 = np.around(min(x5), decimals=2) * 1000

max_x6 = np.around(max(x6), decimals=2) * 1000

min_x6 = np.around(min(x6), decimals=2) * 1000

max_x7 = np.around(max(x7), decimals=2) * 1000

min_x7 = np.around(min(x7), decimals=2) * 1000

max_x8 = np.around(max(x8), decimals=2) * 1000

min_x8 = np.around(min(x8), decimals=2) * 1000

max_x9 = np.around(max(x9), decimals=2) * 1000

min_x9 = np.around(min(x9), decimals=2) * 1000

max_x10 = np.around(max(x10), decimals=2) * 1000

min_x10 = np.around(min(x10), decimals=2) * 1000

max_x11 = np.around(max(x11), decimals=2) * 1000

min_x11 = np.around(min(x11), decimals=2) * 1000


#mean values
m1 = x1.mean()
m1 = np.around(m1, 2)
m2 = x2.mean()
m2 = np.around(m2, 2)
m3 = x3.mean()
m3 = np.around(m3, 2)
m4 = x4.mean()
m4 = np.around(m4, 2)
m5 = x5.mean()
m5 = np.around(m5, 2)
m6 = x6.mean()
m6 = np.around(m6, 2)
m7 = x7.mean()
m7 = np.around(m7, 2)
m8 = x8.mean()
m8 = np.around(m8, 2)
m9 = x9.mean()
m9 = np.around(m9, 2)
m10 = x10.mean()
m10 = np.around(m10, 2)
m11 = x11.mean()
m11 = np.around(m11, 2)




#strings in pdf
pdf = FPDF()
pdf.add_page()

pdf.set_font("Arial",'B', size=16)
pdf.cell(0, 30,'Data telemetry report',ln=1, align='C')

pdf.set_font("Arial", size=10)
#pdf.set_text_color(184,134,11)
if sat == 50:
    pdf.cell(0, 30,'Satellite:    Jaisat',ln=1, align='L')
elif sat == 40:
    pdf.cell(0, 30,'Satellite:    Lightsat',ln=1, align='L')
elif sat == 10:
    pdf.cell(0, 30,'Satellite:    Exoconnect',ln=1, align='L')

pdf.set_font('Arial', size=10)
pdf.cell(0, 0, 'Beguinning of the contact:         ' + beginning, ln=1,align='L')
pdf.cell(0, 10, 'End of the contact:                     ' + end, ln=1,align='L')
pdf.cell(0, 10, 'Duration of the communication : ' + DauerZeit, ln=1,align='L')




pdf.set_font('Arial','',10)

# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw/4

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Channel','Min. value','Mean Value','Max Value'],
('Battery charge [mA],%.2f,%.2f,%.2f' % (min_x1,m1,max_x1)).split(','),
('Battery discharge [mA],%.2f,%.2f,%.2f' % (min_x2,m2,max_x2)).split(','),
('Battery Voltage [V],%.2f,%.2f,%.2f' % (min_x3,m3,max_x3)).split(','),
('Vcc0 [mA],%.2f,%.2f,%.2f' % (min_x4,m4,max_x4)).split(','),
('Vcc1 [mA],%.2f,%.2f,%.2f' % (min_x5,m5,max_x5)).split(','),
('Vcc2 [mA],%.2f,%.2f,%.2f' % (min_x6,m6,max_x6)).split(','),
('Vcc3 [mA],%.2f,%.2f,%.2f' % (min_x7,m7,max_x7)).split(','),
('Vcc4 [mA],%.2f,%.2f,%.2f' % (min_x8,m8,max_x8)).split(','),
('Vcc5 [mA],%.2f,%.2f,%.2f' % (min_x9,m9,max_x9)).split(','),
('Vcc6 [mA],%.2f,%.2f,%.2f' % (min_x10,m10,max_x10)).split(','),
('Vcc7 [mA],%.2f,%.2f,%.2f' % (min_x11,m11,max_x11)).split(',')]


# Text height is the same as current font size
th = pdf.font_size

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)

    pdf.ln(2*th)




pdf.output("beschreibung.pdf")


exec(open("./merger.py").read())
