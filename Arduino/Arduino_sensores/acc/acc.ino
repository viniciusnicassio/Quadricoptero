#include <Wire.h>
#include <LSM303.h>

#define DIV_ACC 32768 //Referencia para 1

LSM303 compass;

float x=0;
float y=0;
float z=0;

void setup()
{
  Serial.begin(9600);
  Wire.begin();
  compass.init();
  compass.enableDefault();
}

void loop()
{
  compass.read();
  Serial.print("A ");
  Serial.print("X: ");
  Serial.print((float)compass.a.x/DIV_ACC);
  Serial.print(" Y: ");
  Serial.print((float)compass.a.y/DIV_ACC);
  Serial.print(" Z: ");
  Serial.println((float)compass.a.z/DIV_ACC);

  delay(100);
}
