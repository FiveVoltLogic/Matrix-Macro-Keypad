# This is some firmware for the Pico which turns it into a macro keyboard when using a matrix keypad. You can modify the keybinds in the ugly if statement below

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

#optional delay before creating the HID for maximum compatibility
time.sleep(1)

#create the HID
kbd = Keyboard(usb_hid.devices)

#set up the row and column arrays
rows = []
row_pins = [board.GP4, board.GP5, board.GP6, board.GP7]
for row in row_pins:
    row_key = digitalio.DigitalInOut(row)
    row_key.direction = digitalio.Direction.OUTPUT
    rows.append(row_key)

columns = []
column_pins = [board.GP0, board.GP1, board.GP2, board.GP3]
for column in column_pins:
    column_key = digitalio.DigitalInOut(column)
    column_key.direction = digitalio.Direction.INPUT
    column_key.pull = digitalio.Pull.DOWN
    columns.append(column_key)


#array of keycodes; if you want to remap see: https://circuitpython.readthedocs.io/projects/hid/en/latest/api.html#adafruit-hid-keycode-keycode /'None' values have no physical connection -This isn't used in this implementation but I've left it in as it may be useful for someone.
keymap = [(Keycode.ONE),(Keycode.TWO),(Keycode.THREE),(Keycode.E),
    (Keycode.FOUR),(Keycode.FIVE),(Keycode.SIX),(Keycode.C),
    (Keycode.SEVEN),(Keycode.EIGHT),(Keycode.NINE),(Keycode.Q),
    (Keycode.KEYPAD_ASTERISK),(Keycode.ZERO),(Keycode.POUND),(Keycode.H)]

#main loop
while True:
    for r in rows: #for each row
        r.value=1 #set row r to high
        for c in columns: #and then for each column
            if c.value: #if a keypress is detected (high row output --> switch closing circuit --> high column input)
                while c.value: #wait until the key is released, which avoids sending duplicate keypresses
                    time.sleep(0.01) #sleep briefly before checking back
                key = rows.index(r) * 4 + columns.index(c) #identify the key pressed via the index of the current row (r) and column (c)
                print(key)
                if key == 0:
                    kbd.send(Keycode.KEYPAD_SEVEN)
                    time.sleep(0.1)
                if key == 1:
                    kbd.send(Keycode.KEYPAD_EIGHT)
                    time.sleep(0.1)
                if key == 2:
                    kbd.send(Keycode.KEYPAD_NINE)
                    time.sleep(0.1)
                if key == 3:
                    kbd.send(Keycode.ALT, Keycode.S)
                    time.sleep(0.1)
                if key == 4:
                    kbd.send(Keycode.KEYPAD_FOUR)
                    time.sleep(0.1)
                if key == 5:
                    kbd.send(Keycode.P)
                    time.sleep(0.1)
                if key == 6:
                    kbd.send(Keycode.KEYPAD_SIX)
                    time.sleep(0.1)
                if key == 7:
                    kbd.send(Keycode.CONTROL, Keycode.PAUSE)
                    time.sleep(0.1)
                if key == 8:
                    kbd.send(Keycode.KEYPAD_ONE)
                    time.sleep(0.1)
                if key == 9:
                    kbd.send(Keycode.KEYPAD_TWO)
                    time.sleep(0.1)
                if key == 10:
                    kbd.send(Keycode.KEYPAD_THREE)
                    time.sleep(0.1)
                if key == 11:
                    kbd.send(Keycode.ALT, Keycode.SHIFT, Keycode.W)
                    time.sleep(0.1)
                if key == 12:
                    kbd.send(Keycode.CONTROL, Keycode.KEYPAD_PLUS)
                    time.sleep(0.1)
                if key == 13:
                    kbd.send(Keycode.CONTROL, Keycode.ZERO)
                    time.sleep(0.1)
                if key == 14:
                    kbd.send(Keycode.CONTROL, Keycode.KEYPAD_MINUS)
                    time.sleep(0.1)
                if key == 15:
                    kbd.send(Keycode.CONTROL, Keycode.S)
                    time.sleep(0.1)
                kbd.release_all() #then release all keys pressed
        r.value=0 #return the row to a low state, in preparation for the next row in the loop
