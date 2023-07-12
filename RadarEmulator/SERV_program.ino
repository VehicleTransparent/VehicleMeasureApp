#include "GlobalEntities.h"
#include "SERV_interface.h"

#if TARGET == 0
#include <Servo.h>

#elif TARGET == 1
#include <ESP32Servo.h>
#endif

Servo angleorienter;
void SERV_vInit()
{
  #if TARGET == 0
  angleorienter.attach(PIN_SERVO);  // attaches the servo on pin 9 to the servo object

  #elif TARGET == 1
  ESP32PWM::allocateTimer(0);
	ESP32PWM::allocateTimer(1);
	ESP32PWM::allocateTimer(2);
	ESP32PWM::allocateTimer(3);
	angleorienter.setPeriodHertz(50);    
	angleorienter.attach(PIN_SERVO, 500, 2400); 
  #endif
  
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
