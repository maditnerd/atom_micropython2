import uasyncio
from machine import Pin
from aiobutton import AIOButton

class Button:
    def __init__(self):
        print("[BUTTON] Active")
        self.pin = Pin(39, Pin.IN, Pin.PULL_UP)
        self.handler = AIOButton(lambda btn: not self.pin.value())
        uasyncio.create_task(self.handler.coro_check())
            