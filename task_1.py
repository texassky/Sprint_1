# Исходная строка
raw_string = '1h 45m,360s,25m,30m 120s,2h 60s'

# Заменяем пробелы запятыми и разбиваем строку на список
time_values = raw_string.replace(' ', ',').split(',')

# Счетчик минут
minutes = 0

# Преобразуем в цикле каждое временное значение из списка time_values
for i in time_values:
    # Переводим часы в минуты и добавляем к счетчику
    if 'h' in i:
        number = i.split('h')
        minutes += int(number[0])*60

    # Добавляем минуты к счетчику    
    elif 'm' in i:
        number = i.split('m')
        minutes += int(number[0])

    # Переводим секунды в минуты и добавляем к счетчику    
    elif 's' in i:
        number = i.split('s')
        minutes += int(number[0])//60

# Выводим итог
print('Общее количество минут:', minutes)