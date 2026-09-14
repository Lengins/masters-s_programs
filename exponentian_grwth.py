def calculate_months_to_threshold(start, rate, threshold):
    if start >= threshold:
        return 0
    elif rate <= 0:
        raise ValueError ("Growth rate must be greater than 0.")
    elif start <= 0 or threshold <= 0:
        raise ValueError ("Start and threshold must be positive numbers.")
    else:
        i = 0
        while start < threshold:
            start = start * (rate/100+1)
            i += 1
        return i

# Пример использования
start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_months_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")