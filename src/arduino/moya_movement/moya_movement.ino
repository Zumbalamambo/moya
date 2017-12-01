
/* Initialize stepper motor pins */
const int stepper = 11;
const int dir = 10;
const int led = 13;

/* Include ROS and the messages */
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

/* callback function used when message is receieved*/
void messageCb( const std_msgs::Int16& cmd_vel) {
  int input = cmd_vel.data;
  digitalWrite(led, LOW);
  if(input==1) {
      digitalWrite(led, HIGH);
  }
  else if (input ==2) {
    digitalWrite(led, HIGH);
    delay(100);
    digitalWrite(led, LOW);
    delay(100);
  }
  else if (input == 3) {
    digitalWrite(led, LOW);
  }
  else {
    digitalWrite(led, HIGH);
    delay(100);
    digitalWrite(led, LOW);
    delay(100);
  }
}

/* Subscribe to /cmd_vel */
ros::Subscriber<std_msgs::Int16> sub("/cmd_vel", &messageCb );

void setup() {
  // put your setup code here, to run once:
  pinMode(stepper, OUTPUT);
  pinMode(dir, OUTPUT);
  digitalWrite(dir, LOW);
  digitalWrite(stepper, LOW);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
//  digitalWrite(12, LOW);
//  digitalWrite(13, LOW);
  nh.initNode();
  nh.subscribe(sub);
}

void loop() {
  nh.spinOnce();
  delay(1);
}

void onestep() {
    digitalWrite(stepper, HIGH);
  delayMicroseconds(1800);
  digitalWrite(stepper, LOW);
  delayMicroseconds(1800);
}

