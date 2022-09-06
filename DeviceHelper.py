import pygame.midi


def print_device_info():
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )


##
# note we're looking for:
#   3: interface :b'ALSA':, name :b'Alesis Nitro MIDI 1':, opened :0:  (input) VIA USB
##
def get_device_id():
    print_device_info()
    device_name = "Alesis Nitro MIDI 1"
    for idx in range(pygame.midi.get_count()):
        (interf, name, input, output, opened) = pygame.midi.get_device_info(idx)
        if str(name).find(device_name) != -1 and input:
            return idx
    print("Device not found: ", device_name, " make sure device is ON and plugged !")

    return -1
