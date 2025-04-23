# Keypad Configuration Tool

This is a graphical configuration tool for creating and editing key bindings for the [Pimoroni Pico RGB Keypad](https://shop.pimoroni.com/products/pico-rgb-keypad-base). The tool provides a virtual 4x4 keypad interface that allows you to visually assign colors, key codes, and behaviors (like key repeat) for each button, and then save or load your configuration.  
It is intended to be used with my [Keypad Software](https://github.com/Man2787/Keypad)


## Features

- Visual 4x4 keypad layout with color selection

- Assign up to 3 keys per button

- Toggle key repeat behavior

- Copy/paste button settings with clipboard support

- Save and load configuration files (`KeypadSave.save`)


## Installation

1. Make sure Python 3.7+ is installed.

2. Install the required Python packages:

```bash
pip install dearpygui pyperclip
```


## Usage

Run the tool with:
```bash
python KeypadConfig.py
```
Once the GUI launches, you can:

* Click any button on the virtual keypad to open an inspector window.
* Edit the button's color, pressed color, key bindings, and repeat setting.
* Use the menu bar to save or load configurations to/from KeypadSave.save.

> **Note:**  
> Make sure to save your configuration before closing the app to preserve your changes.

> **Important:**  
> At the moment this is unable to save directly to the Raspberry Pi so you have to manualy bring the KeypadSave.save file onto the board.
