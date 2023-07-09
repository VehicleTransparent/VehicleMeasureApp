#include "GlobalEntities.h"
#include "US_interface.h"

void US_vInit(void)
{
  pinMode(PIN_TRIG, OUTPUT); // Sets the PIN_TRIG as an Output
  pinMode(PIN_ECHO, INPUT); // Sets the PIN_ECHO as an Input
}

void US_vGetDistance (void){
  // Clears the PIN_TRIG
  digitalWrite(PIN_TRIG, LOW);
  delayMicroseconds(2);
  // Sets the PIN_TRIG on HIGH state for 10 micro seconds
  digitalWrite(PIN_TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(PIN_TRIG, LOW);
  // Reads the PIN_ECHO, returns the sound wave travel time in microseconds
  duration = pulseIn(PIN_ECHO, HIGH);
  // Calculating the distance
  distance[currentIndexToUpbate] = duration * VOICE_SPEED_FACTOR / 2;
}