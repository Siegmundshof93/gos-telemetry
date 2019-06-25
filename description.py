
#sat identifizirung
zweiSat = np.array(x13).reshape((1, len(df)))
einSat = zweiSat.flatten()
counts = np.bincount(einSat)
sat = np.argmax(counts)


#find picks
max_x1  = max(x1 )
max_x1 = np.around(max_x1, decimals=2) * 1000
#max_x1 = np.savetxt(sys.stdout.buffer, max_x1)
#print(max_x1)

min_x1  = min(x1 )
min_x1 = np.around(min_x1, decimals=2) * 1000
#min_x1 = np.savetxt(sys.stdout.buffer, min_x1)


max_x2  = max(x2 )
max_x2 = np.around(max_x2, decimals=2) * 1000

min_x2  = min(x2 )
min_x2 = np.around(min_x2, decimals=2) * 1000

max_x3  = max(x3 )
max_x3 = np.around(max_x3, decimals=2)

min_x3  = min(x3 )
max_x3 = np.around(max_x3, decimals=2)

max_x4  = max(x4 )
max_x4 = np.around(max_x4, decimals=2) * 1000

min_x4  = min(x4 )
min_x4 = np.around(min_x4, decimals=2) * 1000

max_x5  = max(x5 )
max_x5 = np.around(max_x5, decimals=2) * 1000

min_x5  = min(x5 )
min_x5 = np.around(min_x5, decimals=2) * 1000

max_x6  = max(x6 )
max_x6 = np.around(max_x6, decimals=2) * 1000

min_x6  = min(x6 )
min_x6 = np.around(min_x6, decimals=2) * 1000

max_x7  = max(x7 )
max_x7 = np.around(max_x7, decimals=2) * 1000

min_x7  = min(x7 )
min_x7 = np.around(min_x7, decimals=2) * 1000

max_x8  = max(x8 )
max_x8 = np.around(max_x8, decimals=2) * 1000

min_x8  = min(x8 )
min_x8 = np.around(min_x8, decimals=2) * 1000

max_x9  = max(x9 )
max_x9 = np.around(max_x9, decimals=2) * 1000

min_x9  = min(x9 )
min_x9 = np.around(min_x9, decimals=2) * 1000

max_x10 = max(x10)
max_x10 = np.around(max_x10, decimals=2) * 1000

min_x10 = min(x10)
min_x10 = np.around(min_x10, decimals=2) * 1000

max_x11 = max(x11)
max_x11 = np.around(max_x11, decimals=2) * 1000

min_x11 = min(x11)
min_x11 = np.around(min_x11, decimals=2) * 1000


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
pdf.cell(0, 30,'Report',ln=1, align='C')

pdf.set_font("Arial", size=10)
#pdf.set_text_color(184,134,11)
if sat == 50:
    pdf.cell(0, 30,'satellite: Jaisat',ln=1, align='L')
elif sat == 40:
    pdf.cell(0, 30,'satellite: Lightsat',ln=1, align='L')
elif sat == 10:
    pdf.cell(0, 30,'satellite: Exoconnect',ln=1, align='L')

pdf.set_font('Arial', size=10)
pdf.cell(0, 0, 'Beguinning of the contact: ' + str(time[0]), ln=1,align='L')
pdf.cell(0, 30, 'End of the contact: ' + str(time[len(time) - 1]), ln=1,align='L')


#pdf.cell(40, 10, 'End of the contact ' + str(time[len(df)]), ln=0,align='L')


pdf.set_font('Arial','',10)

# Effective page width, or just epw
epw = pdf.w - 2*pdf.l_margin

# Set column width to 1/4 of effective page width to distribute content
# evenly across table and page
col_width = epw/4

# Since we do not need to draw lines anymore, there is no need to separate
# headers from data matrix.

data = [['Channel','Min. value','Mean Value','Max Value'],
['Battery charge [mA]',min_x1,m1,max_x1],
['Battery discharge [mA]',min_x2,m2,max_x2],
['Battery Voltage [V]',min_x3,m3, min_x3 ],
['Vcc0 [mA]',min_x4,m4,max_x4],
['Vcc1 [mA]',min_x5,m5,max_x5],
['Vcc2 [mA]',min_x6,m6,max_x6],
['Vcc3 [mA]',min_x7,m7,max_x7],
['Vcc4 [mA]',min_x8,m8,max_x8],
['Vcc5 [mA]',min_x9,m9,max_x9],
['Vcc6 [mA]',min_x10,m10,max_x10],
['Vcc7 [mA]',min_x11,m11,max_x11]]


# Text height is the same as current font size
th = pdf.font_size

# Here we add more padding by passing 2*th as height
for row in data:
    for datum in row:
        # Enter data in colums
        pdf.cell(col_width, 2*th, str(datum), border=1)

    pdf.ln(2*th)





"""
pdf.set_font('Arial', size=10)
pdf.cell(30, 10, 'Maximum Value of Battery charge is ' + str(max_x1), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery charge is ' + str(min_x1), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery discharge is ' + str(max_x2), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery discharge is ' + str(min_x2), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Voltage is ' + str(max_x3), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Voltage is ' + str(min_x3), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc0 is ' + str(max_x4), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc0 is ' + str(min_x4), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc1 is ' + str(max_x5), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc1 is ' + str(min_x5), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc2 is ' + str(max_x6), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc2 is ' + str(min_x6), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc3 is ' + str(max_x7), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc3 is ' + str(min_x7), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc4 is ' + str(max_x8), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc4 is ' + str(min_x8), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc5 is ' + str(max_x9), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc5 is ' + str(min_x9), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc6 is ' + str(max_x10), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc6 is ' + str(min_x10), ln=1,align='R')
pdf.cell(30, 10, 'Maximum Value of Battery Vcc7 is ' + str(max_x11), ln=0,align='L')
pdf.cell(160, 10, 'Minimum Value of Battery Vcc7 is ' + str(min_x11), ln=1,align='R')
"""


pdf.output("beschreibung.pdf")


exec(open("./merger.py").read())
