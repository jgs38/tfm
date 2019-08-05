/*
 * 
  Autor: Javier Gutierrez Solorzano

*/

int Vo;
float R1 = 100000;              // resistencia fija del divisor de tension 
float lnR2, R2, T, t;
float t1, t2, t3;
float c1 = 0.5308572593e-03, c2 = 2.396039800e-04, c3 = 0.4234340345e-07;

int RELE[]={3,5,6};

int temperatura(int A){
  Vo = analogRead(A);      // lectura del pin analogico
  R2 = R1 * (1023.0 / (float)Vo - 1.0); // conversion de tension a resistencia
  lnR2 = log(R2);
  T = (1.0 / (c1 + c2*lnR2 + c3*lnR2*lnR2*lnR2));   // ecuacion S-H
  t = T - 273.15;   // Kelvin a Celsius
  return t;
}

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);   // inicializa comunicacion serie a 9600 bps
  pinMode(RELE[0], OUTPUT);
  pinMode(RELE[1], OUTPUT);
  pinMode(RELE[2], OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int t[]={temperatura(A2),temperatura(A1),temperatura(A0)};
  
  Serial.print("Temperatura A2= ");
  Serial.println(t[0]); 
  Serial.print("Temperatura A1= ");
  Serial.println(t[1]);
  Serial.print("Temperatura A0= ");
  Serial.println(t[2]);
  Serial.println("**************************************");

  if ((t[0]<43) and (t[0]>19)){ //60
    digitalWrite(RELE[0],HIGH); // circuito cerrado
  }else{
    digitalWrite(RELE[0], LOW); // circuito abierto
  }

  if ((t[1]<43) and (t[1]>19)){
    digitalWrite(RELE[1],HIGH); 
  }else{
    digitalWrite(RELE[1], LOW); 
  }

  if ((t[2]<43) and (t[2]>19)){//55
    digitalWrite(RELE[2],HIGH); 
  }else{
    digitalWrite(RELE[2], LOW);
  }

  delay(1500);       // demora entre lecturas

  //digitalWrite(RELE[1], LOW); // circuito abierto

  //delay(300);

}

