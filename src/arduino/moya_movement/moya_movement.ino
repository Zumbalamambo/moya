
/* Initialize stepper motor pins */
const int stepper1 = 11;
const int dir1 = 10;
const int led = 13;
const int stepper2 = 7;
const int dir2 = 6;

/* Include ROS and the messages */
#include <ros.h>
#include <std_msgs/Int16.h>

int input = 3;

ros::NodeHandle nh;

/* callback function used when message is receieved*/
void messageCb( const std_msgs::Int16& cmd_vel) {
  input = cmd_vel.data;
  digitalWrite(led, LOW);
}

/* Subscribe to /cmd_vel */
ros::Subscriber<std_msgs::Int16> sub("/cmd_vel", &messageCb );

void setup() {
  // put your setup code here, to run once:
  pinMode(stepper1, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(stepper2, OUTPUT);
  pinMode(dir2, OUTPUT);
  digitalWrite(dir1, LOW);
  digitalWrite(stepper1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(stepper2, LOW);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  if(input==1) {
    onestep(true);
    onestep2(true);
    digitalWrite(led, HIGH);
  }
  else if (input ==2) {
    onestep(false);
    onestep2(true);
    digitalWrite(led, LOW);
  }
  else if (input == 3) {
    digitalWrite(led, LOW);
    digitalWrite(led, LOW);
  }
  else if (input ==5) {
    onestep(false);
    onestep2(false);
    digitalWrite(led, HIGH);
  }
  else if (input ==4) {
    onestep(true);
    onestep2(false);
    digitalWrite(led, LOW);
  }
  delay(1);
}

void onestep(bool direction) {
    digitalWrite(dir1, direction);
    digitalWrite(stepper1, HIGH);
    delayMicroseconds(2500);
    digitalWrite(stepper1, LOW);
    delayMicroseconds(2500);
}
void onestep2(bool direction) {
    digitalWrite(dir2, direction);
    digitalWrite(stepper2, HIGH);
    delayMicroseconds(2500);
    digitalWrite(stepper2, LOW);
    delayMicroseconds(2500);
}

