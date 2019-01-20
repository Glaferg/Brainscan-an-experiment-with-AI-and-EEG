# Brainscan an experiment with AI and EEG 
By Gabriel Fergesen




more code will come soon


The goal of Brainscan: an experiment with AI and EEG is to teach a AI what boredom is via custom data software for recording
data from two types of biosensors: HR (on the finger) and EEG. Currently development of testing software to stimulate boredom is under
development.

This project is my debute and is a demo

# How to do it

Materials:
Working computer
a human brain(no zombies or monkeys, sorry)
Google Chrome or Firefox quantom web browser
Internet(to download things)
Arduino Nano(elegoo or arduino/genuino)


Download Wekinator from platforms/Wekinator
Download WekiInputHelper
download wekinator's helper software for arduino input from http://www.wekinator.org/examples/#Arduino. DO NOT INSTALL RUN ON ARDUINO.
Open WekiInputHelper and go to file/open project and select WekiBrain server. click Open
Repeat in Wekinator, but find the wekibrain AI file
look through your computer for serial with processing_adaptive inputs
grab arduino nano either ELEGOO OR ARDUINO/GENUINO
run and select the serial port your board is on. If you are on mac, this will appear as dev/tty/acmo/usb modem (insert number here) On windows, it appears as a COM port.
It should say sending 0 inputs. Don't panic, this is normal.
Go to Arduino Create at https://create.arduino.cc/ If you don't have a login or have the plugin installed, the site will guide you through the steps.
Once set up, go to  https://create.arduino.cc/editor/Glaf3rg/790022e4-979a-46ad-9d5a-096c6f7f35b1/preview to install WekiBrain on your arduino. Select the COM/ USBMODEM that is the nano.
Select the board. 
Type in nano and select your board flavor.
Click load and as soon as the lights stop blinking, the system is ready to use!
Go back to serial with processing_adaptive inputs and select the com/ACMO of your newly loaded nano
in a few seconds, 11 inputs should be rolling in!!
If they aren't: a) check to see if your board is plugged in b) reselect com/ACMO and you should be getting 11 inputs
YOU NOW SHOULD BE READY TO ASSEMBLE THE HEADSET.
Buy a Neurosky® mindflex headset and hack according to frontiernerds.com/brain-hack
WARNING: the hack is half-duplex so once the hack is complete you will be able to get serial data but you won't be able to load code on

# Roadmap:

1: inital commit
2: changed idea
3.created WekiBrain helper software
4:wekinator runtime 
5: NOT DONE: build headset
