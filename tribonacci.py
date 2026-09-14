# этот код должен принимать на вход числа, а выводить в ответ числа трибоначи

def tribonacci(n):
    if isinstance(n, float):
        raise TypeError("Input must be an integer.")
    elif n < 0:
        raise TypeError("Input must be a non-negative integer.")
    else:
        if n == 0:
            return 1
        elif n <= 2:
            return 1
        else:
            a, b, c = 0, 1, 1
            for _ in range(3, n + 1):
                a, b, c = b, c, a + b + c
        return c
        
# Пример использования
n = int(input("Введите номер числа Трибоначчи: "))
result = tribonacci(n)
print(f"T({n}) = {result}")