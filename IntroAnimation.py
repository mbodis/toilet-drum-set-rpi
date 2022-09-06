import random
import time
from ToiletWall import NUM_ROWS, NUM_COLS, ToiletWall


class IntroAnimation:
    def __init__(self, toilet_wall: ToiletWall):
        self.toilet_wall = toilet_wall
        self.intro_color = (140, 140, 140)
        self.__init_led_screen()

    def __init_led_screen(self):
        self.toilet_wall.turn_off_all_leds()
        self.toilet_wall.show()

        rand_init = random.randint(0, 2)
        if rand_init == 0:
            self.__init_screen_0()
        elif rand_init == 1:
            self.__init_screen_1()
        elif rand_init == 2:
            self.__init_screen_2()

        self.toilet_wall.turn_off_all_leds()
        self.toilet_wall.show()

    ##
    # turn on one row up and down
    ##
    def __init_screen_0(self):
        for row in range(NUM_ROWS):
            self.toilet_wall.turn_on_row(row, self.intro_color)
            self.toilet_wall.show()
            # time.sleep(0.004)
            self.toilet_wall.turn_off_row(row)

        time.sleep(0.04)

        for row in range(NUM_ROWS - 2, -1, -1):
            self.toilet_wall.turn_on_row(row, self.intro_color)
            self.toilet_wall.show()
            time.sleep(0.04)
            self.toilet_wall.turn_off_row(row)

    ##
    # turn on one column from left to right and back
    ##
    def __init_screen_1(self):
        for col in range(NUM_COLS):
            self.toilet_wall.turn_on_column(col, self.intro_color)
            self.toilet_wall.show()
            time.sleep(0.04)
            self.toilet_wall.turn_off_column(col)

        time.sleep(0.04)

        for col in range(NUM_COLS - 2, -1, -1):
            self.toilet_wall.turn_on_column(col, self.intro_color)
            self.toilet_wall.show()
            time.sleep(0.04)
            self.toilet_wall.turn_off_column(col)

    ##
    # two lines from top and bottom together meeting in the middle and going back
    ##
    def __init_screen_2(self):
        for row in range(0, int(NUM_ROWS / 2) - 1):
            self.toilet_wall.turn_on_row(row, self.intro_color)
            self.toilet_wall.turn_on_row(NUM_ROWS - 1 - row, self.intro_color)
            self.toilet_wall.show()
            time.sleep(0.04)
            self.toilet_wall.turn_off_row(row)
            self.toilet_wall.turn_off_row(NUM_ROWS - 1 - row)

        for row in range(int(NUM_ROWS / 2) - 1, -1, -1):
            self.toilet_wall.turn_on_row(row, self.intro_color)
            self.toilet_wall.turn_on_row(NUM_ROWS - 1 - row, self.intro_color)
            self.toilet_wall.show()
            time.sleep(0.04)
            self.toilet_wall.turn_off_row(row)
            self.toilet_wall.turn_off_row(NUM_ROWS - 1 - row)

        self.toilet_wall.turn_off_all_leds()
