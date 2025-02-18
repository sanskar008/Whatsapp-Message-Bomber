import pyautogui
import pyperclip
import time


def spam_whatsapp_gui(message, count, delay=1):
    time.sleep(5)  # Give time to switch to WhatsApp manually
    for i in range(count):
        pyperclip.copy(message)  
        pyautogui.hotkey("ctrl", "v")  
        pyautogui.press("enter")  
        print(f"Sent {i+1} messages")
        time.sleep(delay)  

# usage
message = "msg😎"  # You can copy-paste any emoji here!
count = 1  # Number of times to send
delay = 1  # Delay in seconds

spam_whatsapp_gui(message, count, delay)
############ Instructions ############
''' To use this code,
 you have to mannually open whatsapp chat (web or desktop) and then run the code. 
 It will send the message to the opened chat. '''