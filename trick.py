import pyautogui as pg
import time

print('starting in 5 seconds')
time.sleep(5)

for i in range(200):
    pg.write("Mahanati Actor garu")
    pg.press("Enter")