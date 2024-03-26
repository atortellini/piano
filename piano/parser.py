

valid_notes = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '!', '@', '$', '%', '^', '*', '(', 'Q', 'W', 'E', 'T', 'Y', 'I', 'O', 'P', 'S', 'D', 'G', 'H', 'J', 'L', 'Z', 'C', 'V', 'B'}




def parse_sheet_music(music_input, notes_array):
	if len(music_input) == 0:
		print("Invalid number of notes entered.\n")
		return 0

	in_chord = False
	j = 0

	for i in music_input:
		if i == ' ' or i == '|':
			continue
		if i in valid_notes:
			if not(in_chord):
				j += 1
				notes_array.append(str(i))
				continue
			notes_array[j] += str(i)
			continue
		if i == '[':			# Works under assumption that no improper starting chord that runs to end of input
			in_chord = True
			notes_array.append('')
			continue
		if i == ']' and in_chord:
			in_chord = False
			j += 1
			continue
		if i not in valid_notes:
			print(f'Ignoring invalid note: {i}...\n')
			continue
		if i == ']' and not(in_chord):
			print("Invalid chord found in input")
			return 0

	return 1


