import tkinter as tk
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
from tkinter import filedialog
from tkinter import simpledialog


 
app_window = tk.Tk()
app_window.withdraw()

#data = 'planet_order_301232.zip'
#data = 'Zip/planet_order_301232.zip' #full zip file path
file_path = filedialog.askopenfile(initialdir='/home/pvl/GOS/gos-telemetry/telemetry/',
title='Select the ZIP file'
).name #dialog window, for manuel ZIP-file search

df = pd.read_csv(file_path, delimiter=';', index_col=False, skiprows=1) # Read csv file

#path = '/'.join(file_path.split('/')[:-1])
#print(file_path, path)

#Noise remover
for k in range(len(df)):
	if (df.iloc[k,3]>10):
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


#print(max_x1)


#convertation to human readable time
time = np.array(t/1000)
time = np.asarray(time, dtype='datetime64[s]')


#trendline for charge
modelCharge = LinearRegression()
modelCharge.fit(t, x1)
trendCharge = modelCharge.predict(t)

#trendline for discharge
modelDischarge = LinearRegression()
modelDischarge.fit(t, x2)
trendDischarge = modelDischarge.predict(t)

#trendline for Voltage of the battery
modelVoltage = LinearRegression()
modelVoltage.fit(t, x3)
trendVoltage = modelVoltage.predict(t)

#trendline for Vcc0
modelVcc0 = LinearRegression()
modelVcc0.fit(t, x4)
trendVcc0 = modelVcc0.predict(t)

#trendline for Vcc1
modelVcc1 = LinearRegression()
modelVcc1.fit(t, x5)
trendVcc1 = modelVcc1.predict(t)

#trendline for Vcc2
modelVcc2 = LinearRegression()
modelVcc2.fit(t, x6)
trendVcc2 = modelVcc2.predict(t)

#trendline for Vcc3
modelVcc3 = LinearRegression()
modelVcc3.fit(t, x7)
trendVcc3 = modelVcc3.predict(t)

#trendline for Vcc4
modelVcc4 = LinearRegression()
modelVcc4.fit(t, x8)
trendVcc4 = modelVcc4.predict(t)

#trendline for Vcc5
modelVcc5 = LinearRegression()
modelVcc5.fit(t, x9)
trendVcc5 = modelVcc5.predict(t)

#trendline for Vcc6
modelVcc6 = LinearRegression()
modelVcc6.fit(t, x10)
trendVcc6 = modelVcc2.predict(t)

#trendline for Vcc7
modelVcc7 = LinearRegression()
modelVcc7.fit(t, x11)
trendVcc7 = modelVcc7.predict(t)

#plots

with PdfPages('plots.pdf') as pdf:









 plt.subplot()
 plt.title('Battery charge/discharge')
 plt.plot(time, x1, color='red', label='charge')
 plt.plot(time, x2, color='green', label='discharge')
 plt.plot(time, trendCharge,'r--' )
 plt.plot(time, trendDischarge,'g--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
# plt.show()
 pdf.savefig()

 plt.close() 
 

 plt.subplot()
 plt.title('Battery Voltage')
 plt.plot(time, x3, label='voltage')
 plt.plot(time, trendVoltage,'b--')
 plt.ylabel('Voltage level [V]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
 #plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 0')
 plt.plot(time, x4, label='current')
 plt.plot(time, trendVcc0,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
# plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 1')
 plt.plot(time, x5, label='current')
 plt.plot(time, trendVcc1,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
 #plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 2')
 plt.plot(time, x6, label='current')
 plt.plot(time, trendVcc2,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
# plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 3')
 plt.plot(time, x7, label='current')
 plt.plot(time, trendVcc3,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
# plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 4')
 plt.plot(time, x8, label='current')
 plt.plot(time, trendVcc4,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
 #plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 5')
 plt.plot(time, x9, label='current')
 plt.plot(time, trendVcc5,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
# plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 6')
 plt.plot(time, x10, label='current')
 plt.plot(time, trendVcc6,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
 #plt.show()
#plt.show(block=False)
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Vcc 7')
 plt.plot(time, x11, label='current')
 plt.plot(time, trendVcc7,'b--')
 plt.ylabel('Consumed current [A]')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
#plt.savefig('path_to_folder/name.png')
 #plt.show()
 pdf.savefig()
 plt.close()

 plt.subplot()
 plt.title('Mode')
 plt.plot(time, x12, label='current')
 plt.ylabel('')
 plt.xlabel('time')
 plt.legend(loc='upper right')
 plt.grid(True)
 #plt.show()
 pdf.savefig()
 plt.close()

exec(open("./description.py").read())




