import time
from colorama import init;
from termcolor import colored;

def MerryChristmas_v1(delay:float=0.75, repeat:int=3):
   init()
   try:
      delay = float(delay);
      repeat = int(repeat);

      for i in range(repeat):
         print(colored("     MERRY", color='red', attrs=['bold']), end="\r");
         time.sleep(1.5);
         print(colored(' '*len('     MERRY'), color='black', attrs=['bold']), end='\r') #creates a string of black spaces that OVERLAPS 'Merry'.
         time.sleep(0);
         print(colored("     CHRISTMAS!!!", color='green', attrs=['bold']), end="\r");
         time.sleep(1.5);
         print(colored(' '*len('     CHRISTMAS!!!'), color='black', attrs=['bold']), end='\r'); #creates a string of black spaces that OVERLAPS 'Christmas'.

      return f"{colored('Loop has ended... hope you had fun!!!')}\nPlease contact me at merrychristmas@merrychristmas.com for more holiday messages!!!\nThat is a fake email address, but the way."
  
   except ValueError:
      print(ValueError);

      return f"Sorry, but you must enter a valid number for delay and repeat. You entered {delay} for delay and {repeat} for repeat!!!"
   
def MerryChristmas_v2(delay:float=0.3):
   init()
   phrase = colored("   Merry Christmas", color='red', attrs=['bold'])
   try:
      delay = float(delay);
      greeting = "";

      for i in phrase:
         greeting+=i;
         print(greeting, end='\r');
         time.sleep(delay)

      
      return f"{colored('Loop has ended... hope you had fun!!!')}\nPlease contact me at merrychristmas@merrychristmas.com for more holiday messages!!!\nThat is a fake email address, but the way."
   
   except ValueError:
      print(ValueError);
      return f"Sorry... delay and repeat MUST be numbers. You have {delay}."

def MerryChristmas_v3():
   import pyfiglet;
   init()
   try:
      #fonts = 'block', 'broadway', 'hollywood'
      merry = pyfiglet.figlet_format("Merry ");
      christmas = pyfiglet.figlet_format("Christmas!!!");
      colorMerry = colored(merry, color='red', attrs=['bold'])
      colorChristmas = colored(christmas, color='green', attrs=['bold'])

      return colorMerry + colorChristmas;
   except Exception:
      print(Exception);
      return "Something went wrong."

def MerryChristmas_v4(delay=0.57, repeat=5):
   init()
   text = "   Merry Christmas"
   coloredText = colored(text, color='red', attrs=['bold'])
   try:
      delay, repeat=float(delay), int(repeat);
      for i in range(repeat):
         print(coloredText, end="\r");
         time.sleep(delay);
         print(" "*len(text), end="\r");
         time.sleep(delay);
      return "All done!!! HAPPY HOLIDAYS!!! If you like to see more, please email this fake email address at holidaygreetings@holidaygreetings.com!!!"
   except Exception:
      print(Exception);
      return "Sorry... there is an exception."
