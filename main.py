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

ACTION_DELAY_ENABLED = False
ACTION_DELAY_MIN = 1
ACTION_DELAY_MAX = 3

LINE_DELAY_ENABLED = True
LINE_DELAY_MIN = 1
LINE_DELAY_MAX = 3

DELETE_MESSAGE = True


def focused():
    window = win32gui.GetForegroundWindow()
    name = 'discord'
    return name in win32gui.GetClassName(window).lower() or name in win32gui.GetWindowText(window).lower()


def delete_last_message():
    time.sleep(random.uniform(LINE_DELAY_MIN, LINE_DELAY_MAX))
    pyautogui.press('up')
    if ACTION_DELAY_ENABLED:
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
    pyautogui.hotkey('ctrl', 'a')
    if ACTION_DELAY_ENABLED:
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
    pyautogui.press('backspace')
    if ACTION_DELAY_ENABLED:
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
    if ACTION_DELAY_ENABLED:
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
    pyautogui.press('enter')
    if ACTION_DELAY_ENABLED:
        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
    pyautogui.press('enter')
    print("deleted message")


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
                    if ACTION_DELAY_ENABLED:
                        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
                    pyautogui.press('enter')
                else:
                    pyautogui.press('up')
                    if ACTION_DELAY_ENABLED:
                        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
                    pyautogui.hotkey('ctrl', 'a')
                    if ACTION_DELAY_ENABLED:
                        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
                    pyautogui.typewrite(line)
                    if ACTION_DELAY_ENABLED:
                        time.sleep(random.uniform(ACTION_DELAY_MIN, ACTION_DELAY_MAX))
                    pyautogui.press('enter')

                print("line " + str(i + 1) + "/" + str(length))

                if LINE_DELAY_ENABLED and i != length - 1:
                    time.sleep(random.uniform(LINE_DELAY_MIN, LINE_DELAY_MAX))

        if DELETE_MESSAGE:
            delete_last_message()


if __name__ == '__main__':
    run()
