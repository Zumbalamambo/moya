
const int stepper = 11;
const int dir = 10;
const int led = 13;

#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle nh;

void messageCb( const std_msgs::Int16& toggle_msg) {
  int input = toggle_msg.data;
  digitalWrite(led, HIGH);
  if(input<0) {
      digitalWrite(led, LOW);
  }
  else {
    digitalWrite(led, HIGH);
  }

}

ros::Subscriber<std_msgs::Int16> sub("toggle_led", &messageCb );

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

