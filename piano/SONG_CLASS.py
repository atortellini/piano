from parser import parse_sheet_music
import sys

AUTOPLAY = 0
GUIDED_PLAY = 1


def read_stdin():
	lines = sys.stdin.readlines()
	combo = ['']
	for line in lines:
		if line[-1] == '\n':
			combo[0] += line[:-1]
		else:
			combo[0] += line
	return combo[0]

class Song:
	def __init__(self):
		self.playback_method = GUIDED_PLAY
		self.bpm = 0
		self.notes = []
		self.num_notes = 0


	def add_notes(self):
		valid = 0
		while not(valid):
			print("Enter QWERTY piano notes (CTRL + D when done):")
			usr_music = read_stdin()
			valid = parse_sheet_music(usr_music, self.notes)
		self.num_notes = len(self.notes)





