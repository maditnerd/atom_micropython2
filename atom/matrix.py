import uasyncio
from machine import Pin
from font5 import Font5
from neopixel import NeoPixel
from neopixel_scroller import NeopixelScroller

class Matrix():
    def __init__(self, sleep_time=100):
        
        self.red = ((10,0,0))
        self.green = ((0,10,0))
        self.blue = ((0,0,10))
        
        self.sleep_time = sleep_time
        gpio27 = Pin(27, Pin.OUT)
        self.neopixels = NeoPixel(gpio27, 25)
        self.font = Font5()
        self.color = (0, 10, 0)
        self.scroller = None
        self.animation = None
        self.clear()
        self.message = ""
        self.scroller = NeopixelScroller(self.neopixels, self.message, self.font, foreground_color=self.color)
        uasyncio.create_task(self.scroll())

    def clear(self):
        for pixel_index in range(25):
            self.neopixels[pixel_index] = (0, 0, 0)
        self.neopixels.write()

    def fill(self, color):
        self.neopixels.fill(color)
        self.neopixels.write()

    def text_color(self, color):
        self.color = color
        self.scroller.foreground_color = color

    def text(self, message):
        print("[MATRIX] " + message)
        self.message = message.upper()     
        self.scroller = None
        self.scroller = NeopixelScroller(self.neopixels, self.message, self.font, foreground_color=self.color)

    async def scroll(self):
      print("[MATRIX] Start Scroll")
      while True:
        if self.scroller is not None:
            self.scroller.scroll()
            self.neopixels.write()
        await uasyncio.sleep_ms(self.sleep_time)

