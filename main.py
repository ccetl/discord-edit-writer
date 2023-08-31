# before executing you need to run "pip install pyautogui pywin32 keyboard PyQt5"
# author ccetl
import random
import sys
# import threading
import time

import pyautogui
import win32gui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QTextEdit, QFormLayout, QCheckBox, QSlider, QProgressBar, \
    QPushButton, QApplication, QMainWindow


# If you should encounter issues
# such as the wrong message gets
# edited, or it does other weird
# things, like selecting other
# fields and your ping to discord
# is high, consider adjusting
# the delays to a value which is
# suitable for your ping.


def focused():
    foreground_window = win32gui.GetForegroundWindow()
    name = 'discord'
    return name in win32gui.GetClassName(foreground_window).lower() or name in win32gui.GetWindowText(
        foreground_window).lower()


def delete_last_message(line_delay_enabled, line_delay_min, line_delay_max, action_delay_enabled, action_delay_min,
                        action_delay_max):
    if line_delay_enabled:
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


class DiscordMessageSenderApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.sending_thread = None
        self.running = False
        self.line_delay_min_value_label = None
        self.line_delay_max_value_label = None
        self.action_delay_max_value_label = None
        self.action_delay_min_value_label = None
        self.loading_bar = None
        self.start_button = None
        self.delete_message = None
        self.action_delay_max = None
        self.action_delay_min = None
        self.action_delay_enabled = None
        self.line_delay_max = None
        self.line_delay_min = None
        self.line_delay_enabled = None
        self.message_input = None
        self.setWindowTitle("Dlsc0rd Edit Writer")
        self.setGeometry(100, 100, 500, 500)

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        label = QLabel("Message:", self)
        layout.addWidget(label)

        self.message_input = QTextEdit(self)
        self.message_input.setFixedHeight(150)
        layout.addWidget(self.message_input)

        line_delay_frame = QWidget(self)
        line_delay_layout = QFormLayout()

        self.line_delay_enabled = QCheckBox("Line Delay")
        self.line_delay_enabled.setChecked(True)
        line_delay_layout.addRow(self.line_delay_enabled)

        self.line_delay_min = QSlider()
        self.line_delay_min.setOrientation(1)
        self.line_delay_max = QSlider()
        self.line_delay_max.setOrientation(1)

        self.line_delay_min_value_label = QLabel("0")
        self.line_delay_max_value_label = QLabel("0")

        self.line_delay_min.valueChanged.connect(self.update_line_delay_min_label)
        self.line_delay_max.valueChanged.connect(self.update_line_delay_max_label)

        self.line_delay_max.setValue(3)
        self.line_delay_max.setSingleStep(1)
        self.line_delay_max.setRange(0, 10)
        self.line_delay_min.setValue(1)
        self.line_delay_min.setSingleStep(1)
        self.line_delay_min.setRange(0, 10)

        line_delay_layout.addRow("Min:  ", self.line_delay_min_value_label)
        line_delay_layout.addRow(self.line_delay_min)
        line_delay_layout.addRow("Max:", self.line_delay_max_value_label)
        line_delay_layout.addRow(self.line_delay_max)

        line_delay_frame.setLayout(line_delay_layout)
        layout.addWidget(line_delay_frame)

        action_delay_frame = QWidget(self)
        action_delay_layout = QFormLayout()

        self.action_delay_enabled = QCheckBox("Action Delay")
        self.action_delay_enabled.setChecked(False)
        action_delay_layout.addRow(self.action_delay_enabled)

        self.action_delay_min = QSlider()
        self.action_delay_min.setOrientation(1)
        self.action_delay_max = QSlider()
        self.action_delay_max.setOrientation(1)

        self.action_delay_min_value_label = QLabel("0")
        self.action_delay_max_value_label = QLabel("0")

        self.action_delay_min.valueChanged.connect(self.update_action_delay_min_label)
        self.action_delay_max.valueChanged.connect(self.update_action_delay_max_label)

        self.action_delay_max.setValue(3)
        self.action_delay_max.setSingleStep(1)
        self.action_delay_max.setRange(0, 10)
        self.action_delay_min.setValue(1)
        self.action_delay_min.setSingleStep(1)
        self.action_delay_min.setRange(0, 10)

        action_delay_layout.addRow("Min:", self.action_delay_min_value_label)
        action_delay_layout.addRow(self.action_delay_min)
        action_delay_layout.addRow("Max:", self.action_delay_max_value_label)
        action_delay_layout.addRow(self.action_delay_max)

        action_delay_frame.setLayout(action_delay_layout)
        layout.addWidget(action_delay_frame)

        self.delete_message = QCheckBox("Delete Message")
        self.delete_message.setChecked(True)
        layout.addWidget(self.delete_message)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.toggle_sending)
        layout.addWidget(self.start_button)

        self.loading_bar = QProgressBar()
        layout.addWidget(self.loading_bar)

        central_widget.setLayout(layout)

    def toggle_sending(self):
        if not self.running:  # and (not self.sending_thread.is_alive() if self.sending_thread is not None else False):
            self.running = True
            self.start_button.setText("Cancel")
            # self.sending_thread = threading.Thread(target=self.start_sending)
            # self.sending_thread.start()
            self.start_sending()
            self.running = False
        else:
            self.running = False
            self.start_button.setText("Start")

    def update_line_delay_min_label(self, value):
        self.line_delay_min_value_label.setText(str(value))

    def update_line_delay_max_label(self, value):
        self.line_delay_max_value_label.setText(str(value))

    def update_action_delay_min_label(self, value):
        self.action_delay_min_value_label.setText(str(value))

    def update_action_delay_max_label(self, value):
        self.action_delay_max_value_label.setText(str(value))

    def start_sending(self):
        line_delay_enabled = self.line_delay_enabled.isChecked()
        line_delay_min = self.line_delay_min.value()
        line_delay_max = self.line_delay_max.value()

        action_delay_enabled = self.action_delay_enabled.isChecked()
        action_delay_min = self.action_delay_min.value()
        action_delay_max = self.action_delay_max.value()

        delete_message = self.delete_message.isChecked()

        message = self.message_input.toPlainText()
        lines = message.split('\n')

        length = len(lines)

        self.loading_bar.setMaximum(length)

        while not focused():
            time.sleep(1)

        for i, line in enumerate(lines):
            if not self.running:
                self.loading_bar.setValue(self.loading_bar.maximum())
                return

            # line = line.strip()
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
                self.loading_bar.setValue(i + 1)
                print(line)

                if line_delay_enabled and i != length - 1:
                    time.sleep(random.uniform(line_delay_min, line_delay_max))

        if delete_message:
            delete_last_message(line_delay_enabled, line_delay_min, line_delay_max, action_delay_enabled,
                                action_delay_min, action_delay_max)

        self.toggle_sending()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DiscordMessageSenderApp()
    window.show()
    sys.exit(app.exec_())
