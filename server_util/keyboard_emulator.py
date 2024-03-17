from pynput import keyboard
from command_pi import write_button, response_spec_button


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        write_button(key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))
        response_spec_button(format(key)) 


def on_release(key):
    if key == keyboard.Key.home:
        return False
    else:
        pass


def read_keyboard():
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()

read_keyboard()