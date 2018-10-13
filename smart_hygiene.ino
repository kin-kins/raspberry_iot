#include "DHT.h"        // including the library of DHT11 temperature and humidity sensor
#define DHTTYPE DHT11   // DHT 11

#define dht_dpin 10
DHT dht(dht_dpin, DHTTYPE); 
void setup(void)
{ 
  dht.begin();
  Serial.begin(9600);
  Serial.println("Humidity and temperature\n\n");
  delay(700);

  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  

}
void loop() 
{
  int chk=dht.read(0);
    float h = dht.readHumidity();
    int gas=analogRead(A0);
    int tap=digitalRead(8);
    if(tap==0)
    digitalWrite(3,1);
    else if (tap==1)
    digitalWrite(3,0);
    int dust=digitalRead(9);
    
    if(dust==10)
    digitalWrite(4,1);
    else if (dust==1)
    digitalWrite(4,0);
    
    Serial.println(gas);
    float t = dht.readTemperature();         
    Serial.print("Current humidity = ");
    Serial.print(h);
    Serial.print("%  ");
    Serial.print("temperature = ");
    Serial.print(t); 
    Serial.println("C  ");
   /* if(t>31)
    {
      digitalWrite( 16,HIGH);
      digitalWrite( 5,LOW);
    }
    else if(t<31)
    {
      digitalWrite( 16,LOW);
    }*/
    
    
    
  delay(800);
}
