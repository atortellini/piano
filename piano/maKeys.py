import time
from Quartz.CoreGraphics import CGEventCreateKeyboardEvent, CGEventPost, CGEventGetFlags, CGEventSetFlags, kCGEventFlagMaskShift, \
	CGEventSourceCreate, kCGEventSourceStateHIDSystemState, kCGHIDEventTap

MAK_SOURCE_REF = CGEventSourceCreate(kCGEventSourceStateHIDSystemState)
MAK_LOWERKEYS = {"a": 0x00, "s": 0x01, "d": 0x02, "f": 0x03, "h": 0x04, \
	"g": 0x05, "z": 0x06, "x": 0x07, "c": 0x08, "v": 0x09, "b": 0x0b, \
	"q": 0x0c, "w": 0x0d, "e": 0x0e, "r": 0x0f, "y": 0x10, "t": 0x11, \
	"1": 0x12, "2": 0x13, "3": 0x14, "4": 0x15, "6": 0x16, "5": 0x17, \
	"=": 0x18, "9": 0x19, "7": 0x1a, "-": 0x1b, "8": 0x1c, "0": 0x1d, \
	"]": 0x1e, "o": 0x1f, "u": 0x20, "[": 0x21, "i": 0x22, "p": 0x23, \
	"l": 0x25, "j": 0x26, "'": 0x27, "k": 0x28, ";": 0x29, "\\": 0x2a, \
	",": 0x2b, "/": 0x2c, "n": 0x2d, "m": 0x2e, ".": 0x2f, " ": 0x31, "`": 0x32}
MAK_UPPERKEYS = {"A": 0x00, "S": 0x01, "D": 0x02, "F": 0x03, "H": 0x04, \
	"G": 0x05, "Z": 0x06, "X": 0x07, "C": 0x08, "V": 0x09, "B": 0x0b, \
	"Q": 0x0c, "W": 0x0d, "E": 0x0e, "R": 0x0f, "Y": 0x10, "T": 0x11, \
	"!": 0x12, "@": 0x13, "#": 0x14, "$": 0x15, "^": 0x16, "%": 0x17, \
	"+": 0x18, "(": 0x19, "&": 0x1a, "_": 0x1b, "*": 0x1c, ")": 0x1d, \
	"}": 0x1e, "O": 0x1f, "U": 0x20, "{": 0x21, "I": 0x22, "P": 0x23, \
	"L": 0x25, "J": 0x26, '"': 0x27, "K": 0x28, ":": 0x29, "|": 0x2a, \
	"<": 0x2b, "?": 0x2c, "N": 0x2d, "M": 0x2e, ">": 0x2f, "~": 0x32}
MAK_SHIFT = 0x38

def pressLetter(singleChar):
	if (singleChar in MAK_LOWERKEYS.keys()):
		keyDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_LOWERKEYS[singleChar], True)
		keyDown_fl = int(CGEventGetFlags(keyDown))
		if (keyDown_fl & kCGEventFlagMaskShift):
			CGEventSetFlags(keyDown, int(CGEventGetFlags(keyDown)) ^ kCGEventFlagMaskShift )
		CGEventPost(kCGHIDEventTap, keyDown)
	elif (singleChar in MAK_UPPERKEYS.keys()):
		shiftDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_SHIFT, True)
		CGEventPost(kCGHIDEventTap, shiftDown)
		keyDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_UPPERKEYS[singleChar], True)
		CGEventSetFlags(keyDown, int(CGEventGetFlags(keyDown)) | kCGEventFlagMaskShift )
		CGEventPost(kCGHIDEventTap, keyDown)
		shiftUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_SHIFT, False)
		CGEventPost(kCGHIDEventTap, shiftUp)
	time.sleep(0.0008)

def releaseLetter(singleChar):
	if (singleChar in MAK_LOWERKEYS.keys()):
		keyUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_LOWERKEYS[singleChar], False)
		keyUp_fl = int(CGEventGetFlags(keyUp))
		if (keyUp_fl & kCGEventFlagMaskShift):
			CGEventSetFlags(keyUp, int(CGEventGetFlags(keyUp)) ^ kCGEventFlagMaskShift )
		CGEventPost(kCGHIDEventTap, keyUp)
	elif (singleChar in MAK_UPPERKEYS.keys()):
		keyUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_UPPERKEYS[singleChar], False)
		CGEventSetFlags(keyUp, int(CGEventGetFlags(keyUp)) | kCGEventFlagMaskShift)
		CGEventPost(kCGHIDEventTap, keyUp)
	time.sleep(0.0008)

def typeLetter(singleChar):
	if (singleChar in MAK_LOWERKEYS.keys()):
		keyDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_LOWERKEYS[singleChar], True)
		CGEventPost(kCGHIDEventTap, keyDown)
		keyUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_LOWERKEYS[singleChar], False)
		CGEventPost(kCGHIDEventTap, keyUp)
	elif (singleChar in MAK_UPPERKEYS.keys()):
		shiftDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_SHIFT, True)
		CGEventPost(kCGHIDEventTap, shiftDown)
		keyDown = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_UPPERKEYS[singleChar], True)
		CGEventSetFlags(keyDown, int(CGEventGetFlags(keyDown)) | kCGEventFlagMaskShift )
		CGEventPost(kCGHIDEventTap, keyDown)
		keyUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_UPPERKEYS[singleChar], False)
		CGEventSetFlags(keyUp, int(CGEventGetFlags(keyUp)) | kCGEventFlagMaskShift)
		CGEventPost(kCGHIDEventTap, keyUp)
		shiftUp = CGEventCreateKeyboardEvent(MAK_SOURCE_REF, MAK_SHIFT, False)
		CGEventPost(kCGHIDEventTap, shiftUp)
	time.sleep(0.0008)
