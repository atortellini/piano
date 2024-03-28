import time
import os
import threading
import queue
from pynput import keyboard
import maKeys
import SONG_CLASS
from parser import parse_sheet_music

LIBRARY = 4
STDIN = 5

PRESS = 0
RELEASE = 1
event_queue = queue.Queue()
currently_pressed_notes = set()
SONG_COMPLETED = threading.Event()


def prompt_user_choice():
	usr_choice = -1
	while (usr_choice != 0) and (usr_choice != 1):
		usr_choice = int(input("Please enter your choice (0/1):\n 0. Play from songs/ directory\n 1. Play from stdin\n"))
	if (usr_choice == 0):
		return LIBRARY
	return STDIN

def on_press(key):
	if key == keyboard.KeyCode.from_char('='):
		event_queue.put(PRESS)

def on_release(key):
	if key == keyboard.KeyCode.from_char('='):
		event_queue.put(RELEASE)


def process_events():
	global usr_song
	held = False
	current_note = 0
	while current_note < usr_song.num_notes:
		try:
			event_type = event_queue.get(block=False)
			if event_type == PRESS:
				if not(held):
					for note in usr_song.notes[current_note]:
						maKeys.pressLetter(note)
						currently_pressed_notes.add(note)
					held = True
					current_note += 1
					continue
			elif event_type == RELEASE:
				for note in currently_pressed_notes:
					maKeys.releaseLetter(note)
				currently_pressed_notes.clear()
				held = False

		except queue.Empty:
			continue
	for note in currently_pressed_notes:
		maKeys.releaseLetter(note)
	SONG_COMPLETED.set()

if __name__ == "__main__":
	usr_choice = prompt_user_choice()
	global usr_song
	if (usr_choice == LIBRARY):
		song_Lib = SONG_CLASS.Library()
		song_Lib.list_songs()
		usr_song = song_Lib.read_selected_song()
	else:
		usr_song = SONG_CLASS.Song()
		usr_song.add_notes_from_stdin()
	print("Notes ready to play, press '=' whenever...")
	listener = keyboard.Listener(on_press=on_press, on_release=on_release)
	listener.start()
	event_thread = threading.Thread(target=process_events)
	event_thread.start()

	SONG_COMPLETED.wait()	
	
	listener.stop()
	print("Song completed.\n")

