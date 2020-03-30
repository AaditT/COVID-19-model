#include <Servo.h>
Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position


const int trigPin = 9; 
const int echoPin = 10;
float duration, distance; 


void setup() {
  // put your setup code here, to run once:
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  myservo.attach(8);
  myservo.write(0);
  Serial.begin(9600); 

}
void runtimer() {
  for (pos = 0; pos <= 180; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);              // tell servo to go to position in variable 'pos'
    delay(110);                       // waits 15ms for the servo to reach the position
  }
}
void servoReset() {
  myservo.write(0);
}

float getDistance() {
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2); 
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10); 
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH); 
  distance = (duration*.0343)/2;  
  Serial.println(distance);
  return distance;
}

void loop() {
  // put your main code here, to run repeatedly:
  getDistance();
  
  if (distance <= 30)
  {
    runtimer();
  }

  delay(5000);
  
  getDistance();
  if (distance > 30) {
    servoReset();
  }


}
