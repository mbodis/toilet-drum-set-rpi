# README #

### What is this repository for? ###
* LED screen made of toiled paper rolls connected to electric drum set
* This is source code for Rpi to make some visual effects
* tested on: RaspberryPi 2B+

### How do I get set it up? ###
* fresh rpi install
* pyhton py-game (use apt-get)
* pyhton midi


### Hardware setup
* adapter: 220V input, 10A 5V output
* LED strip: power, ground connected to adapter
* RPI:
  * main power supply microUSB
  * data GPIO 18 (pin 12) - LED strip
  * ground connected with LED strip and adapter
* Drum set: Alesis Drums Nitro Mesh Kit, connected to RPi via USB cable


### How to quickly run source on RPI ? ###
<b>copy new source via scp</b>
<br>`sshpass -p 'PASS' scp /LOCAL_DRUMS_PATH/*.py pi@192.168.0.xxx:/RPI_DRUMS_PATH/`

<b>when connected on RPi via ssh - start the drums</b>
<br>`cd /RPI_DRUMS_PATH/ && sshpass -p 'PASS' sudo python3.9 ./main.py`