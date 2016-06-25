int motorIzqPin = 6;
int motorDerPin = 9;
int velIzq = 0;
int velDer = 0;
void setup() {
  pinMode(motorIzqPin, OUTPUT);      //se inicializa el motorizq como salida
  pinMode(motorDerPin, OUTPUT);
  Serial.begin(9600);                //se define el baud rate
  while (! Serial);                  //espera hasta registrar coneccion serie
}

void loop() {
  if (Serial.available()){             //se chequea estar recibiendo por serie
    if(255 == Serial.read()){
      int velIzq = Serial.parseInt();     //se carga el dato recivido en la variable de velocidad
      int velDer = Serial.parseInt();     //se carga el dato recivido en la variable de velocidad
      if (velIzq >= 0 && velIzq <= 255 && velDer >= 0 && velDer <= 255){   //se chequea que el dato sea valido
        analogWrite(motorIzqPin, velIzq);    //se setea la velocidad del motor
        analogWrite(motorDerPin, velDer);    //se setea la velocidad del motor
      }
    }
  }
}
