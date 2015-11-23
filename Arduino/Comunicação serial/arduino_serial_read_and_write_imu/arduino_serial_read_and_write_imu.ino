String readString;
String ard_sends;
char c;

void setup()
{
  Serial.begin(9600);  // initialize serial communications at 9600 bp
}

void loop()
{
  //Esperando
  readString = ""; 
  while(!Serial.available())
  {
    //Atualiza aqui a media
  }
  
  //Lendo
  while (Serial.available())
  {
    if (Serial.available() > 0)
    {
      c = Serial.read();  //gets one byte from serial buffer
      readString += c; //makes the string readString
    }
  }
  
  //Enviando  
  if (readString == "ax"){
    ard_sends = "Mandou ax";
  }
  else{
    ard_sends = "Comando Invalido";
  }
  
  if (readString == "ay"){
    ard_sends = "Mandou ay";
  }
  
  if (readString == "az"){
    ard_sends = "Mandou az";
  }
  
  if (readString == "gx"){
    ard_sends = "Mandou gx";
  }
  
  if (readString == "gy"){
    ard_sends = "Mandou gy";
  }
  
  if (readString == "gz"){
    ard_sends = "Mandou gz";
  }
  
  if (readString == "pf"){
    ard_sends = "Mandou pf";
  }
  
  if (readString == "pt"){
    ard_sends = "Mandou pt";
  }
  
  if (readString == "pe"){
    ard_sends = "Mandou pe";
  }
  
  if (readString == "pd"){
    ard_sends = "Mandou pd";
  }
  
  if (readString == "sf"){
    ard_sends = "Mandou sf";
  }
  
  if (readString == "st"){
    ard_sends = "Mandou st";
  }
  
  if (readString == "se"){
    ard_sends = "Mandou se";
  }
  
  if (readString == "sd"){
    ard_sends = "Mandou sd";
  }
  
  Serial.print(ard_sends);
}
