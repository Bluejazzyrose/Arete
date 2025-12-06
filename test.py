import keyboard

while True:
  
    print(keyboard.read_key())
    if keyboard.read_key() == "a":
        break