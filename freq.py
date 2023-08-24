import csv
import numpy as np
import pandas as pd

# Загрузка данных из CSV файла
file_path = 'scope_2_1.csv'  # путь к CSV файлу
data = []  # список для хранения данных

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    next(csv_reader)  # пропуск заголовка, если он есть
    for row in csv_reader:
        time, amplitude = map(float, row)
        data.append((time, amplitude))

# Преобразование данных в массив NumPy и создание DataFrame
data_array = np.array(data)
data_frame = pd.DataFrame(data_array, columns=['time', 'amplitude'])

# Выбор временного промежутка
start_time = 0.000  # начальное время в выбранном промежутке
end_time = 0.0003    # конечное время в выбранном промежутке

selected_data = data_frame[(data_frame['time'] >= start_time) & (data_frame['time'] <= end_time)]

# Определение порогового значения
threshold = 0.1

# Подсчет пересечений амплитуды через пороговое значение
zero_crossings = 0
prev_amplitude = selected_data['amplitude'].iloc[0]

for current_amplitude in selected_data['amplitude'][1:]:
    if prev_amplitude < threshold and current_amplitude >= threshold:
        zero_crossings += 1
    prev_amplitude = current_amplitude

# Вычисление среднего интервала между периодами колебаний
mean_period_interval = (selected_data['time'].iloc[-1] - selected_data['time'].iloc[0]) / zero_crossings

# Вычисление частоты колебаний
frequency = 1.0 / mean_period_interval

frequency_mhz = frequency / 1_000_000  # Перевод Гц в МГц

print("Number of Periods:", zero_crossings)
print("Frequency (MHz):", frequency_mhz)

