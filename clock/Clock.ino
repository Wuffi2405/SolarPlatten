#include <virtuabotixRTC.h>

virtuabotixRTC myRTC(6, 7, 8);

void setup() {
   Serial.begin(9600);
   /**
    * s | min | h | wochentag | tag | monat | jahr
    */
   myRTC.setDS1302Time(00, 00, 21, 2, 15, 2, 2019);

   Serial.println("Test");
}

void loop() {
  myRTC.updateTime();
  
   Serial.print("Current Date / Time: ");
 Serial.print(myRTC.dayofmonth); //You can switch between day and month if you're using American system
 Serial.print("/");
 Serial.print(myRTC.month);
 Serial.print("/");
 Serial.print(myRTC.year);
 Serial.print(" ");
 Serial.print(myRTC.hours);
 Serial.print(":");
 Serial.print(myRTC.minutes);
 Serial.print(":");
 Serial.println(myRTC.seconds);

 delay(1000);
}
