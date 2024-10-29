import random
numbers = random.sample(range(1, 20), 15) # Создаем случайный список чисел
print("Исходный список:", numbers)
print("Элементы списка, большие предыдущего:", end=" ")
for i in range(1, len(numbers)):
 if numbers[i] > numbers[i - 1]:
  print(numbers[i], end=" ")
if numbers[-1] > numbers [0] :
 print(numbers[-1], end=" ")
