
const int stepper = 11;
const int dir = 10;


void setup() {
  // put your setup code here, to run once:
  pinMode(stepper, OUTPUT);
  pinMode(dir, OUTPUT);
  digitalWrite(dir, LOW);
  digitalWrite(stepper, LOW);
}

void loop() {
  //for(int i = 0; i<200; i++) {
      // put your main code here, to run repeatedly:
  digitalWrite(stepper, HIGH);
  delayMicroseconds(100);
  digitalWrite(stepper, LOW);
  delayMicroseconds(100);
//  }
  //delay(1000);
}
