#include "GlobalEntities.h"
#include "SERV_interface.h"
#include <Servo.h>

Servo angleorienter;
void SERV_vInit()
{
  angleorienter.attach(PIN_SERVO);  // attaches the servo on pin 9 to the servo object
}

void SERV_vOrient (float angle) {
  angleorienter.write(position);  
}

void SERV_updateAngel (void) {
  if ( (clockWise) ){
    SERV_updateAngelCW();
  }
  else {
    SERV_updateAngelCCW();
  }
}

void SERV_updateAngelCW (void)
{
  position = position + ANGEL_STEP;
  
  if (currentIndexToUpbate < RESOLUTION-1){
    currentIndexToUpbate++;  
  }
  if (position+ANGEL_STEP > ANGEL_MAX){
    clockWise = false;
  }
}

void SERV_updateAngelCCW (void)
{
  position = position - ANGEL_STEP;
  if (currentIndexToUpbate > 0)
  {
    currentIndexToUpbate--;
  }
  if (position-ANGEL_STEP < ANGEL_MIN){
    clockWise = true;
  }
}
