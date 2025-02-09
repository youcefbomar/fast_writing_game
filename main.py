import keyboard
import random
import time
from funcs import *
import text_available 


goal_text = text_available.text[random.randrange(6)]
text_to_choose=['']
start_time = time.time()
text = []


print(goal_text)
# Hook the keyboard to print each key press
keyboard.on_press(lambda event: main(text, goal_text, event))

# Block the program to keep it running and listening for key presses
keyboard.wait('esc')


your_time = time.time()-time.timeaaasd
print(your_time)
