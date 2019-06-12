from fpdf import FPDF

import csv
import numpy as np
import pandas as pd
import numpy as np
import time
import datetime
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
df = pd.read_csv(file_path, delimiter=';', index_col=False, skiprows=1) # Read csv file






#Noise remover
for k in range(len(df)):
	if (df.iloc[k,3]>8):
		#print('Found one')
		#print(df.iloc[k-1,3],df.iloc[k,3])
		df.iloc[k,:] = df.iloc[k-1,:]
		#print('replaced it with', df.iloc[k,3])
		#np.replace()




t   = df.iloc[:, 0].values.reshape(-1, 1) # Time, first collumn
x1  = df.iloc[:, 1].values.reshape(-1, 1) # Charge of Battery, second column
x2  = df.iloc[:, 2].values.reshape(-1, 1) # Discharge of Battery, third column
x3  = df.iloc[:, 3].values.reshape(-1, 1) #Voltage of the battery, forth column
x4  = df.iloc[:,14].values.reshape(-1, 1) #Vcc0, 15th column
x5  = df.iloc[:,15].values.reshape(-1, 1) #Vcc1, 16th column
x6  = df.iloc[:,16].values.reshape(-1, 1) #Vcc2, 17th column
x7  = df.iloc[:,17].values.reshape(-1, 1) #Vcc3, 18th column
x8  = df.iloc[:,18].values.reshape(-1, 1) #Vcc4, 19th column
x9  = df.iloc[:,19].values.reshape(-1, 1) #Vcc5, 20th column
x10 = df.iloc[:,20].values.reshape(-1, 1) #Vcc6, 21th column
x11 = df.iloc[:,21].values.reshape(-1, 1) #Vcc7, 22th column
x12 = df.iloc[:,36].values.reshape(-1, 1) #Mode, 37th column
x13 = df.iloc[:,41].values.reshape(-1, 1) #Satellite ID

#sat identifizirung
zweiSat = np.array(x13).reshape((1, len(df)))
einSat = zweiSat.flatten()
counts = np.bincount(einSat)
sat = np.argmax(counts)



#find picks

max_x1  = max(x1 )
min_x1  = min(x1 )
max_x2  = max(x2 )
min_x2  = min(x2 )
max_x3  = max(x3 )
min_x3  = min(x3 )
max_x4  = max(x4 )
min_x4  = min(x4 )
max_x5  = max(x5 )
min_x5  = min(x5 )
max_x6  = max(x6 )
min_x6  = min(x6 )
max_x7  = max(x7 )
min_x7  = min(x7 )
max_x8  = max(x8 )
min_x8  = min(x8 )
max_x9  = max(x9 )
min_x9  = min(x9 )
max_x10 = max(x10)
min_x10 = min(x10)
max_x11 = max(x11)
min_x11 = min(x11)
max_x12 = max(x12)
min_x12 = min(x12)

#strings in pdf
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",'B', size=16)
if sat == 50:
    pdf.cell(200, 30,'Jaisat',ln=1, align='C')
elif sat == 40:
    pdf.cell(200, 30,'Lightsat',ln=1, align='C')
elif sat == 10:
    pdf.cell(200, 30,'Exoconnect',ln=1, align='C')
pdf.set_font('Arial', size=12)
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



pdf.output("beschreibung.pdf")


exec(open("./merger.py").read())
