import matplotlib.pyplot as plt
import csv

def read_data(filename):
    X = []
    Y = []
    
    with open(filename, 'r') as datafile:
        plotting = csv.reader(datafile, delimiter=',')
        
        # Пропускаем заголовки и единицы измерения
        next(plotting)
        next(plotting)
        
        for ROWS in plotting:
            X.append(float(ROWS[0]))
            Y.append(float(ROWS[1]))
    
    return X, Y

# Список файлов, из которых нужно читать данные
filenames = ['scope_1_1.csv', 'scope_2_1.csv', 'scope_3_1.csv', 'scope_4_1.csv']
titles = ['Full signal', 'Strobe pulse #1', 'Strobe pulse #2', 'Strobe pulse #3']  # Заголовки для графиков

# Создание сетки для графиков 2x2
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), constrained_layout=True)

axes = axes.flatten()  # Преобразуем двумерный массив в плоский

# Построение графиков
for i, filename in enumerate(filenames):
    X, Y = read_data(filename)
    ax = axes[i]
    ax.plot(X, Y)
    
    # Добавляем пустую строку слева от заголовка для выравнивания
    title = f'  {titles[i]}'  
    ax.set_title(title, loc='right')  # Заголовок будет выровнен по правому краю
    
    # Размещаем подпись оси X внизу справа
    ax.xaxis.set_label_position('bottom')
    ax.set_xlabel('Time, sec')
    ax.set_ylabel('Voltage on loop antenna, arb.un')

# Убираем пустые графики, если есть менее 4 графиков
for i in range(len(filenames), 4):
    axes[i].axis('off')

# Увеличение интервала между графиками
plt.subplots_adjust(hspace=0.5)




# Список файлов, из которых нужно читать данные
filenames = ['scope_3_1.csv', 'scope_2_1.csv','scope_4_1.csv']
titles = ['Strobe pulse #2', 'Strobe pulse #1','Strobe pulse #3']  # Заголовки для графиков
colors = ['blue', 'green','red']  # Цвета для графиков

# Создание сетки для графиков
fig, ax = plt.subplots(figsize=(8, 6))

# Построение и наложение графиков
for i, filename in enumerate(filenames):
    X, Y = read_data(filename)
    ax.plot(X, Y, color=colors[i], label=titles[i])  # Используем соответствующий цвет
    ax.set_xlabel('Time, sec')
    ax.set_ylabel('Voltage on loop antenna, V')

# Добавляем легенду
ax.legend()

# Добавляем пустую строку слева от заголовка для выравнивания
title = f'Pulses length comparison'  
ax.set_title(title, loc='right')  # Заголовок будет выровнен по правому краю

# Отображение графиков
plt.tight_layout()
plt.show()