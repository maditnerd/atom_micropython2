class NeopixelScroller:

    def __init__(self, neopixels, message, font,
                 display_width=5, display_height=5,
                 foreground_color=(20, 20, 20), background_color=(0, 0, 0)):
        self.neopixels = neopixels
        self.message = message
        self.font = font
        self.display_width = display_width
        self.display_height = display_height
        self.message_width = font.get_width(message) + len(message) + font.get_width(' ')
        self.foreground_color = foreground_color
        self.background_color = background_color
        self.offset = 0

    def scroll(self, delta=1):
        for pixel_index in range(self.display_width * self.display_height):
            self.neopixels[pixel_index] = self.background_color
        destination_x = -self.offset
        for char in self.message:
            self.font.bit_blit(char,
                               self.neopixels,
                               destination_x, 0, self.display_width, self.display_height,
                               self.foreground_color, self.background_color)
            destination_x += self.font.get_width(char)
            destination_x += 1
        self.offset += delta
        self.offset %= self.message_width
