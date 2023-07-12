#ifndef GLOBAL_ENTITIES_H
#define GLOBAL_ENTITIES_H
/*  
for Target:
UNO:0
ESP32: 1
*/
#define RESOLUTION 15
#define BAUDRATE 115200
#define TARGET 0
// defines variables
long duration;
float distance[RESOLUTION];
int position = 0;
int currentIndexToUpbate = 0;
bool clockWise = true;

#endif