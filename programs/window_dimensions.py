from screeninfo import get_monitors
import keyboard
import time

# for m in get_monitors():
#     print(m.width)
#     print(m.height)


def listen():
    while True:
        try:
            if keyboard.is_pressed('q'):
                print('You pressed q')
                return
        except:
            print('You pressed a different key, please press q')

listen()