#ifndef GLOBAL_ENTITIES_H
#define GLOBAL_ENTITIES_H

#define RESOLUTION 15
#define BAUDRATE  115200

// defines variables
long   duration;
float  distance [RESOLUTION] ;
int    position = 0;
int    currentIndexToUpbate = 0;
bool   clockWise = true; 

#endif