#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>

/* Initialize stepper motor pins */
const int stepper1 = 11;
const int dir1 = 10;
const int led = 13;
const int stepper2 = 7;
const int dir2 = 6;

/* Include ROS and the messages */
#include <ros.h>
#include <std_msgs/Int16.h>
#include <std_msgs/String.h>

/* default input is 3: stop mode */
int input = 3;
int sound_language = 1;
int object_name = 0;

ros::NodeHandle nh;

/* callback function used when message is receieved*/
void messageCb( const std_msgs::Int16& cmd_vel) {
  input = cmd_vel.data;   //set global variable to received value
}

/* callback function for language */
void messageCb1( const std_msgs::Int16& language) {
  sound_language = language.data;   //set global variable to received value
  mp3_play(sound_language);
}

/* callback function for soundtrack */
void messageCb2(const std_msgs::Int16& classify_image) {
  object_name = classify_image.data;
  mp3_play(sound_language-1+object_name);
}


std_msgs::String image_trigger;
/* Subscribe to /cmd_vel , publish to /capture_image */
ros::Subscriber<std_msgs::Int16> sub("/cmd_vel", &messageCb );
ros::Subscriber<std_msgs::Int16> sub1("/language", &messageCb1 );
ros::Subscriber<std_msgs::Int16> sub2("/classify_image", &messageCb2);
ros::Publisher pub("/capture_image", &image_trigger);

void setup() {
  /* Initialize MP3 Player*/
  Serial3.begin(9600);
  mp3_set_serial(Serial3);      // DFPlayer-mini mp3 module 시리얼 세팅
  delay(1);                     // 볼륨값 적용을 위한 delay
  mp3_set_volume (30);          // 볼륨조절 값 0~30

/* Initialize all pin modes */
  pinMode(stepper1, OUTPUT);
  pinMode(dir1, OUTPUT);
  pinMode(stepper2, OUTPUT);
  pinMode(dir2, OUTPUT);
  digitalWrite(dir1, LOW);
  digitalWrite(stepper1, LOW);
  digitalWrite(dir2, LOW);
  digitalWrite(stepper2, LOW);

  /* MS1 and MS2 pins on LOW for full step mode on motor driver*/
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
  digitalWrite(12, LOW);
  digitalWrite(13, LOW);

  nh.initNode();
  nh.subscribe(sub);
  nh.subscribe(sub1);
  nh.subscribe(sub2);
  nh.advertise(pub);
}

void loop() {
  /* ROS spinonce */
  nh.spinOnce();

  /*motor control for TELEOP*/

  switch (input) {
    /* Cases 1~5 are TELEOP cases, 6~9 are automatic modes*/
    //straight
    case 1: 
      gostraight();
      digitalWrite(led, HIGH);
      break;
    
    //turn left
    case 2:
      turnleft();
      digitalWrite(led, LOW);
      break;

    //stop
    case 3: 
      digitalWrite(led, LOW);
    break;
    
    //turn right
    case 4: 
      turnright();
      digitalWrite(led, LOW);
    break;
    
    //back
    case 5:
      goback();
      digitalWrite(led, HIGH);
    break;

    //object on right
    case 6:
      /* go straight then turn right*/
      for(int i = 0; i<400; i++) {
        gostraight();
      }
      for(int i = 0; i<200; i++) {
        turnright();
      }
      for(int i = 0; i<400; i++) {
        gostraight();
      }

      break;
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

/* move functions */
void turnleft() {
  onestep(false);
  onestep2(false);
}

void turnright() {
  onestep(true);
  onestep2(true);
}

void gostraight() {
  onestep(true);
  onestep2(false);
}

void goback() {
  onestep(false);
  onestep2(true);
}

/* move functions, with real life angles/distances */

void rotate(int angle) {
  /* one revolution = 200 steps*/
  if (angle <0) {
    for (int i = 0; i<angle*-1; i++) {
      turnleft();
    }
  }
  else {
    for (int i = 0; i<angle*1; i++) {
      turnright();
    }
  }
}
