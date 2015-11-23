#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>

#define DIV_ACC 32768 //Referencia para 1

#define DIV_GIRO 32768 //Relação de 1

#define MEDIA 10 // Valor aquisitado para calulo da media

//Funções
    //Acelerometro
    float AccX();
    float AccY();
    float AccZ();

    //Media
    float mAccX();
    float mAccY();
    float mAccZ();

    //Giroscopio
    float GiroX();
    float GiroY();
    float GiroZ();
    
    //Media
    float mGiroX();/*
    float mGiroY();
    float mGiroZ();*/

LSM303 compass;
L3G gyro;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  if (!gyro.init())
  {
    Serial.println("Não se comunicou com a Giroscopio");
    while (1);
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
  Serial.print(GiroX());
  Serial.print(" Y: ");
  Serial.print(GiroY());
  Serial.print(" Z: ");
  Serial.print(GiroZ());

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

float GiroX(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.x/DIV_GIRO);
}

float GiroY(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.y/DIV_GIRO);
}

float GiroZ(){
  gyro.enableDefault();
  gyro.read();

  return((float)gyro.g.z/DIV_GIRO);
}

float mAccX()
{
  static float media[MEDIA+1];
  static float i=0;
  if(i<=MEDIA)
  {
    media[i]=AccX();
    i++;
  }
  else
  {
    i=0;
    media[i]=AccX();
  }

  for(int j=0, j<=MEDIA, j++)
  {
    media[MEDIA+1]+=media[j];
  }
  return(media[MEDIA+1]/MEDIA);
}

/*float mAccY(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.y/DIV_ACC);
}

float mAccZ(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.z/DIV_ACC);
}*/
