import serial
import time

port_1 = "/dev/ttyUSB0"
port_2 = "/dev/ttyUSB1"
baud = 9600

def write_com_action(port, data):
    ser = serial.Serial(port, baudrate=baud, timeout=1)
    ser.write(data)
    time.sleep(1)
    ser.close()


def response_spec_button(string):
    if string == "Key.f1":
        data = b'1'
        write_com_action(port_1, data)
    elif string == "Key.f2":
        data = b'2'
        write_com_action(port_1, data)
    elif string == "Key.f3":
        data = b'3'
        write_com_action(port_1, data)
    elif string == "Key.f4":
        data = b'4'
        write_com_action(port_1, data)
    elif string == "Key.f5":
        data = b'5'
        write_com_action(port_1, data)
    elif string == "Key.f6":
        data = b'6'
        write_com_action(port_1, data)
    elif string == "Key.f7":
        data = b'7'
        write_com_action(port_1, data)
    elif string == "Key.f8":
        data = b'8'
        write_com_action(port_1, data)
    elif string == "Key.f9":
        data = b'9'
        write_com_action(port_1, data)
    elif string == "Key.f10":
        data = b'q'
        write_com_action(port_1, data)
    elif string == "Key.f11":
        data = b'w'
        write_com_action(port_1, data)
    elif string == "Key.f12":
        data = b'e'
        write_com_action(port_1, data)
    elif string == "Key.caps":
        data = b'a'
        write_com_action(port_1, data)     
    elif string == "Key.print_screen":
        data = b's'
        write_com_action(port_1, data)
    elif string == "Key.scroll_lock":
        data = b'd'
        write_com_action(port_1, data)
    elif string == "Key.pause":
        data = b'f'
        write_com_action(port_1, data)
    elif string == "Key.insert":
        data = b'g'
        write_com_action(port_1, data)  
    elif string == "Key.home":
        data = b'h'
        write_com_action(port_1, data)
    elif string == "Key.page_up":
        data = b'j'
        write_com_action(port_1, data)
    elif string == "Key.delete":
        data = b'k'
        write_com_action(port_1, data)
    elif string == "Key.end":
        data = b'l'
        write_com_action(port_1, data)
    elif string == "Key.page_down":
        data = b'z'
        write_com_action(port_1, data)
    elif string == "Key.application":
        data = b'x'
        write_com_action(port_1, data)
    elif string == "Key.control":
        data = b'c'
        write_com_action(port_1, data)
    elif string == "Key.shift":
        data = b'v'
        write_com_action(port_1, data)
    elif string == "Key.alt":
        data = b'b'
        write_com_action(port_1, data)
    elif string == "Key.right":
        data = b'\x1b[C'
        write_com_action(port_1, data)
    elif string == "Key.left":
        data = b'\x1b[D'
        write_com_action(port_1, data)
    elif string == "Key.up":
        data = b'\x1b[A'
        write_com_action(port_1, data)
    elif string == "Key.down":
        data = b'\x1b[B'
        write_com_action(port_1, data)
    elif string == "Key.enter":
        data = '\r'
        write_button(data)
    elif string == "Key.escape":
        data = '\x1b'
        write_button(data)
    elif string == "Key.backspace":
        data = '\x7f'
        write_button(data)
    elif string == "Key.tab":
        data = '\t'
        write_button(data)
    elif string == "Key.space":
        data = ' '
        write_button(data)  
    else:
        pass

def write_button(string):
    data = string
    data = string.encode()
    write_com_action(port_2, data)
