#! python3


__app__ = 'overlordsBot'
__author__ = 'Ogulcan Gurcaglar'
__date__ = '2016-08-20'
__version__ = '0.1.0'

import pyautogui, os, logging
import pyhooked

logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')
#logging.disable(logging.DEBUG) # uncomment to block debug log messages


def key(event):
    logging.info("pressed", repr(event.char))

GAME_REGION = (500, 200, 1200, 750)  # (left, top, width, height) values coordinates of the game window


def main():
    isBotRunning = None

    while True:
            continue

        if isBotRunning:
            randomMovement()





def im_path(filename):
    return os.path.join('images', filename)


def randomMovement():
    waterCheck()


def waterCheck():
    pos = None


    while True:  # loop because it could be the blue or pink Play button displayed at the moment.
        logging.warning('[!]Searching for Water')
        pos = pyautogui.locateCenterOnScreen(im_path('01.png'), region=GAME_REGION)
        if pos is not None:
            logging.warning('[!]Space Found at {0}'.format(pos))
            break
    realPos = ((pos[0] + 181), pos[1])
    pyautogui.click(realPos)


def MoveUp():
    pyautogui.keyDown('w')
def MoveRight():
    pyautogui.keyDown('d')
def MoveLeft():
    for i in range(15):
        pyautogui.keyDown('a')
    pyautogui.keyUp('a')
def MoveDown():
    pyautogui.keyDown('s')



main()