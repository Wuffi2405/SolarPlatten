import serial				#Arduino Verbindung
import os					#fuer Ordner Handling

#
#ZUM BEARBEITEN --- VARIABLEN
#
PATH = ""
DEBUG = True;
LINUX = False;

#
#andere Variablen
#
today_old = 0
lastDataset = "";

#
#NullPath durch aktuelles Verzeichnis ersetzen
#
if PATH == "":
	PATH = os.path.dirname(os.path.abspath(__file__))

#
#Herstellung einer Verbindung zum Arduino
#
if DEBUG == False:
	if LINUX == True:
		arduino = serial.Serial('/dev/ttyUSB0', 9600, timeout=.1)
	else:
		arduino = serial.Serial('COM6', 9600, timeout=.1)

#
#Ueberpruefung, ob Unterordner existieren
#
if os.path.isdir(PATH + "/tageslisten"):
	if DEBUG == True:
		print("[INFO] Ordner '" + PATH + "/tageslisten' existiert")
else:
	print("[ERROR] Ordner '" + PATH + "/tageslsiten' existiert nicht")
	
while True:
	
	#
	#Daten fuer Speicherung preparieren
	#
	if DEBUG == False:	
		data = arduino.readline()[:-2]
	else:
		data = ',29.03.2019 16:46:44,"0,00","3,16","0,00","0,00",0,0,0,0000,0647,0000,0000,026,",29.03.2019 16:47:23,REPEAT:"'
		
	if len(data)>=79 and data[79] == '"':
		#print(data[79])
	
		#
		#Datenzeile wird geteilt
		#wichtige Daten werden in Variable gespeichert
		#
		x = data.split('"') #Zeile unterteilen
		date = x[0].split(" ") #Datum und Zeit in Variable trennen
		today = date[0].replace(",", "") #Komma am Anfang loeschen
		
		if lastDataset == x[0]:
			print("[WARNING] die Zeile ist bereits vorhanden")
		else:
			lastDataset = x[0]
			value = x[0].replace(',', '') + "," + x[1].replace(',', '.') + "," + x[3].replace(',', '.') #Datenzeile fuer Tageslisten vorbereiten
		 
			print("[INFO] Datenzeile: " + value)
			print("[INFO] heutiges Datum: " + today)
	
			#
			#rohe Daten >> messungen_roh.csv
			#
			f = open(PATH + '/messungen_roh.csv', 'a')
			#f.write('\n' + value.decode('utf-8'))
			f.write('\n' + data)
			f.close()
		
			#
			#optimierte Daten >> messungen.csv
			#
			f = open(PATH + '/messungen.csv', 'a')
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
		
			print("[INFO] " + value)
	else:
		print("[ERROR] die Datenzeile wurde nicht korrekt uebermittelt")
	break