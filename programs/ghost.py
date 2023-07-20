import mouse
import keyboard
import time
from screeninfo import get_monitors


for monitor in get_monitors():
    mouse_start_y = monitor.height/2
    mouse_start_x = monitor.width/2


# def listen():
#     input('Please press Q to exit the function')
#     start_ghost() 



def start_ghost():   
    print(f'starting the program for screen dimensions width: {mouse_start_x*2}, height: {mouse_start_y*2}')
    mouse.move(mouse_start_x, mouse_start_y, duration=1)
    # mouse.click('left')
    keyboard.press_and_release('space')
    time.sleep(5)
    mouse.move(mouse_start_x-500, mouse_start_y, duration=1)
    # mouse.click('left')
    time.sleep(5)
    start_ghost()

start_ghost()