import time
import os
import threading
import queue
from pynput import keyboard
import maKeys
import SONG_CLASS
from parser import parse_sheet_music


PRESS = 0
RELEASE = 1
event_queue = queue.Queue()
currently_pressed_notes = set()
SONG_COMPLETED = threading.Event()



#usr_song.set_playback_method()



# def on_press_alt(key):
# 	global key_pressed_alt
# 	key_pressed_alt = True

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
	global usr_song
	usr_song = SONG_CLASS.Song()
	usr_song.add_notes()
	print("Notes ready to play, press '=' whenever...")
	# if usr_song.playback_method == SONG_CLASS.GUIDED_PLAY: 
	listener = keyboard.Listener(on_press=on_press, on_release=on_release)
	listener.start()
	event_thread = threading.Thread(target=process_events)
	event_thread.start()

	SONG_COMPLETED.wait()	
	# else:
	# 	global key_pressed_alt
	# 	key_pressed_alt = False
	# 	current_note = 0
	# 	tempo = 60 / usr_song.bpm
	# 	listener = keyboard.Listener(on_press=on_press_alt)
	# 	listener.start()
	# 	print("Press any key to begin")
	# 	while not(key_pressed_alt):
	# 		time.sleep(1)
	# 	for notes in usr_song.notes:
	# 		for note in notes:
	# 			maKeys.pressLetter(note)
	# 			currently_pressed_notes.add(note)
	# 		for note in currently_pressed_notes:
	# 			maKeys.releaseLetter(note)
	# 		currently_pressed_notes.clear()
	# 		time.sleep(tempo)

	listener.stop()
	print("Song completed.\n")

