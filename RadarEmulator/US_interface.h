#ifndef US_INTERFACE_H
#define US_INTERFACE_H

#if TARGET == 0
#define PIN_TRIG 3
#define PIN_ECHO 2
#elif TARGET == 1
#define PIN_TRIG 23
#define PIN_ECHO 22
#endif

#define VOICE_SPEED_FACTOR 0.034

void US_vInit(void);
void US_vGetDistance(void);

#endif