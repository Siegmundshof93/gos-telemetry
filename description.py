from fpdf import FPDF

import csv
import numpy as np
import pandas as pd
import numpy as np
import time
import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from sklearn.linear_model import LinearRegression
from fpdf import FPDF
df = pd.read_csv('/home/pvl/GOS/gos-telemetry/telemetry/1.csv',delimiter=';', index_col=False, skiprows=1) # Read csv file






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

#find picks

max_x1 = max(x1)
min_x1 = min(x1)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial",'B', size=16)
pdf.cell(200, 0,'Title',ln=1, align='C')
pdf.set_font('Arial', size=12)
pdf.cell(70, 30, 'Maximum Value of Battery charge is ' + str(max_x1), ln=1,align='C')
pdf.cell(70, 10, 'Minimum Value of Battery charge is ' + str(min_x1), ln=1,align='C')
pdf.output("beschreibung.pdf")


