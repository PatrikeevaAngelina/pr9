import random
numbers = random.sample(range(1, 20), 10) # Создаем случайный список чисел
print("Исходный список:", numbers)
min = numbers.index(min(numbers))
max= numbers.index(max(numbers))
numbers[min], numbers[max] = numbers[max], numbers[min]

print(f"Список после перестановки: {numbers}")

