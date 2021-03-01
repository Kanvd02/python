# ЗАДАНИЕ 1
#
# Человеко-ориентированное представление интервала времени
# Спросить у пользователя размер интервала (в секундах). Вывести на экран строку в зависимости от размера интервала:
#
# 1) до минуты: <s> сек;
# 2) до часа: <m> мин <s> сек;
# 3) до суток: <h> час <m> мин <s> сек;
# 4) сутки или больше: <d> дн <h> час <m> мин <s> сек
#
# Например, если пользователь введет 4567 секунд, вывести:
# 1 час 16 мин 7 сек

seconds_in_days = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

seconds = int(input("Приветствую! Введите количество секунд: "))

days = seconds // seconds_in_days
seconds = seconds - (days * seconds_in_days)

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print("{0:.0f} дней, {1:.0f} часов, {2:.0f} минут, {3:.0f} секунд.".format(
    days, hours, minutes, seconds))

