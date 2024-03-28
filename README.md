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
## ⚠️ Necessary Permissions ⚠️
With the use of the pynput library to monitor when '=' is pressed, it is required that you give the Terminal application, or whichever application you use to run Python scripts, permissions for Input Monitoring.
This can be done by going to **Security & Privacy** settings, scrolling to **Input Monitoring**, and enabling it for the respective application.

## Usage

Upon running the main script--something to the likes of:
```bash
python3 piano.py
```
You will be prompted to select between two modes of piano.py:
```bash
Please enter your choice (0/1):
 0. Play from songs/ directory
 1. Play from stdin

```
If intending to play songs from .txt files, make sure they are included within the songs directory.

The script will then list all of the txt files located in the songs directory, from which you can pick by entering its numbered label.

If intending to use stdin, make sure to properly signal **EOF** by pressing ```return```, and then ```CTRL + D```.

From there you will receive the prompt:
```Notes ready to play, press '=' whenever...```

To which you can you press ``=`` whenever desired.

Upon completion of the song--all notes played--the program will terminate.

## Limitations
This section is written with regards to the current state of the project as of Mar. 27, 2024. 
- Strictly implemented for macOS. Does not support other operating systems due to nature of keypress emulation in maKeys.py.
- Can only handle one song before terminating. 
- ~~Notes can only be provided through stdin~~ txt files containing notes can now be read from as long as they are present within the songs directory!
- The requested song must be played to completion for graceful termination of the program.  *I may implement support for exiting early, along with multiple songs/library of some kind.*

