import keyboard
import time

count = 1
def start_ghost(count):
    current_time = time.strftime('%H:%M')
    print(f'Program last ran at {current_time} and has ran {count} times')
    keyboard.press_and_release('space')
    time.sleep(240)
    new_count = count + 1
    start_ghost(new_count)


start_ghost(count)