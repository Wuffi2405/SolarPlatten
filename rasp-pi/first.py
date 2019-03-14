import serial

arduino = serial.Serial('COM6', 9600, timeout=.1)
x = 0
while True:
	data = arduino.readline()[:-2]
	if data:
		f = open('messungen.csv', 'a')
		f.write('\n' + data.decode('utf-8'))
		print(data)
		f.close()
	x +=1;