/*
  Pico "Simon" Game
  pico_simon.ino
  Emulates "Simon" memory game
  Uses Raspberry Pi Pico
  DroneBot Workshop 2022
  https://dronebotworkshop.com
*/
 
// Define game constants and variables
 
const int MAX_LEVEL = 100;
int sequence[MAX_LEVEL];
int sound[MAX_LEVEL];
int player_sequence[MAX_LEVEL];
int level = 1;
int note = 0;
int velocity = 1000;
 
// Piezo Sounds
 
#define GRN_SOUND 261
#define RED_SOUND 293
#define YEL_SOUND 329
#define BLU_SOUND 349
#define BAD_SOUND 233
 
// LED Definitions
 
#define GRN_LED 13
#define RED_LED 12
#define YEL_LED 11
#define BLU_LED 10
 
// Pushbutton Definitions
 
#define GRN_BTN 18
#define RED_BTN 19
#define YEL_BTN 20
#define BLU_BTN 21
 
// Piezo Buzzer
#define PIEZO 3
 
void setup() {
 
  // LEDs are Outputs
  pinMode(GRN_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);
  pinMode(YEL_LED, OUTPUT);
  pinMode(BLU_LED, OUTPUT);
 
  // Pushbuttons are Inputs with internal pullup resistors
  pinMode(GRN_BTN, INPUT_PULLUP);
  pinMode(RED_BTN, INPUT_PULLUP);
  pinMode(YEL_BTN, INPUT_PULLUP);
  pinMode(BLU_BTN, INPUT_PULLUP);
 
  // Buzzer is an Output
  pinMode(PIEZO, OUTPUT);
 
}
 
void loop() {
 
  if (level == 1) {
    generate_sequence();
 
    // Flash the LEDs in sequence
    for (int i = GRN_LED; i >= BLU_LED; i--) {
      digitalWrite(i, HIGH);
      delay(100);
      digitalWrite(i, LOW);
    }
  }
 
  // Start game with Green button
  if (digitalRead(GRN_BTN) == LOW || level != 1) {
    delay(1000);
    show_sequence();
    get_sequence();
  }
 
}
 
 
void generate_sequence() {
 
  // Generates random sequence
 
  // Seed for true random number
  randomSeed(millis());
 
  for (int i = 0; i < MAX_LEVEL; i++) {
 
    // Random values will match LED output pins
    sequence[i] = random(BLU_LED, (GRN_LED + 1));
 
    switch (sequence[i]) {
      case BLU_LED:
        note = BLU_SOUND;
        break;
      case YEL_LED:
        note = YEL_SOUND;
        break;
      case RED_LED:
        note = RED_SOUND;
        break;
      case GRN_LED:
        note = GRN_SOUND;
        break;
    }
 
    // Sound will match LED output
    sound[i] = note;
 
  }
}
 
void show_sequence() {
 
  // Turn off all LEDs
  digitalWrite(GRN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(YEL_LED, LOW);
  digitalWrite(BLU_LED, LOW);
 
  Serial.print("level = ");
  Serial.println(level);
 
  for (int i = 0; i < level; i++) {
    digitalWrite(sequence[i], HIGH);
    tone(PIEZO, sound[i]);
    delay(velocity);
    digitalWrite(sequence[i], LOW);
    noTone(PIEZO);
    delay(200);
  }
}
 
void get_sequence() {
  // Get sequence user enters
 
  // Flag used if user pressed a button
  int flag = 0;
 
  for (int i = 0; i < level; i++) {
 
    // Reset flag
    flag = 0;
 
    while (flag == 0) {
 
      // Check Green
      if (digitalRead(GRN_BTN) == LOW) {
        digitalWrite(GRN_LED, HIGH);
        tone(PIEZO, GRN_SOUND);
        delay(velocity);
        noTone(PIEZO);
        player_sequence[i] = GRN_LED;
        flag = 1;
        delay(200);
 
        // See if selection is incorrect
        if (player_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(GRN_LED, LOW);
      }
 
 
      // Check Red
      if (digitalRead(RED_BTN) == LOW) {
        digitalWrite(RED_LED, HIGH);
        tone(PIEZO, RED_SOUND);
        delay(velocity);
        noTone(PIEZO);
        player_sequence[i] = RED_LED;
        flag = 1;
        delay(200);
 
        // See if selection is incorrect
        if (player_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(RED_LED, LOW);
      }
 
 
      // Check Yellow
      if (digitalRead(YEL_BTN) == LOW) {
        digitalWrite(YEL_LED, HIGH);
        tone(PIEZO, YEL_SOUND);
        delay(velocity);
        noTone(PIEZO);
        player_sequence[i] = YEL_LED;
        flag = 1;
        delay(200);
 
        // See if selection is incorrect
        if (player_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(YEL_LED, LOW);
      }
 
 
      // Check Blue
      if (digitalRead(BLU_BTN) == LOW) {
        digitalWrite(BLU_LED, HIGH);
        tone(PIEZO, BLU_SOUND);
        delay(velocity);
        noTone(PIEZO);
        player_sequence[i] = BLU_LED;
        flag = 1;
        delay(200);
 
        // See if selection is incorrect
        if (player_sequence[i] != sequence[i]) {
          wrong_sequence();
          return;
        }
        digitalWrite(BLU_LED, LOW);
      }
    }
  }
  // Selection is correct
  right_sequence();
}
 
void right_sequence() {
 
  // Sequence was correct
 
  // Turn off all LEDs
  digitalWrite(GRN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(YEL_LED, LOW);
  digitalWrite(BLU_LED, LOW);
  delay(250);
 
  // Turn on all LEDs
  digitalWrite(GRN_LED, HIGH);
  digitalWrite(RED_LED, HIGH);
  digitalWrite(YEL_LED, HIGH);
  digitalWrite(BLU_LED, HIGH);
  delay(500);
 
  // Turn off all LEDs
  digitalWrite(GRN_LED, LOW);
  digitalWrite(RED_LED, LOW);
  digitalWrite(YEL_LED, LOW);
  digitalWrite(BLU_LED, LOW);
  delay(500);
 
  // Increase difficulty
  if (level < MAX_LEVEL) {
    level++;
  }
  velocity -= 50;
}
 
void wrong_sequence() {
 
  // Sequence was incorrect
  for (int i = 0; i < 3; i++) {
    // Turn on all LEDs
    digitalWrite(GRN_LED, HIGH);
    digitalWrite(RED_LED, HIGH);
    digitalWrite(YEL_LED, HIGH);
    digitalWrite(BLU_LED, HIGH);
    tone(PIEZO, BAD_SOUND);
    delay(250);
 
    // Turn off all LEDs
    digitalWrite(GRN_LED, LOW);
    digitalWrite(RED_LED, LOW);
    digitalWrite(YEL_LED, LOW);
    digitalWrite(BLU_LED, LOW);
    noTone(PIEZO);
    delay(250);
  }
  // Reset difficulty
  level = 1;
  velocity = 1000;
}