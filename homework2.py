a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if a > b:
  a, b = b, a
squares = []
for i in range(int(a)+1, int(b)):
  squares.append(i * i)
print(f"Список квадратов: {squares}")
