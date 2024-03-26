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


	# def set_playback_method(self):
	# 	req_method = -1
	# 	while ((req_method != AUTOPLAY) and (req_method != GUIDED_PLAY)):
	# 		req_method = int(input("Enter requested playback method:\n 0. AUTOPLAY\n 1. GUIDED_PLAY"))
	# 	self.playback_method = req_method
	# 	if req_method == AUTOPLAY:
	# 		tempo = 0
	# 		while ((tempo < 30) or (tempo > 400)):
	# 			tempo = int(input("Tempo in BMP: (30-400):"))
	# 		self.bpm = tempo







