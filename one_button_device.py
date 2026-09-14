def how_many_times(message):
    if not type(message) == str:
        raise TypeError('Input must be a string')
    total = 0

    for char in message:
        if char != ' ':
            if not ('a' <= char <= 'z'):
                raise ValueError('String must contain only lowercase letters or spaces.')
            total += ord(char) - ord('a') + 1

    return total # Пример использования
message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")