def triangle_type(trian1, trian2, trian3):
    if trian1 <= 0 or trian2 <= 0 or trian3 <= 0:
        return "Impossible triangle"
    if not (trian1 + trian2 > trian3 and
trian2 + trian3 > trian1 and
trian3 + trian1 > trian2):
        return "Impossible triangle"
    if trian1 == trian2 == trian3:
        return "Equilateral"
    elif trian1 == trian2 or trian2 == trian3 or trian3 == trian1:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
# Пример использования
a = float(input("Введите длину первой стороны: "))
b = float(input("Введите длину второй стороны: "))
c = float(input("Введите длину третьей стороны: "))

result = triangle_type(a, b, c)
print(f"Тип треугольника: {result}")

