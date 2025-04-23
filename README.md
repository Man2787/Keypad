# Pico RGB Keypad Keyboard Emulator

This script enables the [Pimoroni Pico RGB Keypad Base](https://shop.pimoroni.com/products/pico-rgb-keypad-base) to emulate keyboard key presses using CircuitPython.

## Installation

1. Follow [this guide](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/circuitpython) to install CircuitPython on your Raspberry Pi Pico.
2. Download the [CircuitPython Library Bundle](https://circuitpython.org/libraries).
3. Copy the contents of the `lib` folder from the downloaded bundle to the `lib` folder on your Pico.

> **Note:**  
> If you’re running low on space, you only need to copy the following files:
> - The `adafruit_hid` folder  
> - The `adafruit_dotstar.mpy` file  

## Usage

You can either:
- Use the provided [keypad configuration file](/KeypadSave.save) to load a premade setup, or  
- Create your own custom configuration using the keypad configuration creator available here: [Keypad Interface Tool](https://github.com/Man2787/Keypad-interface)
