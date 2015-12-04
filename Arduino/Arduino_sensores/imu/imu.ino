#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>

//#define DIV_ACC 32768 //Referencia para 1

//#define DIV_GIRO 32768 //Relação de 1

#define DIV_ACC 182.044444444 //Referencia para 180

#define DIV_GIRO 182.044444444 //Relação de 180

#define MEDIA 50 // Valor aquisitado para calulo da media

//Funções
    //Acelerometro
    float AccX();
    float AccY();
    float AccZ();
    
    //Giroscopio
    float GiroX();
    float GiroY();
    float GiroZ();
    
    //Media
    void mAccX(float *media,int &i);
    void mAccY(float *media,int &i);
    void mAccZ(float *media,int &i);
    
    void mGiroX(float *media,int &i);
    void mGiroY(float *media,int &i);
    void mGiroZ(float *media,int &i);
    
    //Variaveis
    float mAccx[MEDIA+1];
    float mAccy[MEDIA+1];
    float mAccz[MEDIA+1];
    
    float mGirox[MEDIA+1];
    float mGiroy[MEDIA+1];
    float mGiroz[MEDIA+1];
    
    int iAccx=0;
    int iAccy=0;
    int iAccz=0;
    
    int iGirox=0;
    int iGiroy=0;
    int iGiroz=0;

    LSM303 compass;
    L3G gyro;

void setup() {
  delay(10000);
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
  mGiroX(mGirox,iGirox);
  Serial.print(mGirox[MEDIA]);
  Serial.print(" Y: ");
  mGiroY(mGiroy,iGiroy);
  Serial.print(mGiroy[MEDIA]);
  Serial.print(" Z: ");
  mGiroZ(mGiroz,iGiroz);
  Serial.print(mGiroz[MEDIA]);

  Serial.print(" A ");
  Serial.print("X: ");
  mAccX(mAccx,iAccx);
  Serial.print(mAccx[MEDIA]);
  Serial.print(" Y: ");
  mAccY(mAccy,iAccy);
  Serial.print(mAccy[MEDIA]);
  Serial.print(" Z: ");
  mAccZ(mAccz,iAccz);
  Serial.println(mAccz[MEDIA]);

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

void mAccX(float *media,int &i){
  if(i<=MEDIA){
    media[i]=AccX();
    i++;
  }
  else{
    i=0;
    media[i]=AccX();
  }
  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++){
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mAccY(float *media,int &i){
  if(i<=MEDIA){
    media[i]=AccY();
    i++;
  }
  else{
    i=0;
    media[i]=AccY();
  }
  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++){
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mAccZ(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i]=AccZ();
    i++;
  }
  else
  {
    i=0;
    media[i]=AccZ();
  }
  

  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }
  
  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mGiroX(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i]=GiroX();
    i++;
  }
  else
  {
    i=0;
    media[i]=GiroX();
  }
  

  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }
  
  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mGiroY(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i]=GiroY();
    i++;
  }
  else
  {
    i=0;
    media[i]=GiroY();
  }
  

  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }
  
  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mGiroZ(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i]=GiroZ();
    i++;
  }
  else
  {
    i=0;
    media[i]=GiroZ();
  }
  

  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }
  
  media[MEDIA]=media[MEDIA]/MEDIA;
}
