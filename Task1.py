# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

import math
dist1 = int(input("Введите расстояние за день: "))
dist2 = int(input("Введите расстояние для искомого времени: "))

# print(f"Дней потребуется: {int(dist2 / dist1)}")
# print(f"Дней потребуется: {round(dist2 / dist1, 1)}")

print(f"Дней потребуется: {math.ceil(dist2 / dist1)}")




