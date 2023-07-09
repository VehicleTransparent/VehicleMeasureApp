#include "GlobalEntities.h"
#include "US_interface.h"
#include "SERV_interface.h"

void setup() {
  US_vInit();
  SERV_vInit();
  Serial.begin(BAUDRATE); // Starts the serial communication
}

void loop() {
  SERV_vOrient(position);
  US_vGetDistance();
  COMM_vSendData();
  SERV_updateAngel();
  delay(15);
}

void COMM_vSendData (void)
{
  // Prints the distance on the Serial Monitor
  Serial.println("{\"DISTANCE\": [" + constructStr() + "] }");
}

String constructStr(void) {
  String dataToSend = "";
  for (int currentIndex = RESOLUTION-1 ; currentIndex > 0; currentIndex --)
  {
    dataToSend += String(distance[currentIndex]) + ", ";
  }
  dataToSend += distance[0];
  return dataToSend;
}
