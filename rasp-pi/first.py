import serial				#Arduino Verbindung
import os					#für Ordner Handling

#
#ZUM BEARBEITEN --- VARIABLEN
#
PATH = ""
LENGTH = 80
DEBUG = True;

#
#andere Variablen
#
today_old = 0

#
#NullPath durch aktuelles Verzeichnis ersetzen
#
if PATH == "":
	PATH = os.path.dirname(os.path.abspath(__file__))

#
#Herstellung einer Verbindung zum Arduino
#
if DEBUG == False:
	arduino = serial.Serial('COM6', 9600, timeout=.1)

#
#Ueberprüfung, ob Unterordner existieren
#
if os.path.isdir(PATH + "/tageslisten"):
	if DEBUG == True:
		print("[INFO] Ordner '" + PATH + "/tageslisten' existiert")
else:
	print("[ERROR] Ordner '" + PATH + "/tageslsiten' existiert nicht")
	
while True:
	
	#
	#Daten für Speicherung preparieren
	#
	if DEBUG == False:	
		data = arduino.readline()[:-2]
	else:
		data = ',10.06.2019 16:45:49,"0,00","3,18","0,00","0,00",0,0,1,0000,0651,0000,0000,01,""'
		
	if len(data) == LENGTH:
		#
		#Datenzeile wird geteilt
		#wichtige Daten werden in Variable gespeichert
		#
		x = data.split('"')
		value = x[0].replace(',', '') + "," + x[1].replace(',', '.') + "," + x[3].replace(',', '.')
		print("[INFO] Datenzeile: " + value)
	
		date = x[0].split(" ")
		today = date[0].replace(",", "")
		print("[LOL] heutiges Datum: " + today)
	
		#
		#rohe Daten >> messungen_roh.csv
		#
		f = open(PATH + '\messungen_roh.csv', 'a')
		#f.write('\n' + value.decode('utf-8'))
		f.write('\n' + data)
		f.close()
		
		#
		#optimierte Daten >> messungen.csv
		#
		f = open(PATH + '\messungen.csv', 'a')
		#f.write('\n' + value.decode('utf-8'))
		f.write('\n' + value)
		f.close()
		
		#
		#tagesspezif. Daten >> tageslisten
		#
		f = open(PATH + "/tageslisten/"+today+".csv", 'a')
		#f.write('\n' + value.decode('utf-8'))
		f.write('\n' + value)
		f.close()
		
		#print(data)
	
	break