from  command_mcu import replase_server
#from keyboard_emulator import read_keyboard
import time

def save_number_server(input):
    with open('number_server.txt', 'w+') as f:
        f.write(input)
        f.write("\n")
    f.close()


def read_number_server_earlier():
    with open('number_server.txt', 'r') as f:
        lines = f.readline()
        lines = lines.replace(' ','')
        lines = lines.replace('\n','')
        lines = lines.replace('\r','')
    f.close()
    return lines


while True:
    try:
        print("Выберите сервер для работы")
        print("Для этого введите команду 'display_x где x номер сервера'")
        print("Для выхода из режима нажмите клавишу home")
        main_command = input()
        main_command_less = main_command[0:8]
        main_command_number = main_command[8:9]
        main_command_number = int(main_command_number)
        if main_command_number < 5:
            main_command_number = str(main_command_number)
            if len(main_command_number) == 0:
                print("Введите команду заново")
                break
            else:
                pass
            if main_command_less == "display_":
                print("Выбран сервер =",main_command_number)
                val = read_number_server_earlier()
                replase_server(main_command_number, val)
                save_number_server(main_command_number)
                time.sleep(1)
                #read_keyboard()
                break
            else:
                print("Такой команды нет")
        else:
            print("Неверный номер сервера!")
    except KeyboardInterrupt:
        break
