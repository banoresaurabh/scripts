# This one spams people with three smilies 
from selenium import webdriver
import pyautogui
import time

i = 0
while i < 100:
	pyautogui.moveTo(461,718)
	pyautogui.click()
	pyautogui.moveTo(458,476)
	pyautogui.click()
	pyautogui.click()
	pyautogui.click()
	#pyautogui.typewrite("testing script!!")
	pyautogui.moveTo(1294,718)
	pyautogui.click()
	i += 1
	time.sleep(2);