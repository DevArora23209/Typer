import pyautogui
import time
a=input("enter the text::") 
print("You have 10 seconds to switch to the text field...")
time.sleep(10)
text_to_type = a
pyautogui.typewrite(text_to_type, interval=0.1) 