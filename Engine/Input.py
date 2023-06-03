import ctypes
from ctypes.wintypes import *
import time

# CTYPES ADAPTATE -------------------------------

#KEYBOARD
class CHAR_UNION(ctypes.Union):
    _fields_ = [("UnicodeChar", WCHAR),
                ("AsciiChar", CHAR)]

class KEY_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("bKeyDown", BYTE),
                ("pad2", BYTE),
                ('pad1', SHORT),
                ("wRepeatCount", SHORT),
                ("wVirtualKeyCode", SHORT),
                ("wVirtualScanCode", SHORT),
                ("uChar", CHAR_UNION),
                ("dwControlKeyState", INT)]

#MOUSE
class MOUSE_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("dwMousePosition", ctypes.wintypes._COORD),
                ("dwButtonState", INT),
                ("dwControlKeyState", INT),
                ("dwEventFlags", INT)]

#WINDOW BUFFER SIZE
class WINDOW_BUFFER_SIZE_RECORD(ctypes.Structure):
    _fields_ = [("dwSize", ctypes.wintypes._COORD)]

#MENU
class MENU_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("dwCommandId", UINT)]

#FOCUS
class FOCUS_EVENT_RECORD(ctypes.Structure):
    _fields_ = [("bSetFocus", BYTE)]

#UNION
class INPUT_UNION(ctypes.Union):
    _fields_ = [("KeyEvent", KEY_EVENT_RECORD),
                ("MouseEvent", MOUSE_EVENT_RECORD),
                ("WindowBufferSizeEvent", WINDOW_BUFFER_SIZE_RECORD),
                ("MenuEvent", MENU_EVENT_RECORD),
                ("FocusEvent", FOCUS_EVENT_RECORD)]

#RECORD
class INPUT_RECORD(ctypes.Structure):
    _fields_ = [("EventType", SHORT),
                ("Event", INPUT_UNION)]

# -----------------------------------------------

class Input:
	"""Обработка входящих событий окна консоли"""

	def init(useHotkey=False, lineInput=False, echo=False, resizeEvents=False, mouseEvents=False, insert=False, quickEdit=False, extended=False, handle=None):
		"""Включает получение событий\nПринимает: (bool) useHotkey - использование горячих клавиш, (bool) lineInput - описание отсутствует, (bool) echo - добавление в выходной массив, (bool) resizeEvents - принятие событий изменения размеров окна, (bool) mouseEvents - принятие событий мыши, (bool) insert - включает insert, (bool) quickEdit - выделение мышью, (bool) extended - запрет quickEdit"""
		Input.handle = handle or ctypes.windll.kernel32.GetStdHandle(-10)
		Input.events = ctypes.wintypes.DWORD()
		Input.record = (INPUT_RECORD * 32)()
		
		out = 0

		if useHotkey: out += 1
		if lineInput: out += 2
		if echo: out += 4
		if resizeEvents: out += 8
		if mouseEvents: out += 16
		if insert: out += 32
		if quickEdit: out += 64
		if extended: out += 128
		ctypes.windll.kernel32.SetConsoleMode(Input.handle, out)

	def tick():
		"""Получение и запись событий"""

		ctypes.windll.kernel32.ReadConsoleInputExW(Input.handle, ctypes.byref(Input.record), 16, ctypes.byref(Input.events), 2)

		Input.event_count = int(bytes(Input.events)[0])

		events_list = []
		for i in range(Input.event_count):
			event_dict = {}
			event_record = Input.record[i]
			event_type = event_record.EventType 
			event = event_record.Event

			# Event Type classification
			if event_type == 1:
				event_type = "keyboard"

			elif event_type == 2:
				event_type = "mouse"

			elif event_type == 4:
				event_type = "window"

			elif event_type == 8:
				event_type = "menu"

			elif event_type == 16:
				event_type = "focus"

			event_dict["type"] = event_type

			event_dict["mouse_type"] = event.MouseEvent.dwEventFlags
			event_dict["x"] = event.MouseEvent.dwMousePosition.X
			event_dict["y"] = event.MouseEvent.dwMousePosition.Y
			event_dict["mouse_key"] = event.MouseEvent.dwButtonState

			event_dict["key_code"] = event.KeyEvent.wVirtualKeyCode
			event_dict["key_char"] = event.KeyEvent.uChar.UnicodeChar
			event_dict["key_state"] = event.KeyEvent.bKeyDown

			events_list.append(event_dict)

		return events_list