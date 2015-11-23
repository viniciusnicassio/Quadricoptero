#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>

#define DIV_ACC 32768 //Referencia para 1

#define DIV_Giro 32768 //Referencia de 1

//Funções
//Acelerometro
float AccX();
float AccY();
float AccZ();
//Giroscopio
float giroX();
float giroY();
float giroZ();

LSM303 compass;
L3G gyro;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  if (!gyro.init())
  {
    Serial.println("Não se comunicou com a giroscopio");
  }


  if (!compass.init())
  {
    Serial.println("Não se comunicou com a acelerometro");
    while (1);
  }


}

void loop() {
  Serial.print("G ");
  Serial.print("X: ");
  Serial.print(giroX());
  Serial.print(" Y: ");
  Serial.print(giroY());
  Serial.print(" Z: ");
  Serial.print(giroZ());

  Serial.print(" A ");
  Serial.print("X: ");
  Serial.print(AccX());
  Serial.print(" Y: ");
  Serial.print(AccY());
  Serial.print(" Z: ");
  Serial.println(AccZ());

  delay(100);
}

float AccX(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.x/DIV_ACC);
}

float AccY(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.y/DIV_ACC);
}

float AccZ(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.z/DIV_ACC);
}

float giroX(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.x/DIV_Giro);
}

float giroY(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.y/DIV_Giro);
}

float giroZ(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.z/DIV_Giro);
}
