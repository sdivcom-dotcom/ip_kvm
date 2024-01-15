import board
import digitalio
import busio
import time
import usb_hid
from adafruit_hid import keyboard

uart1 = busio.UART(tx=board.GP0, rx=board.GP1, baudrate=9600)
uart2 = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=9600)

kbd = keyboard.Keyboard(usb_hid.devices)

while True:
    data1 = uart1.readline(1)  # read up to 32 bytes
    data2 = uart2.readline(3)  # read up to 32 bytes
    
    print("DATA1 =",data1)
    print("DATA2 =",data2)
#Вверхний ряд
    if data1 == b'q':
        kbd.send(keyboard.Keycode.Q)
    elif data1 == b'w':
        kbd.send(keyboard.Keycode.W)
    elif data1 == b'e':
        kbd.send(keyboard.Keycode.E)
    elif data1 == b'r':
        kbd.send(keyboard.Keycode.R)
    elif data1 == b't':
        kbd.send(keyboard.Keycode.T)
    elif data1 == b'y':
        kbd.send(keyboard.Keycode.Y)
    elif data1 == b'u':
        kbd.send(keyboard.Keycode.U)
    elif data1 == b'i':
        kbd.send(keyboard.Keycode.I)
    elif data1 == b'o':
        kbd.send(keyboard.Keycode.O)
    elif data1 == b'p':
        kbd.send(keyboard.Keycode.P)
#Средний ряд2
    elif data1 == b'a':
        kbd.send(keyboard.Keycode.A)
    elif data1 == b's':
        kbd.send(keyboard.Keycode.S)
    elif data1 == b'd':
        kbd.send(keyboard.Keycode.D)
    elif data1 == b'f':
        kbd.send(keyboard.Keycode.F)
    elif data1 == b'g':
        kbd.send(keyboard.Keycode.G)
    elif data1 == b'h':
        kbd.send(keyboard.Keycode.H)
    elif data1 == b'j':
        kbd.send(keyboard.Keycode.J)
    elif data1 == b'k':
        kbd.send(keyboard.Keycode.K)
    elif data1 == b'l':
        kbd.send(keyboard.Keycode.L)
#Нижний ряд
    elif data1 == b'z':
        kbd.send(keyboard.Keycode.Z)
    elif data1 == b'x':
        kbd.send(keyboard.Keycode.X)
    elif data1 == b'c':
        kbd.send(keyboard.Keycode.C)
    elif data1 == b'v':
        kbd.send(keyboard.Keycode.V)
    elif data1 == b'b':
        kbd.send(keyboard.Keycode.B)
    elif data1 == b'n':
        kbd.send(keyboard.Keycode.N)
    elif data1 == b'm':
        kbd.send(keyboard.Keycode.M)
#Цифры
    elif data1 == b'0':
        kbd.send(keyboard.Keycode.ZERO)
    elif data1 == b'1':
        kbd.send(keyboard.Keycode.ONE)
    elif data1 == b'2':
        kbd.send(keyboard.Keycode.TWO)
    elif data1 == b'3':
        kbd.send(keyboard.Keycode.THREE)
    elif data1 == b'4':
        kbd.send(keyboard.Keycode.FOUR)
    elif data1 == b'5':
        kbd.send(keyboard.Keycode.FIVE)
    elif data1 == b'6':
        kbd.send(keyboard.Keycode.SIX)
    elif data1 == b'7':
        kbd.send(keyboard.Keycode.SEVEN)
    elif data1 == b'8':
        kbd.send(keyboard.Keycode.EIGHT)
    elif data1 == b'9':
        kbd.send(keyboard.Keycode.NINE)
#Кнопки специальные
    elif data1 == b'\r':
        kbd.send(keyboard.Keycode.ENTER)
    elif data1 == b'\x1b':
        kbd.send(keyboard.Keycode.ESCAPE)
    elif data1 == b'\x7f':
        kbd.send(keyboard.Keycode.BACKSPACE)
    elif data1 == b'\t':
        kbd.send(keyboard.Keycode.TAB)
    elif data1 == b' ':
        kbd.send(keyboard.Keycode.SPACEBAR)
