#include <IRremote.h>

#define IR_RECEIVE_PIN 11

#define IR_BUTTON_1 12
#define IR_BUTTON_2 24
#define IR_BUTTON_3 94
#define IR_BUTTON_NEXT 67
#define IR_BUTTON_LAST 68
#define IR_BUTTON_PLAY_PAUSE 64
#define IR_BUTTON_VOL_UP 70
#define IR_BUTTON_VOL_DOWN 21

void setup() {
  Serial.begin(9600);
  IrReceiver.begin(IR_RECEIVE_PIN);
}
void loop() {
  if (IrReceiver.decode()) {
    IrReceiver.resume();

    
    //Serial.println(IrReceiver.decodedIRData.command);

    int command = IrReceiver.decodedIRData.command;
    
    switch (command) {
      case IR_BUTTON_1: {
        Serial.println("Pressed on button 1");
        break;
      }
      case IR_BUTTON_2: {
        Serial.println("Pressed on button 2");
        break;
      }
      case IR_BUTTON_3: {
        Serial.println("Pressed on button 3");
        break;
      }
      case IR_BUTTON_PLAY_PAUSE: {
        Serial.println("Pressed on button play/pause");
        break;
      }
      case IR_BUTTON_NEXT: {
        Serial.println("Pressed on next song button");
        break;
      }
      case IR_BUTTON_VOL_UP: {
        Serial.println("Pressed on volume up button");
        break;
      }
      case IR_BUTTON_LAST: {
        Serial.println("Pressed on last song button");
        break;
      }
      case IR_BUTTON_VOL_DOWN: {
        Serial.println("Pressed on volume down button");
        break;
      }
      default: {
        Serial.println(command);
      }
    }
  }
}
