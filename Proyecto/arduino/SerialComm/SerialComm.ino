int incomingByte = 0;   // for incoming serial data

void setup() {
  Serial.begin(9600);     // opens serial port, sets data rate to 9600 bps
}

void loop() {
  //analogWrite(9, 180);
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.parseInt();// guarda el nuemero que envio, falta cambiar los m/s a velocidad de servo
    digitalWrite(13, HIGH - digitalRead(13));
    Serial.println(incomingByte);
    analogWrite(6, incomingByte);
  }
}
