import serial				#Arduino Verbindung
from datetime import date	#für das heutige Datum
import os					#für Ordner Handling

#arduino = serial.Serial('COM6', 9600, timeout=.1)

#Referenzvariable für den heuteigen Tag
today = str(date.today())

#Überprüfung, ob Unterordner existieren
#print(os.getcwd())
if os.path.isdir("/tageslisten"):
	print("Ordner existiert")
else:
	print("Bitte einen Ordner 'Tageslisten' erstellen")
#	os.rmdir("/tageslisten")
#else:
#	try:  
#		os.mkdir("\\tageslisten")
#	except OSError:  
#		print ("Creation of the directory %s failed" % "/tageslisten")
#	else:  
#		print ("Successfully created the directory %s" % "/tageslisten")
	
while True:

	if today == str(date.today()):
		print(today)
	else:
		today = str(date.today());
	
	data = arduino.readline()[:-2]
	#data = ';08.03.2019 16:45:49;"0,00";"3,18";"0,00";"0,00";0;0;1;0000;0651;0000;0000;01;""'
	if data:
		f = open('messungen_roh.csv', 'a')
		f.write('\n' + data.decode('utf-8'))
		#f.write('\n' + data)
		f.close()
		
		f = open("tageslisten/"+today+".csv", 'a')
		f.write('\n' + data.decode('utf-8'))
		#f.write('\n' + data)
		f.close()
		
		print(data)
		#today = str(date.today())
		#print(today)
	
	break