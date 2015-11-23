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
  while(!Serial.available()) {}
  
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
  
  if (readString == "a")
  {
    ard_sends = "Mandou a";
  }
  if (readString == "g")
  {
    ard_sends = "Mandou g";
  }
  if (readString != "a" && readString != "g")
  {
    ard_sends = "Comando Invalido";
  }
  
  Serial.print(ard_sends);
}
