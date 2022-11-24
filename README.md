This is a stripped down version of the project by TEC.IST that can be found here: https://hackaday.io/project/178204-the-smallest-keyboard

# Introduction

I found a matrix keypad in an old bit of telecommunication hardware that had a really nice click to the button push.
I took it out of the equipment and it sat on my desk for about a month while I played around with it.
Eventually I decided that I had to do something with it, to make it useful again so I looked out for a way to turn it into a macropad.

The only code I could find was for either a matrix keypad or a macro keypad that wired each button to a different IO on an arduino or pi pico.

Finally I found [The Smallest Keyboard](https://hackaday.io/project/178204-the-smallest-keyboard) which does both. Of course there were way more keys than I need,
so I stripped it down for my purposes, and as I wanted to use Ctrl and Alt keyboard shortcuts, I added a long and ugly if statement to do that.

# Hardware
For this project I used a Raspberry Pi Pico and a 4x4 matrix keypad that I found. You can however use any matrix keypad or make your own.

# Requirements
The code requires that [Circuit Python](https://circuitpython.org/board/raspberry_pi_pico/) be installed on the Pi Pico - Just copy the U2F file to the Pico. You will also need the [Adafruit HID keyboard and keycode libraries](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/) - Download the library that matches your version of Circuit Python and copy the files at /lib/adafruit_hid/ to the /lib folder on the Pico.

# Programming
To program this, you can quite simply drag and drop the code.py file to the pico, or to test, you can use thonny and select the pico as the interpreter. I found a tutorial [here](https://kitronik.co.uk/blogs/resources/first-steps-with-the-raspberry-pi-pico-and-thonny) but a quick [Searx]([https://searx.fmac.xyz/](https://searx.fmac.xyz/search?q=pi%20pico%20thonny%20interpreter&language=en-GB&time_range=None&safesearch=1&categories=general)) will give you instructions on setting this up.
