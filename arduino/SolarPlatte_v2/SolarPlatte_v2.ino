/**
 * Bibliothek für Clock-Module
 */
#include <virtuabotixRTC.h>

/**
 * Werte für Spannung
 */
int U1;
int U2;
const int U1_pin = A5;
const int U2_pin = A4;
const int R1;
const int R2;
const int R3;
const int R4;

/**
 * Instanz erstellen
 * CLK | DAT | RST
 */
virtuabotixRTC clock(6, 7, 8);

void setup() {
  /**
   * serielle Verbindung zu PC aufbauen
   */
  Serial.begin(9600);
  while(!Serial){}
}

void loop() {
  /**
   * Zeit übergeben
   */
  clock.updateTime();
  String data = "";
  String tag = String(clock.dayofmonth);
  String monat = String(clock.month);
  String jahr = String(clock.year);
  String stunde = String(clock.hours);
  String minute = String(clock.minutes);
  String sekunde = String(clock.seconds);
  data += tag+"."+monat+"."+jahr+" "+stunde+":"+minute+":"+sekunde;

  data += ',';

  /**
   * Spannung messen
   */
  U1 = analogRead(U1_pin);
  U2 = analogRead(U2_pin);

  /**
   * Berechnungen zur Spannung
   */
  U1 = 1;
  U2 = 3;
  /**
   * an PC übergeben
   */
  data += '"';
  data += U1;
  data += '"';
  data += ',';
  data += '"';
  data += U2;
  data += '"';

  Serial.println(data);
  /**
   * warten, sonst zu viele Messungen
   */
  delay(5000);
}
