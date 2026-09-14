'''while True:
    name = input('Enter your name: ')
    if name == 'Stop':
        break
    else:
        age = input(f'Hello, {name}, input your age: ')
    print(f' You are {name} with age {age} yrs old')'''
'''for i in range(5):
    if i == 3:
        break
        print("Готово") 
    else:
        print(i)'''

'''num = 3

match num:
    case 1:
        print(1)
    case 4:
        print(4)
    case _:
        print(None)
'''
'''
for i in range(7):
    match i:
        case 0:
            day = 'Пн'
        case 1:
            day =  'Вт'
        case 2:
            day =  'Ср'
        case 3:
            day = 'Чт'
        case 4:
            day =  'Пт'
        case 5:
            day = 'Сб'
        case 6:
            day = 'Вс'

    match i:
        case 5 | 6:
            print(f'{day} - выходной день')
        case _:
            print(f'{day} - будний день')'''
'''
command = input("Введите команду (start, stop, help): ")

match command:
    case "start":
        print("Система запускается...")
    case "stop":
        print("Система выключается.")
    case "help":
        print("Доступные команды: start, stop, help")
    case _:
        print("Неизвестная команда.")'''
