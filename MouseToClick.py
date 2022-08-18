import aircv as ac
from pymouse import *
from PIL import ImageGrab
import win32api, win32con



class MouseToClick(object):
    # 擷取整個螢幕
    @classmethod
    def screenshot(cls):
        filename = 'screen.png'
        im = ImageGrab.grab()
        im.save(filename)

    # 獲取對應的圖片的座標點
    @classmethod
    def matchImg(cls, imgobj, confidence=0.5):
        imgsrc = 'screen.png'
        imsrc = ac.imread(imgsrc)
        imobj = ac.imread(imgobj)
        match_result = ac.find_template(imsrc, imobj, confidence)
        print(match_result)
        x = match_result['result'][0]
        y = match_result['result'][1]
        # 當前x y為識別圖片的中心點，可以進行直接點選
        return x, y

    # 點選對應的滑鼠
    @classmethod
    def click(cls, imgobj):
        x, y = MouseToClick.matchImg(imgobj)
        mouse = PyMouse()
        print(int(x), int(y))
        mouse.click(int(x), int(y))

    # 輸入單個鍵盤   enter等等
    @classmethod
    def oneKey(cls, key):
        keyboard = {'*': '106', '+': '107', '-': '109', '.': '110', '/': '111', 'F1': '112', 'F2': '113', 'F3': '114',
                    'F4': '115', 'F5': '116', 'F6': '117', 'F7': '118', 'F8': '119', 'F9': '120', 'F10': '121',
                    'F11': '122', 'F12': '123', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70',
                    'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79',
                    'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88',
                    'Y': '89', 'Z': '90', '0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54',
                    '7': '55', '8': '56', '9': '57', 'BACKSPACE': '8', 'TAB': '9', 'CLEAR': '12', 'ENTER': '13',
                    'SHIFT': '16', 'CTRL': '17', 'ALT': '18', 'CAPSLOCK': '20', 'ESC': '27', 'SPACEBAR': '32',
                    'PAGEUP': '33', 'PAGEDOWN': '34', 'END': '35', 'LEFT': '37', 'UP': '38', 'HOME': '36',
                    'RIGHT': '39', 'DOWN': '40', 'INSERT': '45', 'DELETE': '46', 'HELP': '47', 'NUMLOCK': '144'}
        key = key.upper()
        win32api.keybd_event(int(keyboard[key]), 0, 0, 0)
        win32api.keybd_event(int(keyboard[key]), 0, win32con.KEYEVENTF_KEYUP, 0)

    # 輸入兩個鍵盤  ctrl+a等等
    @classmethod
    def twoKey(cls, keyone, keytwo):
        keyboard = {'*': '106', '+': '107', '-': '109', '.': '110', '/': '111', 'F1': '112', 'F2': '113', 'F3': '114',
                    'F4': '115', 'F5': '116', 'F6': '117', 'F7': '118', 'F8': '119', 'F9': '120', 'F10': '121',
                    'F11': '122', 'F12': '123', 'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70',
                    'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76', 'M': '77', 'N': '78', 'O': '79',
                    'P': '80', 'Q': '81', 'R': '82', 'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88',
                    'Y': '89', 'Z': '90', '0': '48', '1': '49', '2': '50', '3': '51', '4': '52', '5': '53', '6': '54',
                    '7': '55', '8': '56', '9': '57', 'BACKSPACE': '8', 'TAB': '9', 'CLEAR': '12', 'ENTER': '13',
                    'SHIFT': '16', 'CTRL': '17', 'ALT': '18', 'CAPSLOCK': '20', 'ESC': '27', 'ESC': '27',
                    'SPACEBAR': '32', 'PAGEUP': '33', 'PAGEDOWN': '34', 'END': '35', 'LEFT': '37', 'UP': '38',
                    'HOME': '36', 'RIGHT': '39', 'DOWN': '40', 'INSERT': '45', 'DELETE': '46', 'HELP': '47',
                    'NUMLOCK': '144'}
        keyone = keyone.upper()
        keytwo = keytwo.upper()
        win32api.keybd_event(int(keyboard[keyone]), 0, 0, 0)
        win32api.keybd_event(int(keyboard[keytwo]), 0, 0, 0)
        win32api.keybd_event(int(keyboard[keytwo]), 0, win32con.KEYEVENTF_KEYUP, 0)
        win32api.keybd_event(int(keyboard[keyone]), 0, win32con.KEYEVENTF_KEYUP, 0)