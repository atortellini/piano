from parser import parse_sheet_music
import sys
import os

DIRECTORY = "songs/"
AUTOPLAY = 0
GUIDED_PLAY = 1

def sanitize_input(lines):
	combo = ['']
	for line in lines:
		if line[-1] == '\n':
			combo[0] += line[:-1]
		else:
			combo[0] += line
	return combo[0]


class Library:
	def __init__(self, directory=DIRECTORY):
		self.directory = directory
		self.songs = [file for file in os.listdir(self.directory) if file.endswith(".txt")]
		self.num_songs = len(self.songs)

	def list_songs(self):
		if self.num_songs == 0:
			print(f'No songs found in {self.directory}. Make sure song files end with .txt\n')
			sys.exit()

		print(f'Songs found in {self.directory}:\n')
		i = 0
		for song in self.songs:
			print(f'{i}. {song}\n')
			i += 1

	def read_selected_song(self):
		num_selected_song = -1
		while (num_selected_song < 0) or (num_selected_song > self.num_songs - 1):
			num_selected_song = int(input("Please enter the listed number of the song you would like to play: "))
		
		selected_song = Song()
		selected_song.add_notes_from_file(self.directory + self.songs[num_selected_song])
		return selected_song





class Song:
	def __init__(self):
		self.playback_method = GUIDED_PLAY
		self.bpm = 0
		self.notes = []
		self.num_notes = 0


	def add_notes_from_stdin(self):
		valid = 0
		while not(valid):
			print("Enter QWERTY piano notes (CTRL + D when done):")
			lines = sys.stdin.readlines()
			usr_music = sanitize_input(lines)
			valid = parse_sheet_music(usr_music, self.notes)
		self.num_notes = len(self.notes)
	def add_notes_from_file(self, song_dir):
		print(f'Reading file for notes...\n')
		with open(song_dir, 'r') as file:
			lines = file.readlines()
			file.close()
		notes_str = sanitize_input(lines)
		valid = parse_sheet_music(notes_str, self.notes)
		if not(valid):
			print("Unable to process notes in file")
			sys.exit()
		self.num_notes = len(self.notes)





