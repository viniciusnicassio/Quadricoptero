#include <Wire.h>
#include <L3G.h>
#include <LSM303.h>

//#define DIV_ACC 32768 //Referencia para 1

//#define DIV_GIRO 32768 //Relação de 1

#define DIV_ACC 182.044444444 //Referencia para 180

#define DIV_GIRO 182.044444444 //Relação de 180

#define MEDIA 30 // Valor aquisitado para calulo da media

#define SHARP_FRENTE 9 //Porta referente ao sharp da frente
#define SHARP_ESQ 8 //Porta referente ao sharp de traz
#define SHARP_TRAZ 7 //Porta referente ao sharp da esquerda
#define SHARP_DIR 6 //Porta referente ao sharp da direta

#define PIR_FRENTE 10 //Porta referente ao PIR da frente
#define PIR_ESQ 16 //Porta referente ao PIR de traz
#define PIR_TRAZ 14 //Porta referente ao PIR da esquerda
#define PIR_DIR 15 //Porta referente ao PIR da direta

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

void mSharpFrente(float *media,int &i);
void mSharpTraz(float *media,int &i);
void mSharpEsq(float *media,int &i);
void mSharpDir(float *media,int &i);

//Variaveis
float sharpfrente[MEDIA+1];
float sharptraz[MEDIA+1];
float sharpesq[MEDIA+1];
float sharpdir[MEDIA+1];

float maccx[MEDIA+1];
float maccy[MEDIA+1];
float maccz[MEDIA+1];

float mgirox[MEDIA+1];
float mgiroy[MEDIA+1];
float mgiroz[MEDIA+1];


int isharpfrente=0;
int isharptraz=0;
int isharpesq=0;
int isharpdir=0;

int iaccx=0;
int iaccy=0;
int iaccz=0;

int igirox=0;
int igiroy=0;
int igiroz=0;

float ax_zero=0;
float ay_zero=0;
float az_zero=0;

float gx_zero=0;
float gy_zero=0;
float gz_zero=0;

String ard_sends_f;
String readstring;
float ard_sends;
char c;

LSM303 compass; //acelerometro
L3G gyro; //giroscopio


void setup()
{
  Serial.begin(115200);  // initialize serial communications at 115200 bp
  Serial.flush();
  Wire.begin(); //IMU

  //Iniciando Sharp's
  pinMode(SHARP_FRENTE, INPUT);
  pinMode(SHARP_TRAZ, INPUT);
  pinMode(SHARP_ESQ, INPUT);
  pinMode(SHARP_DIR, INPUT);
  
  //Iniciando PIR's
  pinMode(PIR_FRENTE, INPUT);
  pinMode(PIR_TRAZ, INPUT);
  pinMode(PIR_ESQ, INPUT);
  pinMode(PIR_DIR, INPUT);

  if (!gyro.init())
  {
    Serial.println("Não se comunicou com a Giroscopio");
    while (1);
  }


  if (!compass.init())
  {
    Serial.println("Não se comunicou com a Acelerometro");
    while (1);
  }
}

void loop()
{
  readstring = ""; 
  while(!Serial.available()){//Atualiza a media enquanto aguarda ordem
    //Media acelerometro
    mAccX(maccx,iaccx);
    mAccY(maccy,iaccy);
    mAccZ(maccz,iaccz);

    // Media giroscopio
    mGiroX(mgirox,igirox);
    mGiroY(mgiroy,igiroy);
    mGiroZ(mgiroz,igiroz);
    
    // Media Sharp
    mSharpFrente(sharpfrente, isharpfrente);
    mSharpTraz(sharptraz, isharptraz);
    mSharpEsq(sharpesq, isharpesq);
    mSharpDir(sharpdir, isharpdir);
    
  }
  Serial.flush();  
  while (Serial.available())
  {
    if (Serial.available() > 0)
    {
      c = Serial.read();  //gets one byte from serial buffer
      readstring += c; //makes the string readString
    }
  }
  ard_sends=-999;
  if (readstring=="ax")
    ard_sends=maccx[MEDIA]-ax_zero;
  else if (readstring=="ay")
    ard_sends=maccy[MEDIA]-ay_zero;
  else if (readstring=="az")
    ard_sends=maccz[MEDIA]-az_zero;

  else if (readstring=="gx")
    ard_sends=mgirox[MEDIA]-gx_zero;
  else if (readstring=="gy")
    ard_sends=mgiroy[MEDIA]-gy_zero;
  else if (readstring=="gz")
    ard_sends=mgiroz[MEDIA]-gz_zero;
    
  else if (readstring=="sf")
    ard_sends=sharpfrente[MEDIA];
  else if (readstring=="st")
    ard_sends=sharptraz[MEDIA];
  else if (readstring=="se")
    ard_sends=sharpesq[MEDIA];
  else if (readstring=="sd")
    ard_sends=sharpdir[MEDIA];
    
  else if (readstring=="pf")
    ard_sends=digitalRead(PIR_FRENTE);
  else if (readstring=="pt")
    ard_sends=digitalRead(PIR_TRAZ);
  else if (readstring=="pe")
    ard_sends=digitalRead(PIR_ESQ);
  else if (readstring=="pd")
    ard_sends=digitalRead(PIR_DIR);
    
  else if (readstring=="z"){
    ax_zero=maccx[MEDIA];
    ay_zero=maccy[MEDIA];
    az_zero=maccz[MEDIA];
    
    gx_zero=mgirox[MEDIA];
    gy_zero=mgiroy[MEDIA];
    gz_zero=mgiroz[MEDIA];
  }
  Serial.print(ard_sends);
  
}


// Funçoes
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

float AccX(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.x/DIV_ACC);
}

float AccY(){
  compass.enableDefault();
  compass.read();

  return((float)-compass.a.y/DIV_ACC);
}

float AccZ(){
  compass.enableDefault();
  compass.read();

  return((float)compass.a.z/DIV_ACC);
}

//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
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
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
void mSharpFrente(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i] = 9462/(analogRead(SHARP_FRENTE) - 16.92);
    i++;
  }
  else
  {
    i=0;
    media[i] = 9462/(analogRead(SHARP_FRENTE) - 16.92);
  }


  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mSharpTraz(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i] = 9462/(analogRead(SHARP_TRAZ) - 16.92);
    i++;
  }
  else
  {
    i=0;
    media[i] = 9462/(analogRead(SHARP_TRAZ) - 16.92);
  }


  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mSharpEsq(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i] = 9462/(analogRead(SHARP_ESQ) - 16.92);
    i++;
  }
  else
  {
    i=0;
    media[i] = 9462/(analogRead(SHARP_ESQ) - 16.92);
  }


  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}

void mSharpDir(float *media,int &i)
{
  if(i<=MEDIA)
  {
    media[i] = 9462/(analogRead(SHARP_DIR) - 16.92);
    i++;
  }
  else
  {
    i=0;
    media[i] = 9462/(analogRead(SHARP_DIR) - 16.92);
  }


  media[MEDIA]=0;
  for(int j=0; j<=MEDIA-1; j++)
  {
    media[MEDIA]+=media[j];
  }

  media[MEDIA]=media[MEDIA]/MEDIA;
}
