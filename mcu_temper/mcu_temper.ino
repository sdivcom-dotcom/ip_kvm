#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS      2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

uint8_t deviceCount = 0;

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

void setup(void)
{
  Serial.begin(115200);
  Serial.println(__FILE__);
  Serial.println("Dallas Temperature Demo");
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

void loop(void)
{
  sensors.requestTemperatures();
Serial.println("AAAAAAAAAAAAAAAAAAAAAAAAAA");
  for (int i = 0; i < 4; i++)
  {
    Serial.print("temp:\t");
    Serial.println(sensors.getTempC(T[i].addr));
    
  }
Serial.println("==========================");
  delay(10000);
}

// END OF FILE