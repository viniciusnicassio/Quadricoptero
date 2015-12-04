String ard_sends;

const int Saida1=6;

//const int time=0.1; //16M
//const float passo=0.1; //16M
const int time=20; //16k
const float passo=0.1; //16k
//const int time=85; //8k
//const float passo=0.05; //16k

float pwm;
float timeup;
float timedown;
char c;

void setup() {
  Serial.begin(9600); 
  pinMode(Saida1, OUTPUT);
  pwm=0.8;
  timeup=pwm*time;
  timedown=(1-pwm)*time;
}

void loop() {
/*  Serial.print("pwm= ");
  Serial.print(pwm);
  Serial.print("\ttimeup= ");
  Serial.print(timeup);
  Serial.print("\ttimedown= ");
  Serial.println(timedown);
  delay(100);*/
  if(Serial.available()){
    c = Serial.read();
    if(c=='w')
    {
      pwm = pwm+passo;
    }
    if(c=='s')
    {
      pwm =pwm - passo;
    }
    if(c=='p')
    {
      pwm = 0;
    }
    timeup=pwm*time;
    timedown=(1-pwm)*time;
    Serial.println(pwm);
  }
    
  if(timeup<=0){
    digitalWrite(Saida1, LOW);
  }
  if(pwm>=1){
    digitalWrite(Saida1, HIGH);
  }
  if(pwm>0 && pwm<1){
    digitalWrite(Saida1, HIGH);
    delayMicroseconds(timeup);
    digitalWrite(Saida1, LOW);
    delayMicroseconds(timedown);
  }
}
