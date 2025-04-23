import time
import board
import busio
import usb_hid

from adafruit_bus_device.i2c_device import I2CDevice
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar

#from adafruit_hid.keycode import Keycode
#from adafruit_hid.consumer_control import ConsumerControl
#from adafruit_hid.consumer_control_code import ConsumerControlCode


cs = DigitalInOut(board.GP17)
cs.direction = Direction.OUTPUT
cs.value = 0
num_pixels = 16
pixels = adafruit_dotstar.DotStar(
    board.GP18, board.GP19, num_pixels, brightness=0.5, auto_write=True)
i2c = busio.I2C(board.GP5, board.GP4)
device = I2CDevice(i2c, 0x20)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

held = [0] * 16


class Key:
    def __init__(self, index, color, pressedColor, keyList, repeting):
        self.index = index
        self.color = color
        self.pressedColor = pressedColor
        self.keyList = keyList
        self.repeting = repeting

    def key_pressed(self):
        print(self.keyList)

        pixels[self.index] = self.pressedColor

        if (len(self.keyList) == 1):
            kbd.send(self.keyList[0])
        if (len(self.keyList) == 2):
            kbd.send(self.keyList[0], self.keyList[1])
        if (len(self.keyList) >= 3):
            kbd.send(self.keyList[0], self.keyList[1], self.keyList[3])

        held[self.index] = 1

    def not_pressed(self):
        pixels[self.index] = self.color
        held[self.index] = 0


keysList: list[Key] = []
previousSaveHash: int = 0

def str_to_bool(s: str) -> bool:
    return s.strip().lower() == "true"


def read_button_states(x, y):
    pressed = [0] * 16
    with device:
        device.write(bytes([0x0]))
        result = bytearray(2)
        device.readinto(result)
        b = result[0] | result[1] << 8
        for i in range(x, y):
            if not (1 << i) & b:
                pressed[i] = 1
            else:
                pressed[i] = 0
    return pressed

def SaveFileChanged() -> bool:
    if (not (previousSaveHash == hash(open('KeypadSave.save', 'r').read()))):
        return True
    return False

class Keypad():
    def __init__(self):
        self.Load()

    def Load(self):
        global keysList, previousSaveHash
        print("loading")

        with open('KeypadSave.save', 'r') as file:
            keysList.clear()
            previousSaveHash = hash(file.read())
            file.seek(0)

            for line in file.readlines():
                line = line.strip(' ')
                #previousSaveHash += line
                tokens = line.split("|")
                colorTokens = tokens[1].split(",")
                pressedColorTokens = tokens[2].split(",")

                index = int(tokens[0])
                color = (int(colorTokens[0]), int(
                    colorTokens[1]), int(colorTokens[2]))
                pressedColor = (int(pressedColorTokens[0]), int(
                    pressedColorTokens[1]), int(pressedColorTokens[2]))
                repeting = str_to_bool(tokens[4])
                
                print(repeting)

                keys = []
                if (not tokens[3] == "None"):
                    for key in tokens[3].split(","):
                        keys.append(int(key))

                keyVar = Key(index, color, pressedColor, keys, repeting)

                keysList.append(keyVar)

        print("loaded")

    def MainLoop(self):
        checkTime = 0

        print(len(keysList))

        while True:
            if (checkTime > 100):
                print("checking file")
                if (SaveFileChanged()):
                    self.Load()
                checkTime = 0

            pressed = read_button_states(0, 16)

            for i in range(len(keysList)):
                if pressed[i]:
                    if (keysList[i].repeting):
                        print("repeting")
                        keysList[i].key_pressed()
                    else:
                        if (not held[i]):
                            keysList[i].key_pressed()
                else:
                    keysList[i].not_pressed()

            checkTime += 1

            time.sleep(0.05)
