# BE CAREFUL!

from os import write # Imports
import pyautogui as pg, webbrowser as web, time as tm # Imports
web.open("https://web.whatsapp.com/send?phone=") # After the = complete with the complete number of the person
tm.sleep(5) # Timer (you must have time to open the browser and also Whatsapp Web)
for i in range (10): # X msg you wanna send
    pg.write("El poder de la IA") # Msg
    pg.press("enter") # After writing the msg, press enter to send

#x = 1
#while (x >= 1):
   # pg.write("message")
    #pg.pg.press("enter")

# With these lines of code, you can send infinites messages

# BE CAREFUL!