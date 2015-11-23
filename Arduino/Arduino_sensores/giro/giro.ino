#include <Wire.h>
#include <L3G.h>

#define DIV_Giro 32768 //Relação de 1

L3G gyro;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  if (!gyro.init())
  {
    Serial.println("Failed to autodetect gyro type!");
    while (1);
  }

  gyro.enableDefault();
}

void loop() {
  gyro.read();

  Serial.print("G ");
  Serial.print("X: ");
  Serial.print((float)gyro.g.x/DIV_Giro);
  Serial.print(" Y: ");
  Serial.print((float)gyro.g.y/DIV_Giro);
  Serial.print(" Z: ");
  Serial.println((float)gyro.g.z/DIV_Giro);

  delay(100);
}
