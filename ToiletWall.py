import board
import time
import neopixel

from constants import COLOR_BLACK

# display
NUM_LEDS = 192
NUM_ROWS = 12
NUM_COLS = 16

# leds
LED_PIXEL_PIN = board.D18  # pin that the NeoPixel is connected to
LED_ORDER = neopixel.RGB  # pixel color channel order


class ToiletWall:

    def __init__(self):
        self.num_rows = NUM_ROWS
        self.num_cols = NUM_COLS
        self.num_leds = NUM_LEDS
        self.doesScreenNeedRedraw = 0
        # ledIdx[0][0] - bottom left corner (first LED in strip)
        # ledIdx[NUM_ROWS-1][NUM_COLS-1] - top right corner (last LED in strip)
        self.ledIdx = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16],
            [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47],
            [63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48],
            [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
            [95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80],
            [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111],
            [127, 126, 125, 124, 123, 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112],
            [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143],
            [159, 158, 157, 156, 155, 154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144],
            [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175],
            [191, 190, 189, 188, 187, 186, 185, 184, 183, 182, 181, 180, 179, 178, 177, 176]
        ]
        time.sleep(3)  # keep enough itme to init LEDs (probably make sense only for arduino :D)
        self.leds = neopixel.NeoPixel(
            LED_PIXEL_PIN,
            self.num_leds,
            auto_write=False,
            pixel_order=LED_ORDER)

    def change_led(self, row: int, col: int, color):
        # TODO python does not have pointers, leds should be global :/
        # do not change led if it's same color
        # if self.doesScreenNeedRedraw == 0 and (
        #         (color[0] != self.leds[self.ledIdx[row][col]][0])
        #         or (color[1] != self.leds[self.ledIdx[row][col]][1])
        #         or (color[2] != self.leds[self.ledIdx[row][col]][2])
        # ):
        #     self.doesScreenNeedRedraw = 1

        # skip possible invalid data
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.leds[self.ledIdx[row][col]] = color

    def show(self):
        # TODO python does not have pointers, leds should be global :/
        # if self.doesScreenNeedRedraw:
        #     self.doesScreenNeedRedraw = 0
        #     self.leds.show()
        # else:
        #     print('skipping redraw')
        self.leds.show()

    def turn_off_all_leds(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.change_led(row, col, COLOR_BLACK)

    def turn_on_row(self, row: int, color):
        for col in range(self.num_cols):
            self.change_led(row, col, color)

    def turn_off_row(self, row: int):
        for col in range(self.num_cols):
            self.change_led(row, col, COLOR_BLACK)

    def turn_on_column(self, col: int, color):
        for row in range(self.num_rows):
            self.change_led(row, col, color)

    def turn_off_column(self, col: int):
        for row in range(self.num_rows):
            self.change_led(row, col, COLOR_BLACK)
