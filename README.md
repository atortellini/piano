## Impress your friends with how rhythmically (?) you can press '='!
Collection of scripts that allow for the semi-automation of virtual piano playing on macOS.

Control the timing and length of QWERTY piano key presses using '='.

## Folder Structure
```bash
piano/
│
├── docs/              # Documentation for maKeys
│   └── maKeys.md
│
├── piano/             # Package directory
│   ├── __init__.py
│   ├── parser.py      # QWERTY note parsing module
│   ├── piano.py       # Main application module
│   ├── maKeys.py      # Module for emulating keypresses
│   └── SONG_CLASS.py  # Song class + read stdin module
│
├── README.md          # Project README
├── LICENSE            # License file
└── requirements.txt   # Python dependencies
```

## Use

Upon running the main script--something to the likes of:
```bash
python3 piano.py
```
You will be prompted to enter the QWERTY keyboard notes of the song:
```bash
Enter QWERTY piano notes (CTRL + D when done):
```
To properly signal **EOF**, make sure to press ```return``` to create a newline and then ```CTRL + D```.

From there you will receive the prompt:
```Notes ready to play, press '=' whenever...```

To which you can you press ``=`` whenever desired.

Upon completion of the song--all notes played--the program will terminate.

## Limitations
This section is written with regards to the current state of the project as of Mar. 26, 2024. 
- Strictly implemented for macOS. Does not support other operating systems due to nature of keypress emulation in maKeys.py.
- Can only handle one song prior to terminating. 
- Notes can only be provided through stdin (no reading from other files yet)
- The requested song must be played to completion for graceful termination of the program.  *I may implement support for exiting early, along with multiple songs/library of some kind.*

## ~~GUIDED_MODE vs AUTOPLAYER~~ (Mentions of AUTOPLAYER removed from source files in latest commit).
~~If you've looked at the source code and noticed mention of GUIDED_MODE and AUTOPLAYER, this project contains an implementation for an AUTOPLAYER. It differs with respects to the current GUIDED_MODE as AUTOPLAYER mindlessly goes through the song without need for user input. However, since I was very dissatisfied with my poor implementation, it currently sits dormant; pieces of it are commented out in the various script files. If you have a desire to use an AUTOPLAYER, feel free to uncomment the code (no guarantees it functions properly).~~
