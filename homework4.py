numbers = []
while True:
 a = input("Введите число, либо введите 'end' для завершения: ")
 if a == 'end':
  break
 elif a.isdigit():
  numbers.append(int(a))
 else:
  print("Некорректный ввод. Введите число или 'end'.")
chet = 0
nechet = 0
for number in numbers:
 if number % 2 == 0:
  chet += 1
 else:
  nechet += 1
print(f"Количество четных элементов: {chet}")
print(f"Количество нечетных элементов: {nechet}")
