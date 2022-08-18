import time

import win32gui

import win32api

import win32con

time.sleep(3)

ps = win32api.GetCursorPos()

print(ps)