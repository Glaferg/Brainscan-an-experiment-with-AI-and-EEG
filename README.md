# Brainscan an experiment with AI and EEG 
By Gabriel Fergesen




more documentation will come soon


The goal of Brainscan: an experiment with AI and EEG is to teach a AI what boredom is via custom data software for recording
data from two types of biosensors:  EEG. Currently development of testing software to stimulate boredom is under
development.

This project is my debute and is a demo

# How to do it

# Materials:
-Working computer

-Two people (One to record mental state of the subject and one to be the subject.)

-Google Chrome or Firefox quantom web browser

-Unfalutering Internet.

-Arduino Uno(Elegoo or Arduino/Genuino)

-Assembled modified Mindflex headset.

-The Github repository https://github.com/Glaferg/Brainscan-an-experiment-with-AI-and-EEG downloaded to access "Boredom sheets" and AI
configuration files

-Printed Boredom sheets

-Two Pens.

-Quiet area.  

-Complete notes on the project are listed at this site. 

Download The Github repository https://github.com/Glaferg/Brainscan-an-experiment-with-AI-and-EEG. Unpackage and move to documents folder on your computer.

Download Wekinator from http://www.wekinator.org/downloads/

Download WekiInputHelper http://www.wekinator.org/input-helper/

download wekinator's helper software for arduino input from http://www.wekinator.org/examples/#Arduino. DO NOT INSTALL RUN ON ARDUINO.

Open WekiInputHelper and go to file/open project and select WekiBrain server. It should be inside the repo. Click Open.

Repeat in Wekinator, but find the wekibrain AI file.

Grab an arduino uno either ELEGOO OR ARDUINO/GENUINO brand

Look through your computer for an app called "serial with processing_adaptive inputs"

Run and select the serial port your board is on. If you are on mac, this will appear as dev/tty/acmo/usb modem (insert number here) On windows, it appears as a COM port.

It should say, "sending 0 inputs". Don't panic, this is normal.

Go to Arduino Create at https://create.arduino.cc/ If you don't have a login or have the plugin installed, the site will guide you through the steps.

Once set up, go to https://create.arduino.cc/editor/Glaf3rg/790022e4-979a-46ad-9d5a-096c6f7f35b1/preview to install WekiBrain on your arduino. 

Select the board.

Type in "uno" and select your board flavor.

Select the COM/ USBMODEM port that is the uno.

Click load and as soon as the light on the microcontroller stops blinking, the system is ready to use!

Go back to serial with processing_adaptive inputs and select the com/ACMO of your newly loaded nano
in a few seconds, 11 inputs should be rolling in!!

If they aren't: a) check to see if your board is plugged in b) reselect com/ACMO and you should be getting 11 inputs

YOU NOW SHOULD BE READY TO ASSEMBLE THE HEADSET.

Buy a Neurosky® mindflex headset and hack according to frontiernerds.com/brain-hack

You should be finished with assembling your WekiBrain rig!

# How to operate

So you're in. The Nano is running, data is flowing to Wekinator... What next?
How to train the AI, of course. Inside Wekinator's beautiful visual wrapper for AI, there are 3 rows of neat little bars with names. First, the +/- on each row. Quite simply, the + records data into the ai's gesture, and the - removes the last record into the gesture. Each gesture is designed to isolate a condition. When the AI is running, the swirling blue bars show how certain the AI is, and the green light shows which thing is the AI's best guess. To make the AI more sensitive, drag the Match threshold bar up or down to decrese or increse sensitivity. 

# The Proceedure

1.  Find willing test subject.

2.  Print out all six boring math sheets.

3.  Run programs in this order: First, open WekiInputHelper and go to file/open project and select in the pop-up "code/WekiBrain server.prog" It should be inside the repository you downloaded. Second, click Open.

4.  First, open Wekinator and go to file/open project and select in the pop-up "code/wekibrain AI.1/wekibrain AI.1.wekproj" It should be inside the repository you downloaded. Second, click Open.

 
# Roadmap:

1: inital commit
2: changed idea
3.created WekiBrain helper software
4:wekinator runtime 
5: NOT DONE: build headset
