# before executing you need to run "pip install pyautogui pywin32"
# author ccetl
import random
import time

import pyautogui
import win32gui

# If you should encounter issues
# such as the wrong message gets
# edited, or it does other weird
# things, like selecting other
# fields and your ping to discord
# is high, consider adjusting
# the delays to a value which is
# suitable for your ping.

action_delay_enabled = True
action_delay_min = 1
action_delay_max = 3

line_delay_enabled = True
line_delay_min = 1
line_delay_max = 3

delete_message = False


def focused():
    window = win32gui.GetForegroundWindow()
    name = 'discord'
    return name in win32gui.GetClassName(window).lower() or name in win32gui.GetWindowText(window).lower()


def run():
    while not focused():
        time.sleep(1)

    with open('./message.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        length = len(lines)
        for i in range(length):
            line = lines[i].strip()
            if line:
                if i == 0:
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

                print("line " + str(i + 1) + "/" + str(length))

                if line_delay_enabled and i != length - 1:
                    time.sleep(random.uniform(line_delay_min, line_delay_max))

        if delete_message:
            time.sleep(random.uniform(line_delay_min, line_delay_max))
            pyautogui.press('up')
            if action_delay_enabled:
                time.sleep(random.uniform(action_delay_min, action_delay_max))
            pyautogui.hotkey('ctrl', 'a')
            if action_delay_enabled:
                time.sleep(random.uniform(action_delay_min, action_delay_max))
            pyautogui.press('backspace')
            if action_delay_enabled:
                time.sleep(random.uniform(action_delay_min, action_delay_max))
            if action_delay_enabled:
                time.sleep(random.uniform(action_delay_min, action_delay_max))
            pyautogui.press('enter')
            if action_delay_enabled:
                time.sleep(random.uniform(action_delay_min, action_delay_max))
            pyautogui.press('enter')
            print("deleted message")


if __name__ == '__main__':
    run()
