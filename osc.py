import matplotlib.pyplot as plt
import csv

def read_data(filename):
    X = []
    Y = []

    with open(filename, 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')
        
        # Пропускаем строки, которые нельзя преобразовать в числа
        for row in plotting:
            if len(row) == 2:
                try:
                    X.append(float(row[0]))
                    Y.append(float(row[1]))
                except ValueError:
                    pass

    return X, Y

# Имя файла для анализа
filename = 'scope_6.csv'
title = 'Full signal'

# Чтение данных из файла
X, Y = read_data(filename)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(X, Y)
plt.xlabel('Time, sec')
plt.ylabel('Voltage on loop antenna, V')
plt.title(f'{title}')
plt.grid(True)
plt.show()
