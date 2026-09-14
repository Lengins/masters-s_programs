def decimal_to_binary(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    elif num < 0:
        raise ValueError("Only non-negative integers are allowed.")
    elif num == 0:
        return "0"
    else:
        binary_str = ""
        while num != 0:
            binary_str = str(num % 2) + binary_str
            num //= 2
        return binary_str
# Пример использования
num = int(input("Введите десятичное число: "))
binary = decimal_to_binary(num)
print(f"Двоичное представление: {binary}")