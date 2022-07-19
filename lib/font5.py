class Font5:

    def __init__(self):
        self.blocks = {'A': b'\x1e\x05\x05\x1e', 'B': b'\x1f\x15\x15\x0a',
                       'C': b'\x0e\x11\x11\x11', 'D': b'\x1f\x11\x11\x0e',
                       'E': b'\x1f\x15\x15\x11', 'F': b'\x1f\x05\x05\x01',
                       'G': b'\x0e\x11\x15\x0d', 'H': b'\x1f\x04\x04\x1f',
                       'I': b'\x11\x1f\x11', 'J': b'\x08\x10\x10\x0f',
                       'K': b'\x1f\x04\x0a\x11', 'L': b'\x1f\x10\x10\x10',
                       'M': b'\x1f\x02\x04\x02\x1f', 'N': b'\x1f\x02\x04\x1f',
                       'O': b'\x0e\x11\x11\x0e', 'P': b'\x1f\x05\x05\x02',
                       'Q': b'\x0e\x11\x19\x1e', 'R': b'\x1f\x05\x0d\x12',
                       'S': b'\x12\x15\x15\x09', 'T': b'\x01\x01\x1f\x01\x01',
                       'U': b'\x0f\x10\x10\x0f', 'V': b'\x03\x0c\x10\x0c\x03',
                       'W': b'\x1f\x08\x04\x08\x1f', 'X': b'\x11\x0a\x04\x0a\x11',
                       'Y': b'\x01\x02\x1c\x02\x01', 'Z': b'\x19\x15\x13\x11',
                       '0': b'\x0e\x13\x19\x0e', '1': b'\x12\x1f\x10',
                       '2': b'\x12\x19\x15\x12', '3': b'\x15\x15\x15\x0a',
                       '4': b'\x06\x05\x1f\x04', '5': b'\x17\x15\x15\x09',
                       '6': b'\x0e\x15\x15\x09', '7': b'\x11\x09\x05\x03',
                       '8': b'\x0a\x15\x15\x0a', '9': b'\x12\x15\x15\x0e',
                       ' ': b'\x00\x00', '?': b'\x01\x15\x05\x02', '!': b'\x17',
                       '.': b'\x10', ':': b'\x0a', ',': b'\x10\x08',
                       '\'': b'\x03', '"': b'\x03\x00\x03',
                       '(': b'\x0e\x11', ')': b'\x11\x0e',
                       '[': b'\x1f\x11', ']': b'\x11\x1f',
                       '{': b'\x04\x1b\x11', '}': b'\x11\x1b\x04',
                       '<': b'\x04\x0a\x11', '>': b'\x11\x0a\x04',
                       '_': b'\x10\x10\x10', '|': b'\x1f',
                       '+': b'\x04\x0e\x04', '-': b'\x04\x04\x04',
                       '*': b'\x0a\x04\x0a', '/': b'\x08\x04\x02',
                       '=': b'\x0a\x0a\x0a', '#': b'\x0a\x1f\x0a\x1f\x0a',
                       '%': b'\x13\x09\x04\x12\x19',
                       '@': b'\x0e\x17\x17\x06', '°': b'\x02\x05\x02'
                       }

    def get_width(self, string):
        width = 0
        for char in string:
            width += len(self.blocks[char])
        return width

    def get_height(self):
        return 5

    def bit_blit(self, char, pixels,
                 destination_x, destination_y, destination_w, destination_h,
                 foreground_color, background_color):
        block = self.blocks[char]
        for source_x in range(len(block)):
            x = source_x + destination_x
            if x >= 0 and x < destination_w:
                column = block[source_x]
                for source_y in range(5):
                    y = source_y + destination_y
                    if y >= 0 and y < destination_h:
                        pixel_index = y + destination_w * (destination_w - x - 1)
                        row_mask = 1 << source_y
                        pixels[pixel_index] = foreground_color if column & row_mask > 0 else background_color
