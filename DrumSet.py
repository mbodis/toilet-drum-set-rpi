from Drum import Drum
from ToiletWall import ToiletWall
from IntroAnimation import IntroAnimation


class DrumSet:

    def __init__(self):
        self.drumsCount = 8
        self.toilet_wall = ToiletWall()
        self.toilet_wall.turn_off_all_leds()

        self.__init_drums()

        # init & run intro animation
        IntroAnimation(self.toilet_wall)

    def __init_drums(self):
        self.drum = []

        idxs0 = (0, 1)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(21, idxs0, (255, 0, 0))
        new_drum.add_new_note(44, idxs0, (255, 255, 0))
        new_drum.add_new_note(42, idxs0, (255, 0, 255))
        new_drum.add_new_note(46, idxs0, (255, 255, 255))
        self.drum.append(new_drum)

        idxs1 = (2, 3)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(48, idxs1, (0, 255, 0))
        self.drum.append(new_drum)

        idxs2 = (4, 5)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(45, idxs2, (0, 255, 255))
        self.drum.append(new_drum)

        idxs3 = (6, 7)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(38, idxs3, (150, 30, 0))
        new_drum.add_new_note(40, idxs3, (50, 180, 150))
        self.drum.append(new_drum)

        idxs4 = (8, 9)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(36, idxs4, (128, 100, 150))
        self.drum.append(new_drum)

        idxs5 = (10, 11)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(43, idxs5, (20, 30, 255))
        self.drum.append(new_drum)

        idxs6 = (12, 13)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(51, idxs6, (58, 0, 150))
        self.drum.append(new_drum)

        idxs7 = (14, 15)
        new_drum = Drum(self.toilet_wall)
        new_drum.add_new_note(49, idxs7, (100, 150, 20))
        self.drum.append(new_drum)

    def new_action_note_on(self, channel: int, note: int, velocity: int):
        # log note
        self.log_note_event("note on:", channel, note, velocity)

        # new note was played
        for drumIdx in range(self.drumsCount):
            self.drum[drumIdx].event_is_note_on(note, velocity)

    def log_note_event(self, msg: str, channel: int, note: int, velocity: int):
        print("----- ", msg, " -----")
        print("channel: ", channel)
        print("note: ", note)
        print("velocity: ", velocity)
        print("")

    def update_note_status(self):
        for drumIdx in range(self.drumsCount):
            self.drum[drumIdx].draw_drum_effect()
