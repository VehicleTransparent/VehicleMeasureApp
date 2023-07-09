#ifndef US_INTERFACE_H
#define US_INTERFACE_H

#define PIN_TRIG 3
#define PIN_ECHO 2
#define VOICE_SPEED_FACTOR  0.034

void US_vInit        (void);
void US_vGetDistance (void);

#endif