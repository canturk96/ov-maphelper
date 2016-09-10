import pyautogui, os, time, glob
import win32api,win32con
from zenlog import log
import random
import winsound


class Core:
    def __init__(self):
        # ekrani bese boldum
        self.MAIN_REGION = (50, 50, 1660, 900)
        pyautogui.FAILSAFE = False
        self.vectors = {}
        self.Freq = 1100  # Set Frequency To 2500 Hertz
        self.Dur = 300  # Set Duration To 1000 ms == 1 second


        log.info('CORE INIT completed. Welcome to OV-bot v1.2')

        Core.vectors_init(self)
        Core.region_init(self)

    def region_init(self):
        # ekrani bese boldum
        self.MAIN_REGION = (50, 50, 1660, 900) # (left, top, width, height) # MAIN REGION
        log.info('regions init completed.')

    def vectors_init(self):
        self.vectors = {"up": (955, 300),
                        "down": (937, 810),
                        "left": (502, 480),
                        "right": (1600, 650),
                        "stuckmove": (640, 450)}

        log.info('vectors init completed.')

    def mouse_right_click(self, move="No Way Bro"):
        cords = (self.vectors[move][0], self.vectors[move][1])
        if move is "left":
            win32api.SetCursorPos((self.vectors['left'][0], self.vectors['left'][1]))
        elif move is 'right':
            win32api.SetCursorPos((self.vectors['right'][0], self.vectors['right'][1]))
        elif move is 'up':
            win32api.SetCursorPos((self.vectors['up'][0], self.vectors['up'][1]))
        elif move is 'down':
            win32api.SetCursorPos((self.vectors['down'][0], self.vectors['down'][1]))
        elif move is 'stuckmove':
            win32api.SetCursorPos((self.vectors['stuckmove'][0], self.vectors['stuckmove'][1]))
        else:
            log.error('no vector specified. mouse_right_click function.' + str(self.vectors[move][0]) + ',' +
                      str(self.vectors[move][1]))
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, cords[0], cords[1])
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, cords[0], cords[1])
        time.sleep(1)
        log.info('mouse_right_click -> '+str(self.vectors[move][0])+','+str(self.vectors[move][1]))

    def _earth_search_main(self):
        log.i('looking main')
        pos = pyautogui.locateCenterOnScreen("botmods/images/sari.png", region=self.MAIN_REGION)
        if pos is not None:
            Core._what_is_my_pos(self, pos)
            return True
        else:
            return False

    def _what_is_my_pos(self, pos):
        log.i('what is my position...')
        if pos is None:
            pos = (0, 0)
        x = pos[0]
        y = pos[1]

        if x < 520:
            log.w('yellow dot detected at left !')
            params = {"move": "right"}
            Core.mouse_right_click(self, **params)
            time.sleep(10)

        elif x > 1600:
            log.w('yellow dot detected at right !')
            params = {"move": "left"}
            Core.mouse_right_click(self, **params)
            time.sleep(10)

        elif y > 800:
            log.w('yellow dot detected at lower !')
            params = {"move": "up"}
            Core.mouse_right_click(self, **params)
            time.sleep(10)

        elif y < 210:
            log.w('yellow dot detected at upper !')
            params = {"move": "down"}
            Core.mouse_right_click(self, **params)
            time.sleep(10)

        else:
            params = {"move": "stuckmove"}
            Core.mouse_right_click(self, **params)
            log.i('Random MOVE')

    def _intel_move(self, pos):
        if pos is None:
            pos = (0, 0)
        x = pos[0]
        y = pos[1]

        if x < 520:
            log.w('intel move to left !')
            params = {"move": "left"}
            Core.mouse_right_click(self, **params)
            time.sleep(1)

        elif x > 1600 or 520 < x < 1600:
            log.w('intel move to right !')
            params = {"move": "right"}
            Core.mouse_right_click(self, **params)
            time.sleep(1)

        elif y > 800 or 210 < y < 800:
            log.w('intel move to down !')
            params = {"move": "down"}
            Core.mouse_right_click(self, **params)
            time.sleep(1)

        elif y < 210:
            log.w('intel move to upper !')
            params = {"move": "up"}
            Core.mouse_right_click(self, **params)
            time.sleep(1)
        elif x is 0 and y is 0:
            params = {"move": "stuckmove"}
            Core.mouse_right_click(self, **params)
            log.i('Random MOVE')
        else:
            params = {"move": "stuckmove"}
            Core.mouse_right_click(self, **params)
            log.i('Random MOVE')

    def earth_search(self, the_last_pos):
        while True:
            if Core._earth_search_main(self):
                break
            else:
                log.i('Intel MOVE')
                Core._intel_move(self, the_last_pos)
                break

    def main_function(self):
        is_bot_running = False
        is_pathfinder_running = False
        no_water = 0
        water_count = 0
        the_last_pos = None

        stuck_meter = 0
        log.w('getting into main_function')
        while True:

            b = win32api.GetAsyncKeyState(ord('B'))
            v = win32api.GetAsyncKeyState(ord('V'))

            if b:
                is_bot_running = not is_bot_running
                log.c('BOT STATE -> ' + str(is_bot_running))
                winsound.Beep(self.Freq, self.Dur)

            if v:
                is_pathfinder_running = not is_pathfinder_running
                log.c('Pathfinder STATE -> ' + str(is_pathfinder_running))
                winsound.Beep(self.Freq, self.Dur)

            if is_bot_running:


                pos = pyautogui.locateCenterOnScreen(Core.im_path('01.png'), region=self.MAIN_REGION)


                if stuck_meter > 20:
                    log.i('stuck meter > ' + str(stuck_meter))
                    real_pos = ((pos[0] + 181), pos[1])
                    the_last_pos = real_pos
                    pos = None

                    stuck_meter = 0
                    log.i('Random MOVE')
                    Core.earth_search(self, the_last_pos)

                if pos is not None:
                    log.w('We found Water space !')
                    real_pos = ((pos[0] + 181), pos[1])
                    pyautogui.click(real_pos)
                    stuck_meter += 1
                    the_last_pos = real_pos

                    water_count += 1
                    log.i('Total Water Parsed : ' + str(water_count))

                else:
                    v = win32api.GetAsyncKeyState(ord('V'))
                    if v:
                        is_pathfinder_running = not is_pathfinder_running
                        log.c('Pathfinder STATE -> ' + str(is_pathfinder_running))

                    no_water += 1
                    if is_pathfinder_running:
                        if no_water > 5:
                            log.i('Searching For Earth! no water seen for:' + str(no_water))
                            Core.earth_search(self, the_last_pos)
                            the_last_pos = None
                            no_water = 0
                    else:
                        log.i('No water seen for:' + str(no_water))

    @staticmethod
    def im_path(filename):
        return os.path.join('botmods/images', filename)
