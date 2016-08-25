#! python3



##ALL THANKS TO @AlSweigart


__app__ = 'maphelper'
__date__ = '2016-08-20'
__version__ = '0.1.0'

import pyautogui, os, logging
import win32api



logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
GAME_REGION = (500, 200, 1200, 750)  # (left, top, width, height)


##http://stackoverflow.com/users/252218/boppreh THANKS for this know-how :)

#def listen(conn):

#   logging.info('Starting..{0} {1}')
#   """
#   Calls `handlers` for each keyboard event received. This is a blocking call.
#   """
#   # Adapted from http://www.hackerthreads.org/Topic-42395
#   from ctypes import windll, CFUNCTYPE, POINTER, c_int, c_void_p, byref
#   import win32con, win32api, win32gui, atexit
#
#
#   event_types = {win32con.WM_KEYDOWN: 'key down',
#                  win32con.WM_KEYUP: 'key up',
#                  0x104: 'key down', # WM_SYSKEYDOWN, used for Alt key.
#                  0x105: 'key up', # WM_SYSKEYUP, used for Alt key.
#                 }
#
#   def low_level_handler(nCode, wParam, lParam):
#
#       """
#       Processes a low level Windows keyboard event.
#       """
#       event = KeyboardEvent(event_types[wParam], lParam[0], lParam[1],
#                             lParam[2] == 32, lParam[3])
#       for handler in handlers:
#           handler(event)
#
#       # Be a good neighbor and call the next hook.
#       return windll.user32.CallNextHookEx(hook_id, nCode, wParam, lParam)
#
#   # Our low level handler signature.
#   CMPFUNC = CFUNCTYPE(c_int, c_int, c_int, POINTER(c_void_p))
#   # Convert the Python handler into C pointer.
#   pointer = CMPFUNC(low_level_handler)
#
#   # Hook both key up and key down events for common keys (non-system).
#   hook_id = windll.user32.SetWindowsHookExA(win32con.WH_KEYBOARD_LL, pointer,
#                                         win32api.GetModuleHandle(None), 0)
#
#   # Register to remove the hook when the interpreter exits. Unfortunately a
#   # try/finally block doesn't seem to work here.
#   atexit.register(windll.user32.UnhookWindowsHookEx, hook_id)
#
#   while True
#
#       msg = win32gui.GetMessage(None, 0, 0)


def water_check():
    pyautogui.alert('B TUSU ILE AÇ KAPA')
    logging.info('Starting..')
    is_bot_running = False

    pos = None

    while True:



        i = win32api.GetAsyncKeyState(ord('B'))

        if i:
            is_bot_running = not is_bot_running
            logging.info('BOT STATE CHANGED!')

        if is_bot_running:
            logging.warning('[!]Searching for Water')
            pos = pyautogui.locateCenterOnScreen(im_path('01.png'), region=GAME_REGION)
            if pos is not None:
                logging.warning('[!]Space Found at {0}'.format(pos))
                real_pos = ((pos[0] + 181), pos[1])
                pyautogui.click(real_pos)


def im_path(filename):
    return os.path.join('images', filename)

# EVENTS #

if __name__ == '__main__':
    water_check()