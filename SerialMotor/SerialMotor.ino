int motorIzqPin = 6;
int motorDerPin = 9;
int velIzq = 0;
int velDer = 0;
void setup() {
  pinMode(motorIzqPin, OUTPUT);      //se inicializa el motorizq como salida
  pinMode(motorDerPin, OUTPUT);
  Serial.begin(9600);                //se define el baud rate
}

void loop() {
int velIzq;
int velDer;
  if (Serial.available()){             //se chequea estar recibiendo por serie
    if (255 == Serial.read()) {
      digitalWrite(12, HIGH - digitalRead(12)); 
      velIzq = Serial.parseInt();     //se carga el dato recivido en la variable de velocidad
      analogWrite(motorIzqPin, velIzq);    //se setea la velocidad del motor
      //velDer = Serial.parseInt();     //se carga el dato recivido en la variable de velocidad
      //if (velIzq >= 0 && velIzq <= 255 && velDer >= 0 && velDer <= 255){   //se chequea que el dato sea valido
      //  digitalWrite(13, HIGH - digitalRead(13)); 
      //  analogWrite(motorIzqPin, velIzq);    //se setea la velocidad del motor
      //  analogWrite(motorDerPin, velDer);    //se setea la velocidad del motor
      //}
    }
  }
}
