#pip install pythongui
import pyautogui, time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

link = "https://www.youtube.com/watch?v=so8V5dAli-Q&ab_channel=HalseyVEVO"
pyautogui.write(link)
pyautogui.press("enter")
