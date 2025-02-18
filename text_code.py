import pywhatkit as kit
import time

def spam_whatsapp_message(phone_number, message, count, delay=5):
    for i in range(count):
        kit.sendwhatmsg_instantly(phone_no=phone_number, message=message, wait_time=15, tab_close=True)
        print(f"Sent {i+1} messages to {phone_number}")
        time.sleep(delay)  

# usage
phone_number = "+918574569854"  # Change to the recipient's phone number
message = "msg"
count = 15  # Number of times to send
delay = 10  # Delay in seconds between each message

spam_whatsapp_message(phone_number, message, count, delay)
############ Instructions ############
''' For this code, 
you just need to login your whatsapp web in your browser and then run the code.
 It will send the message to the given number. '''
''' It only sends plain text messages, not emojis or media files. '''