#include <Stepper.h>

const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor
const int motor_pin_1 = 3;
const int motor_pin_2 = 4;
const int motor_pin_3 = 6;
const int motor_pin_4 = 7;

// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 3, 4, 6, 7);

int stepCount = 0;  // number of steps the motor has taken

void setup() {
  digitalWrite(2,HIGH);
  digitalWrite(5,HIGH);
   //myStepper.setSpeed(150);
  // nothing to do inside the setup
  Serial.begin(38400);
  pinMode(10, OUTPUT);
  //digitalWrite(10, HIGH);
}

void loop() {
    unsigned long t1, t2;
   //onestep(3000);
    // step 1/100 of a revolution:
    for(int i = 0; i<200; i++){
       t1 = micros();
       //onestep(i);
       delayMicroseconds(2000);
       t2= micros();
       delay(0);
    }
    delay(1000);

    
  }
  
void onestep(int sequence) {
 switch(sequence%4){
  case 0:
    digitalWrite(motor_pin_1, HIGH);
  digitalWrite(motor_pin_2, LOW);
  digitalWrite(motor_pin_3, HIGH);
  digitalWrite(motor_pin_4, LOW);
  break;

  case 1:
    digitalWrite(motor_pin_1, LOW);
  digitalWrite(motor_pin_2, HIGH);
  digitalWrite(motor_pin_3, HIGH);
  digitalWrite(motor_pin_4, LOW);
  break;
  case 2:
    digitalWrite(motor_pin_1, LOW);
  digitalWrite(motor_pin_2, HIGH);
  digitalWrite(motor_pin_3, LOW);
  digitalWrite(motor_pin_4, HIGH);
  break;
  case 3:
    digitalWrite(motor_pin_1, HIGH);
  digitalWrite(motor_pin_2, LOW);
  digitalWrite(motor_pin_3, LOW);
  digitalWrite(motor_pin_4, HIGH);
  break;
 }
}

