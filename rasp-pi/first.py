import serial				#Arduino Verbindung
import os					#für Ordner Handling

#arduino = serial.Serial('COM6', 9600, timeout=.1)

#ZUM BEARBEITEN
PATH = ""
LENGTH = 80

#andere Variablen
today_old = 0
#Überprüfung, ob Unterordner existieren
if os.path.isdir(PATH + "/tageslisten"):
	print("Ordner existiert")
else:
	print("Bitte einen Ordner 'Tageslisten' erstellen")
	
while True:
	
	#Daten für Speicherung preparieren
		#data = arduino.readline()[:-2]
	data = ',08.06.2019 16:45:49,"0,00","3,18","0,00","0,00",0,0,1,0000,0651,0000,0000,01,""'
	x = data.split('"')
	value = x[0].replace(',', '') + "," + x[1].replace(',', '.') + "," + x[3].replace(',', '.')
	print(value)
	
	date = x[0].split(" ")
	today = date[0].replace(",", "")
	print(today)
	
	#if today_old == today:
	#	print("selber Tag")
	#else:
	#	today_old = today
	#	print("neuer Tag")
		
	if data:
		f = open(PATH + 'messungen_roh.csv', 'a')
		#f.write(PATH + '\n' + value.decode('utf-8'))
		f.write(PATH + '\n' + value)
		f.close()
		
		f = open(PATH + "tageslisten/"+today+".csv", 'a')
		#f.write(PATH + '\n' + value.decode('utf-8'))
		f.write(PATH + '\n' + value)
		f.close()
		
		#print(data)
	
	break