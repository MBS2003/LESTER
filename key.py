import pyautogui

def windows():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")

def window_next():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def one():
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def two():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def three():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def four():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def five():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def six():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def seven():
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")

def recent():
    pyautogui.keyDown("win")
    pyautogui.press("tab")
    pyautogui.keyUp("win")

def tab():
    pyautogui.press("tab")

def start_menu():
    pyautogui.press("win")

def enter():
    pyautogui.press("enter")

def space():
    pyautogui.press("space")

def down():
    pyautogui.press("down")

def right():
    pyautogui.press("right")

def left():
    pyautogui.press("left")

def up():
    pyautogui.press("up")

def settings():
    pyautogui.keyDown("win")
    pyautogui.press("i")
    pyautogui.keyUp("win")

def notification():
    pyautogui.keyDown("win")
    pyautogui.press("a")
    pyautogui.keyUp("win")

def search():
    pyautogui.keyDown("win")
    pyautogui.press("s")
    pyautogui.keyUp("win")

def show_desktop():
    pyautogui.keyDown("win")
    pyautogui.press("d")
    pyautogui.keyUp("win")
    
def gamebar():
    pyautogui.keyDown("win")
    pyautogui.press("g")
    pyautogui.keyUp("win")

def dict():
    pyautogui.keyDown("win")
    pyautogui.press("h")
    pyautogui.keyUp("win")

def lockpc():
    pyautogui.keyDown("win")
    pyautogui.press("l")
    pyautogui.keyUp("win")

def options():
    pyautogui.keyDown("win")
    pyautogui.press("x")
    pyautogui.keyUp("win")

def cortana():
    pyautogui.keyDown("win")
    pyautogui.press("c")
    pyautogui.keyUp("win")

def controll():
    pyautogui.keyDown("win")
    pyautogui.press("b")
    pyautogui.keyUp("win")

def minimize():
    pyautogui.keyDown("win")
    pyautogui.press("m")
    pyautogui.keyUp("win")

def run():
    pyautogui.keyDown("win")
    pyautogui.press("r")
    pyautogui.keyUp("win")

def taskbar():
    pyautogui.keyDown("win")
    pyautogui.press("t")
    pyautogui.keyUp("win")

def fullscreen():
    pyautogui.press("f11")

def media_full():
    pyautogui.press("f")

def scrollup():
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    pyautogui.scroll(50)
    
def scrolldown():
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)
    pyautogui.scroll(-50)

def close():
    pyautogui.keyDown("alt")
    pyautogui.press("f4")
    pyautogui.keyUp("alt")

def volumeup():
    pyautogui.press('volumeup')
    pyautogui.press('volumeup')

def volumedown():
    pyautogui.press('volumedown')
    pyautogui.press('volumedown')

def volume():
    pyautogui.press('volumemute')

def youtube_play_1():
    pyautogui.press('tab')
    pyautogui.press('enter')

def youtube_play_2():
    pyautogui.press('tab', presses=5)
    pyautogui.press('enter')

def youtube_play_3():
    pyautogui.press('tab', presses=9)
    pyautogui.press('enter')

def youtube_play_4():
    pyautogui.press('tab', presses=13)
    pyautogui.press('enter')

def youtube_play_5():
    pyautogui.press('tab', presses=17)
    pyautogui.press('enter')
    
def alignleft():
    pyautogui.keyDown("win")
    pyautogui.press("left")
    pyautogui.keyUp("win")

def alignright():
    pyautogui.keyDown("win")
    pyautogui.press("right")
    pyautogui.keyUp("win")

def alignup():
    pyautogui.keyDown("win")
    pyautogui.press("up")
    pyautogui.keyUp("win")

def aligndown():
    pyautogui.keyDown("win")
    pyautogui.press("down")
    pyautogui.keyUp("win")

def browser_back():
    pyautogui.press("browserback")

def browser_front():
    pyautogui.press("browserforward")

def browser_home():
    pyautogui.press("browserhome")

def browser_refresh():
    pyautogui.press("browserrefresh")

def playpause():
    pyautogui.press("playpause")

def f5():
    pyautogui.press("f5")

