import pygame.midi
import threading
import time

from DeviceHelper import get_device_id
from DrumSet import DrumSet


class ThreadReadingMidi(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

        # wait until drums are connected and enabled
        while True:
            pygame.midi.init()
            device_id = get_device_id()
            if device_id == -1:
                print("device not found sleeping 3 sec")
                time.sleep(3)
                pygame.midi.quit()
                continue
            print("using deviceId: ", device_id)
            self.my_input = pygame.midi.Input(device_id)
            break

    def run(self):
        self.read_input(self.my_input)

    def read_input(self, input_device):
        while True:
            if input_device.poll():  # return true if there are any data
                # read 1 event
                event = input_device.read(1)  # [[[153, 49, 50, 0], 125]]
                event = event[0]  # [[153, 49, 50, 0], 125]
                data = event[0]  # [153, 49, 50, 0]
                timestamp = event[1]  # 125
                note_number = data[1]  # 49
                velocity = data[2]  # 50
                if note_number != 0 and velocity != 0:
                    drum_set.new_action_note_on(9, note_number, velocity)


class ThreadLedDisplay(threading.Thread):
    def __init__(self, thread_id, name):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name

    def run(self):
        while True:
            # TODO implement QUEUE both threads can access ??
            drum_set.update_note_status()


# init drums
drum_set = DrumSet()

# init and run threads
threadReadingMidi = ThreadReadingMidi(1, "Thread-midi")
threadLedDisplay = ThreadLedDisplay(2, "Thread-led")
threadReadingMidi.start()
threadLedDisplay.start()

# TODO cover case when device was unplugged after some time and then plugged back
