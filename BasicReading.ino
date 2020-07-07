#include <SoftwareSerial.h>

//Create software serial object to communicate with SIM800L
SoftwareSerial mySerial(5,4); //SIM800L Tx & Rx is connected to Arduino #3 & #2
String s;
char c;
void setup()
{
  //Begin serial communication with Arduino and Arduino IDE (Serial Monitor)
  Serial.begin(115200);
  
  //Begin serial communication with Arduino and SIM800L
  mySerial.begin(115200);

  Serial.println("Initializing..."); 
  delay(1000);

  mySerial.println("AT"); //Once the handshake test is successful, it will back to OK
  updateSerial();
  
  mySerial.println("AT+CMGF=1"); // Configuring TEXT mode
  updateSerial();
  mySerial.println("AT+CNMI=1,2,0,0,0"); // Decides how newly arrived SMS messages should be handled  AT+CNMI=<mode>,<mt>,<bm>,<ds>,<bfr>
  updateSerial();
}

void loop()
{
  u: updateSerial();
  // delay(200);
}

void updateSerial()
{ 

  while (Serial.available()) 
  {
    mySerial.write(Serial.read());//Forward what Serial received to Software Serial Port
  } 
  while(mySerial.available()) 
  {
    Serial.write(mySerial.read());
  }
}
