#define PIR_FRENTE 9
#define PIR_TRAZ 8
#define PIR_ESQUERDA 7
#define PIR_DIREITA 6

void setup() {
  Serial.begin(9600);
  pinMode(PIR_FRENTE, INPUT);
  pinMode(PIR_TRAZ, INPUT);
  pinMode(PIR_ESQUERDA, INPUT);
  pinMode(PIR_DIREITA, INPUT);

}

void loop() {
  Serial.print("\nPir frente: ");
  Serial.println(digitalRead(PIR_FRENTE));
  Serial.print("Pir traz: ");
  Serial.println(digitalRead(PIR_TRAZ));
  Serial.print("Pir esquerda: ");
  Serial.println(digitalRead(PIR_ESQUERDA));
  Serial.print("Pir Direita: ");
  Serial.println(digitalRead(PIR_DIREITA));
  delay(1000);
}
