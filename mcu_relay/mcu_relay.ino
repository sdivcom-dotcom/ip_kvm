#include <RtcDS1302.h>
#include <Adafruit_BMP085.h>
ThreeWire myWire(7,6,8); // IO, SCLK, CE
RtcDS1302<ThreeWire> Rtc(myWire);
Adafruit_BMP085 bmp;
const int relay = 2;
char inputChar;
void setup() {
  // put your setup code here, to run once:
    Serial.begin(115200);
    pinMode(relay, OUTPUT);
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