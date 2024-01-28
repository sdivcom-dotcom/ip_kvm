import serial
import time

port = "/dev/ttyACM0"
baud = 9600

def write_com_action(data):
    ser = serial.Serial(port=port, baudrate=baud, timeout=10)
    ser.write(data)
    time.sleep(1)
    ser.close()


def read_com_action():
    try:
        ser = serial.Serial(port, baud)
        line = ser.readline().decode('utf-8').strip()
    except serial.SerialException as e:
        print(f"Ошибка при работе с COM-портом: {e}")
    finally:
        if ser.is_open:
            ser.close()
    return line


def step_kvm(val_step):
    data = b'r'
    i = 0
    while i < val_step:

        write_com_action(data)
        time.sleep(1)
        i = i + 1
    return i

      
def replase_server(main_command_number, val_read_file_number):
    main_command_number = int(main_command_number)
    val_read_file_number = int(val_read_file_number)
    if main_command_number == 4:
        if val_read_file_number < main_command_number:
            val_step = main_command_number - val_read_file_number
            step_kvm(val_step)
        else:
            print("ERROR!")
    elif main_command_number > val_read_file_number:
        val_step = main_command_number - val_read_file_number
        step_kvm(val_step)
    elif val_read_file_number > main_command_number:
        val_step = val_read_file_number - main_command_number
        step_kvm(val_step)
    elif val_read_file_number == 4:
        if main_command_number == 1:
            step_kvm(main_command_number)
        elif main_command_number == 2:
            step_kvm(main_command_number)
        elif main_command_number == 3:
            step_kvm(main_command_number)
        else:
            print("ERROR!")
    elif main_command_number == val_read_file_number:
        pass
    else:
        print("ERROR!")
