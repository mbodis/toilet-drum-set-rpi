from DrumNote import DrumNote
from ToiletWall import ToiletWall


class Drum:
    def __init__(self, toilet_wall: ToiletWall):
        self.toilet_wall = toilet_wall
        self.note_count = 0
        self.drum_notes = []

    def add_new_note(self, note: int, display_idxs, color):
        self.drum_notes.append(DrumNote(self.toilet_wall, note, display_idxs, color))
        self.note_count += 1

    def event_is_note_on(self, note: int, velocity: int):
        for noteIdx in range(self.note_count):
            if self.drum_notes[noteIdx].does_note_exists(note):
                self.drum_notes[noteIdx].activate_note(velocity)
                return True
        return False

    def draw_drum_effect(self):
        for noteIdx in range(self.note_count):
            self.drum_notes[noteIdx].draw_effect()