#Спецсимволы
    elif data1 == b'-':
        kbd.send(keyboard.Keycode.MINUS)
    elif data1 == b'-':
        kbd.send(keyboard.Keycode.PLUS)
    elif data1 == b'=':
        kbd.send(keyboard.Keycode.EQUALS)
    elif data1 == b'[':
        kbd.send(keyboard.Keycode.LEFT_BRACKET)
    elif data1 == b']':
        kbd.send(keyboard.Keycode.RIGHT_BRACKET)
    elif data1 == b'\\':
        kbd.send(keyboard.Keycode.BACKSLASH)
    elif data1 == b';':
        kbd.send(keyboard.Keycode.SEMICOLON) 
    elif data1 == b"'":
        kbd.send(keyboard.Keycode.QUOTE)
    elif data1 == b'`':
        kbd.send(keyboard.Keycode.GRAVE_ACCENT)   
    elif data1 == b',':
        kbd.send(keyboard.Keycode.COMMA)
    elif data1 == b'.':
        kbd.send(keyboard.Keycode.PERIOD)
    elif data1 == b'/':
        kbd.send(keyboard.Keycode.FORWARD_SLASH)
    else:
        pass
#Стрелки
    if data2 == b'\x1b[C':
        kbd.send(keyboard.Keycode.RIGHT_ARROW)    
    elif data2 == b'\x1b[D':
        kbd.send(keyboard.Keycode.LEFT_ARROW)
    elif data2 == b'\x1b[B':
        kbd.send(keyboard.Keycode.DOWN_ARROW)
    elif data2 == b'\x1b[A':
        kbd.send(keyboard.Keycode.UP_ARROW)
#F клавиавишы
    elif data2 == b'1':
        kbd.send(keyboard.Keycode.F1)   
    elif data2 == b'2':
        kbd.send(keyboard.Keycode.F2) 
    elif data2 == b'3':
        kbd.send(keyboard.Keycode.F3)   
    elif data2 == b'4':
        kbd.send(keyboard.Keycode.F4) 
    elif data2 == b'5':
        kbd.send(keyboard.Keycode.F5)   
    elif data2 == b'6':
        kbd.send(keyboard.Keycode.F6) 
    elif data2 == b'7':
        kbd.send(keyboard.Keycode.F7)   
    elif data2 == b'8':
        kbd.send(keyboard.Keycode.F8) 
    elif data2 == b'9':
        kbd.send(keyboard.Keycode.F9)   
    elif data2 == b'q':
        kbd.send(keyboard.Keycode.F10) 
    elif data2 == b'w':
        kbd.send(keyboard.Keycode.F11)   
    elif data2 == b'e':
        kbd.send(keyboard.Keycode.F12)
    ##################
    elif data2 == b'a':
        kbd.send(keyboard.Keycode.CAPS_LOCK)
    elif data2 == b's':
        kbd.send(keyboard.Keycode.PRINT_SCREEN)
    elif data2 == b'd':
        kbd.send(keyboard.Keycode.SCROLL_LOCK)
    elif data2 == b'f':
        kbd.send(keyboard.Keycode.PAUSE) 
    elif data2 == b'g':
        kbd.send(keyboard.Keycode.INSERT) 
    elif data2 == b'h':
        kbd.send(keyboard.Keycode.HOME) 
    elif data2 == b'j':
        kbd.send(keyboard.Keycode.PAGE_UP) 
    elif data2 == b'k':
        kbd.send(keyboard.Keycode.DELETE)
    elif data2 == b'l':
        kbd.send(keyboard.Keycode.END)
    elif data2 == b'z':
        kbd.send(keyboard.Keycode.PAGE_DOWN)
    elif data2 == b'x':
        kbd.send(keyboard.Keycode.APPLICATION)
    elif data2 == b'c':
        kbd.send(keyboard.Keycode.CONTROL)   
    elif data2 == b'v':
        kbd.send(keyboard.Keycode.SHIFT) 
    elif data2 == b'b':
        kbd.send(keyboard.Keycode.ALT)
    else:
        pass

    # elif data1 == b'\x1b':
    #     kbd.send(keyboard.Keycode.POUND)


    
