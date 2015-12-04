#define SHARP_FRENTE 9
#define SHARP_TRAZ 8
#define SHARP_ESQUERDA 7
#define SHARP_DIREITA 6

void setup() {
  Serial.begin(9600);
  pinMode(SHARP_FRENTE, INPUT);
  pinMode(SHARP_TRAZ, INPUT);
  pinMode(SHARP_ESQUERDA, INPUT);
  pinMode(SHARP_DIREITA, INPUT);

}

void loop() {
  Serial.print("\nSharp frente: ");
  Serial.println(analogRead(SHARP_FRENTE));
  Serial.print("Sharp traz: ");
  Serial.println(analogRead(SHARP_TRAZ));
  Serial.print("Sharp esquerda: ");
  Serial.println(analogRead(SHARP_ESQUERDA));
  Serial.print("Sharp Direita: ");
  Serial.println(analogRead(SHARP_DIREITA));
  delay(500);
}
