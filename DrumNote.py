from TimeHelper import current_milli_time
from ToiletWall import ToiletWall, NUM_ROWS
from constants import COLOR_BLACK

DISPLAY_IDX_SIZE = 2
MAX_VELOCITY = 127
SHOW_LED_ADDITIONAL_ANIMATION_MS = 400


def calculate_max_row(velocity: int):
    paint_rows = velocity / MAX_VELOCITY * NUM_ROWS
    # make sure that it's not more than LED_ROWS, I've recorded velocity=153
    if paint_rows > NUM_ROWS:
        paint_rows = NUM_ROWS

    return int(paint_rows)


class DrumNote:

    def __init__(self, toilet_wall: ToiletWall, note: int, display_idxs, color):
        self.toilet_wall = toilet_wall

        # midi
        self.note = note

        # display
        self.color = color
        self.display_idxs = display_idxs

        # animation
        self.one_led_ms = SHOW_LED_ADDITIONAL_ANIMATION_MS / NUM_ROWS  # 400/12 = 33
        self.max_row = -1
        self.last_hidden = -1
        self.last_ts_note_on_event = 0
        self.note_init_execution = False
        self.is_animation_active = False

    def does_note_exists(self, note: int):
        return self.note == note

    def activate_note(self, velocity: int):
        self.is_animation_active = True
        self.last_ts_note_on_event = current_milli_time()
        self.max_row = calculate_max_row(velocity)
        self.note_init_execution = True

    def reset_previous_push(self):
        if self.note_init_execution:
            self.last_hidden = -1
            self.note_init_execution = False

            # clean columns
            for col in range(DISPLAY_IDX_SIZE):
                self.toilet_wall.turn_off_column(self.display_idxs[col])

            # fill columns
            for row in range(self.max_row):
                for col in range(DISPLAY_IDX_SIZE):
                    self.toilet_wall.change_led(row, self.display_idxs[col], self.color)

            # show changes
            self.toilet_wall.show()

    def draw_effect(self):
        redraw = False
        # one time: draw all rows by velocity
        self.reset_previous_push()

        # repeatedly: turn off columns by TS
        if self.is_animation_active:
            curr_diff = current_milli_time() - self.last_ts_note_on_event  # animation diff <0, 400>
            hide_rows = round(curr_diff / self.one_led_ms)
            # print(' ')
            # print("curr_diff:", curr_diff, "hide_rows:", hide_rows, "max_row:", self.max_row, "last_hidden:", self.last_hidden)
            # print(' ')

            # case: nothing was hide yet
            # case: hide nex row
            if self.last_hidden == -1 or ((self.max_row - hide_rows) != self.last_hidden):
                hide_row = self.max_row - hide_rows
                for col in range(DISPLAY_IDX_SIZE):

                    # print("last_hidden:", self.last_hidden, "hide_row", hide_row, " col ", col)

                    if self.last_hidden == -1:
                        self.last_hidden = self.max_row
                    for row in range(self.last_hidden, hide_row, -1):
                        self.toilet_wall.change_led(
                            row,
                            self.display_idxs[col],
                            COLOR_BLACK)
                        # print("hiding row (foreach) -- ", row)

                self.last_hidden = self.max_row - hide_rows
                redraw = True

            if self.last_hidden < 0:
                self.last_hidden = -1
                self.is_animation_active = False

            if curr_diff > SHOW_LED_ADDITIONAL_ANIMATION_MS:
                self.last_hidden = -1
                self.is_animation_active = False

        return redraw
