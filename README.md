# WHATSAPP_BOT
<br>
<br>
<br>


[![Python 3.9](https://www.python.org/static/community_logos/python-logo-generic.svg)

[![PyPI version](https://badge.fury.io/py/WHATSAPP_BOT.svg)](https://badge.fury.io/py/WHATSAPP_BOT)
![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)
![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)
![License](https://img.shields.io/badge/license-GPLv3-blue.svg)

A Python bot that automates several actions on Whatsapp, such as replying to messages and downloading of voice notes.

## Disclaimer

I hold no liability for what you do with this bot or what happens to you by using this bot.

## Dependencies

Install the following packages  using `pip`:
  ``` 
 
  pip install pyautogui 
  pip install opencv  
  pip install pyperclip
  ```

Import the following file and library:

  ```
  from pynput.mouse import Controller, Button 
  from time import sleep 
  from whatsapp_response import response 
  ```
    
 You will need to open whatsapp web desktop application 
 
 # Configuration
 
 Create a class called:
 ```
 class WhatsApp:
 ```
 Define a function that navitages the cursor to green  dot(Whatsapp message) to click on new
 message.
 Use `pyautogui as pt` to automate process.
 
 
  ```
      def nav_green_dot(self):
            try:
                position = pt.locateOnScreen("green dot.png", confidence=.7)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(-100, 0, duration=self.speed)
                pt.doubleClick(interval=self.click_speed)
            except Exception as e:
                    print(' Exception(nav_green_dot): ', e)
 ```  
 <br>
 <br>
 <br>
Second function navigates to the message input box using `pt`and :


``` 
     def nav_input_box(self):
            try:
                position = pt.locateOnScreen("paperclip.png", confidence=.7)
                pt.moveTo(position[0:2], duration=self.speed)
                pt.moveRel(100, 40, duration=self.speed)
                pt.doubleClick(interval=self.click_speed)
            except Exception as e:
                print('Exception(nav_input_box): ',  e)
```     
<br>
<br>
<br>
Import python file containig replies and process message to get reply 

```

from whatsapp_response import response

def send_message(self):
            try:
                    #CHECKS WHETHER LAST MESSAGE WAS THE SAME
                if self.message != self.last_message:
                    bot_response = response(self.message)
                    print ('you say', bot_response)
                    pt.typewrite(bot_response, interval= .1 )
                      #pt.typewriter(\n)

                        #ASSIGNS THE LAST MESSAGE
                    self.last_message = self.message
```
The send_message function first checks whether bothas made response if != True imports message
from whatsapp_response file


   
