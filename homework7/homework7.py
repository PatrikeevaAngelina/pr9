import random
numbers = random.sample(range(1, 20), 10) # Создаем случайный список чисел
print("Исходный список:", numbers)
a=numbers[-1]
numbers=numbers[:-1]
numbers.insert(0,a)
print("Список после сдвига:",numbers)
