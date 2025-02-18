from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def send_whatsapp_message(number, message, count):
    driver = webdriver.Chrome()  
    driver.get(f"https://web.whatsapp.com/send?phone={number}")  
    time.sleep(20)  

    for i in range(count):
        message_box = driver.find_element("xpath", '//div[@title="Type a message"]')  
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print(f"Sent {i+1} messages to {number}")
        time.sleep(2)

    driver.quit()  


send_whatsapp_message("+918574569854", "Automated Message!", 5)
