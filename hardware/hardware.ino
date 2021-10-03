#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <ESP8266WebServer.h>
#include <ESP8266HTTPClient.h>

const char* ssid = "**********";
const char* password = "************";
const char *host = "wildaware-server-and-hardware.neeltron.repl.co";
const int httpsPort = 443;
const char fingerprint[] PROGMEM = "25 DE 41 40 12 C6 E3 8C 9A FD 50 CC 35 CB 03 42 7B FC DD 86";

String incomingByte;
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length() - 1;
  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}
void setup() {
  Serial.begin(9600);
  WiFi.mode(WIFI_OFF);
  delay(1000);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.println("");
  Serial.print("Connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("Connected to ");
  Serial.println(ssid);
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
}
void loop() {
  if (Serial.available() > 0) {
    incomingByte = Serial.readString();
    String name = getValue(incomingByte, ' ', 0);
    String imgLink = getValue(incomingByte, ' ', 1);
    Serial.println(name);
    WiFiClientSecure httpsClient;
    Serial.println(host);
    Serial.printf("Using fingerprint '%s'\n", fingerprint);
    httpsClient.setFingerprint(fingerprint);
    httpsClient.setTimeout(15000); // 15 Seconds
    delay(1000);

    Serial.print("HTTPS Connecting");
    int r = 0; //retry counter
    while ((!httpsClient.connect(host, httpsPort)) && (r < 30)) {
      delay(100);
      Serial.print(".");
      r++;
    }
    if (r == 30) {
      Serial.println("Connection failed");
    }
    else {
      Serial.println("Connected to web");
    }

    String getData, Link;
    name.trim();
    Link = "/input?url="+imgLink+"&aname="+name+"&loc=Jaipur&desc=lionfound";
    Link.trim();
    Serial.print("requesting URL: ");
    Serial.println(host + Link);
    httpsClient.print(String("GET ") + Link + " HTTP/1.1\r\n" +
                      "Host: " + host + "\r\n" +
                      "Connection: close\r\n\r\n");

    Serial.println("request sent");

    while (httpsClient.connected()) {
      String line = httpsClient.readStringUntil('\n');
      if (line == "\r") {
        Serial.println("received");
        break;
      }
    }

    String line;
    while (httpsClient.available()) {
      line = httpsClient.readStringUntil('\n');
      Serial.println(line);
    }
    delay(1000);
  }
}
