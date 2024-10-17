#include <MeMegaPi.h>

// Create motor objects
MeMegaPiDCMotor motor1(PORT1B); 
MeMegaPiDCMotor motor2(PORT2B); 
MeMegaPiDCMotor motor3(PORT3B); 
MeMegaPiDCMotor gripperMotor(PORT1A); 

MeUltrasonicSensor ultrasonic(PORT7); 

float distance = 0;

void setup() {
  Serial.begin(9600);
  motor1.stop();
  motor2.stop();
  motor3.stop();
  gripperMotor.stop();
}

void loop() {
  distance = ultrasonic.distanceCm();
  Serial.print("Distance: ");
  Serial.println(distance);

  if (distance > 50) {
    motor1.run(-100);  
    motor2.run(100); 
  } 
  else if (distance > 20 && distance <= 50) {
    motor1.run(50);
    motor2.run(50);   
  } 
  else if (distance <= 20) {
    motor1.stop();
    motor2.stop();

 
    motor3.run(100);
    delay(500);
    gripperMotor.run(-100);
    delay(1500);             
    gripperMotor.stop(); 
    delay(2000);
    gripperMotor.run(100);
    delay(1500);  
    motor3.run(-100);
    delay(500);
    motor3.stop();
    delay(2000);
    
  }

  delay(100); 
