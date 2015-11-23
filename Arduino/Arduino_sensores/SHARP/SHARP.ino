#define SHARP_FRENTE A0
#define SHARP_TRAZ A1
#define SHARP_ESQUERDA A2
#define SHARP_DIREITA A3

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
  delay(1000);
}
