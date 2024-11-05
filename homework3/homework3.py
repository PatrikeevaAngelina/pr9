numbers = []
while True:
 a = input("Введите число, либо введите 'end' для завершения: ")
 if a == 'end':
  break
 elif a.isdigit():
  numbers.append(int(a))
 else:
  print("Некорректный ввод. Введите число или 'end'.")
print("Нечетные элементы списка:", end=" ")
for number in numbers:
 if number % 2 != 0:
  print(number, end=" ")