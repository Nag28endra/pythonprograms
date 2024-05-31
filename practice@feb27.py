import pyautogui
import time

time.sleep(2)
count =0 
while count<=500:
    pyautogui.typewrite('keerthi Code!!!')

    pyautogui.press('enter')
    count += 1