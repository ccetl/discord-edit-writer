# before executing you need to run "pip install pyautogui pywin32"
# author ccetl
import random
import time

import pyautogui
import win32gui

action_delay_enabled: bool = True
action_delay_min: float = 1.0
action_delay_max: float = 3.0

line_delay_enabled: bool = True
line_delay_min: float = 1.0
line_delay_max: float = 3.0


def focused():
    window = win32gui.GetForegroundWindow()
    name = 'discord'
    return name in win32gui.GetClassName(window).lower() or name in win32gui.GetWindowText(window).lower()


def run():
    while not focused():
        time.sleep(1)

    with open('./message.txt', 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            line = lines[i].strip()
            if line:
                if i == 0:
                    pyautogui.press('enter')  # ensure the chat is selected
                    if action_delay_enabled:
                        time.sleep(random.uniform(action_delay_min, action_delay_max))
                    pyautogui.typewrite(line)
                    if action_delay_enabled:
                        time.sleep(random.uniform(action_delay_min, action_delay_max))
                    pyautogui.press('enter')
                else:
                    pyautogui.press('up')
                    if action_delay_enabled:
                        time.sleep(random.uniform(action_delay_min, action_delay_max))
                    pyautogui.hotkey('ctrl', 'a')
                    if action_delay_enabled:
                        time.sleep(random.uniform(action_delay_min, action_delay_max))
                    pyautogui.typewrite(line)
                    if action_delay_enabled:
                        time.sleep(random.uniform(action_delay_min, action_delay_max))
                    pyautogui.press('enter')

                if line_delay_enabled:
                    time.sleep(random.uniform(line_delay_min, line_delay_max))


if __name__ == '__main__':
    run()
