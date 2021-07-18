import pyautogui as pt
import pyperclip as pc
from time import sleep
from whatsapp response import response


# INSTRUCTION FOR WHATSAPP BOT
class WhatsApp:

#define whatsapp bot values

    def __init__(self, speed=.5, click_speed=.3):
            self.speed = speed
            self.click_speed = click_speed
            self.message = ""
            self.last_message = ""

    #navigate to the green dots for new messsage
            def nav_green_dot(self):
                try:
                    position = pt.locateonscreen("green dot.png", confidence=.7)
                    pt.moveTo(position[0:2], duration=self.speed)
                    pt.moveRel(-100, 0, duration=self.speed)
                    pt.doubleClick(interval=self.clickspeed)
                except Exception as e:
                    print(' Exception(nav_green_dot): ', e)


            #navigate to our message input box
            def nav_input_box(self):
                try:
                    position = pt.locateonscreen("paperclip.png", confidence=.7)
                    pt.moveTo(position[0:2], duration=self.speed)
                    pt.moveRel(100, 10, duration=self.speed)
                    pt.doubleClick(interval=self.clickspeed)
                except Exception as e:
                    print('Exception(nav_input_box): ',  e)


            #navigates to the message we want to reply
            def nav_message (self):
                try:
                    position = pt.locateonscreen("paperclip.png", confidence=.7)
                    pt.moveTo(position[0:2], duration=self.speed)
                    pt.moveRel(100, 10, duration + self.speed)
                except Exception as e:
                    print('Exception(nav_message): ', e)

            #copies the message we want to process
            def get_message(self):
                pt.tripleClick(Button.left, 3)
                sleep(self.speed)
                pt.click(Button.right, 1)
                sleep(self.speed)
                pt.moveRel(10, 10, duration=self.speed)
                pt.click(Button.left, 1)
                sleep(1)

                self.message = pc.paste()
                print('user says:', self.message)

        #SENDS MESSAGE TO THE USER
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
                    else:
                print('no new messages')

        except Exception as e:
                print('Exception (send_message':, e) )



wa_bot = WhatsApp(speed=.5,clickspeed=.4)
sleep(.2)

while True:
    wa_bot.nav_green_dot()
    wa_bot.nav_message()
    wa_bot.get_message()
    wa_bot.nav_input_box()
    wa_bot.send_message()

    sleep(.10)






