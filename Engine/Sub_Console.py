import win32pipe, win32file
import sys
import os
import ctypes
import ctypes.wintypes
import win32file
from Input import Input
import json

class CONSOLE_SCREEN_BUFFER_INFO(ctypes.Structure):
    _fields_ = [
        ("dwSize", ctypes.wintypes._COORD),
        ("dwCursorPosition", ctypes.wintypes._COORD),
        ("wAttributes", ctypes.wintypes.WORD),
        ("srWindow", ctypes.wintypes.SMALL_RECT),
        ("dwMaximumWindowSize", ctypes.wintypes._COORD),
    ]

console_id = sys.argv[1]

pipe_in_name = r'\\.\pipe\consolein' + console_id
pipe_out_name = r'\\.\pipe\consoleout' + console_id

pipe_in = win32file.CreateFile(
	pipe_in_name,
	win32file.GENERIC_READ | win32file.GENERIC_WRITE,
	0, None, win32file.OPEN_EXISTING, 0, None
)

pipe_out = win32pipe.CreateNamedPipe(
	pipe_out_name,
	win32pipe.PIPE_ACCESS_DUPLEX,
	win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_WAIT, 1,
	1024 * 1024 * 32,
	1024 * 1024 * 32,
	0, None
)

win32pipe.ConnectNamedPipe(pipe_out, None)
enable = True

out_handle = ctypes.windll.kernel32.GetStdHandle(-11)
ctypes.windll.kernel32.SetConsoleMode(out_handle, 5)
while enable:
	try:
		message = win32file.ReadFile(pipe_out, 1024 * 1024 * 32)
	except:
		enable = False
		quit()
	command = int(message[1][0])
	content = message[1][1:]

	if command == 1:
		enable = False
		quit()

	elif command == 2:
		data = content.decode()
		ctypes.windll.kernel32.WriteConsoleW(out_handle, data, len(data), None, None)

	elif command == 3:
		title = message[1][1:].decode()
		ctypes.windll.kernel32.SetConsoleTitleW(title)

	elif command == 4:
		hwnd = ctypes.windll.kernel32.GetConsoleWindow()
		icon_handle = ctypes.windll.user32.LoadImageW(None, content.decode(), ctypes.wintypes.UINT(1), 0, 0, ctypes.wintypes.UINT(0x00000010))
		ctypes.windll.user32.SendMessageW(hwnd, 0x80, 0, icon_handle)

	elif command == 5:
		w = int.from_bytes([message[1][1], message[1][2]], byteorder="little")
		h = int.from_bytes([message[1][3], message[1][4]], byteorder="little")
		os.system(f'mode con cols={w} lines={h}')

	elif command == 6:
		csbi = CONSOLE_SCREEN_BUFFER_INFO()
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ctypes.windll.kernel32.GetStdHandle(-11), ctypes.byref(csbi))
		w = csbi.srWindow.Right - csbi.srWindow.Left + 1
		h = csbi.srWindow.Bottom - csbi.srWindow.Top + 1
		data = ((1).to_bytes(1, "little")) + (w).to_bytes(1, "little") + (h).to_bytes(1, "little")
		win32file.WriteFile(pipe_in, data)

	elif command == 7:
		data = ((2).to_bytes(1, "little")) + bytes(json.dumps(Input.tick()), "utf-8")
		#print(len(data))
		win32file.WriteFile(pipe_in, data)

	elif command == 8:
		Input.init(extended=True, mouseEvents=True, useHotkey=False)