#include <RtcDS1302.h>
#include <Adafruit_BMP085.h>
#include <OneWire.h>
#include <DallasTemperature.h>

ThreeWire myWire(7,6,8); // IO, SCLK, CE
RtcDS1302<ThreeWire> Rtc(myWire);
Adafruit_BMP085 bmp;
const int relay = 2;
const int pin_green = 3;//green
const int pin_yellow = 4;//yellow
const int pin_red = 5;//red
#define ONE_WIRE_BUS    9
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
uint8_t deviceCount = 0;
char inputChar;

struct
{
  int id;
  DeviceAddress addr;
} T[4];

float getTempByID(int id)
{
  for (uint8_t index = 0; index < deviceCount; index++)
  {
    if (T[index].id == id)
    {
      return sensors.getTempC(T[index].addr);
    }
  }
  return -999;
}

void printAddress(DeviceAddress deviceAddress)
{
  for (uint8_t i = 0; i < 8; i++)
  {
    if (deviceAddress[i] < 16) Serial.print("0");
    Serial.print(deviceAddress[i], HEX);
  }
}


void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600);
    pinMode(relay, OUTPUT);
    pinMode(pin_green, OUTPUT);
    pinMode(pin_yellow, OUTPUT);
    pinMode(pin_red, OUTPUT);
    Rtc.Begin();

    RtcDateTime compiled = RtcDateTime(__DATE__, __TIME__);
    //printDateTime(compiled);

    if (!Rtc.IsDateTimeValid()) 
    {
        //Serial.println("RTC lost confidence in the DateTime!");
        Rtc.SetDateTime(compiled);
    }

    if (Rtc.GetIsWriteProtected())
    {
        //Serial.println("RTC was write protected, enabling writing now");
        Rtc.SetIsWriteProtected(false);
    }

    if (!Rtc.GetIsRunning())
    {
        //Serial.println("RTC was not actively running, starting now");
        Rtc.SetIsRunning(true);
    }
    
    RtcDateTime now = Rtc.GetDateTime();
    if (now < compiled) 
    {
        //Serial.println("RTC is older than compile time!  (Updating DateTime)");
        Rtc.SetDateTime(compiled);
    }

    if (!bmp.begin()) {
    Serial.println("Could not find a valid BMP085 sensor, check wiring!");
    while (1) {}
    }
    sensors.begin();
  deviceCount = sensors.getDeviceCount();
  Serial.print("#devices: ");
  Serial.println(deviceCount);
    for (uint8_t index = 0; index < deviceCount; index++)
  {
    sensors.getAddress(T[index].addr, index);
    T[index].id = sensors.getUserData(T[index].addr);
  }

  for (uint8_t index = 0; index < deviceCount; index++)
  {
    Serial.println();
    Serial.println(T[index].id);
    printAddress(T[index].addr);
    Serial.println();
  }
  Serial.println();

}

void loop() {
  if (Serial.available() > 0) {
    inputChar = Serial.read();
    if (inputChar == 'r') {
      digitalWrite(relay, HIGH);
      delay(50);
      digitalWrite(relay, LOW);
    }
    else if (inputChar == 'a') {
    Serial.print("Temperature = ");
    Serial.print(bmp.readTemperature());
    Serial.println(" *C");
    }
    else if (inputChar == 'q'){
    digitalWrite(pin_red, LOW);
    digitalWrite(pin_yellow, LOW);
    digitalWrite(pin_green, HIGH);
    }
    else if (inputChar == 'w'){
    digitalWrite(pin_red, LOW);
    digitalWrite(pin_yellow, HIGH);
    digitalWrite(pin_green, LOW);
    }
    else if (inputChar == 'e'){
    digitalWrite(pin_red, HIGH);
    digitalWrite(pin_yellow, LOW);
    digitalWrite(pin_green, LOW);
    }
    else if (inputChar == 'y'){
    digitalWrite(pin_red, LOW);
    digitalWrite(pin_yellow, LOW);
    digitalWrite(pin_green, LOW);
    }
    else if (inputChar == 'u'){
   sensors.requestTemperatures();
   Serial.println("AAAAAAAAAAAAAAAAAAAAAAAAAA");
   for (int i = 0; i < 4; i++)
   {
   Serial.print("temp:\t");
   Serial.println(sensors.getTempC(T[i].addr));  
  }
Serial.println("==========================");
    }
    else if (inputChar == 't') {
    RtcDateTime now = Rtc.GetDateTime();
    printDateTime(now);
    Serial.println();
    if (!now.IsValid())
    {
        Serial.println("RTC lost confidence in the DateTime!");
    }
    }
  } 
}

#define countof(a) (sizeof(a) / sizeof(a[0]))
void printDateTime(const RtcDateTime& dt)
{
    char datestring[26];

    snprintf_P(datestring, 
            countof(datestring),
            PSTR("%02u/%02u/%04u %02u:%02u:%02u"),
            dt.Month(),
            dt.Day(),
            dt.Year(),
            dt.Hour(),
            dt.Minute(),
            dt.Second() );
    Serial.print(datestring);
}