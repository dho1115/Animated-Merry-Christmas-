import time
from colorama import init;
from termcolor import colored

init();

def blink_text(text, color, interval=0.5, times=5):
   for _ in range(times):
      print(colored(text, color), end='\r')
      time.sleep(interval)
      print(' ' * len(text), end='\r')
      time.sleep(interval)

blink_text('Blinking Text', 'red')