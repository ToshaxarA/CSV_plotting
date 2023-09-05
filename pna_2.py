import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

# Функция для чтения данных из CSV файла и извлечения числовых данных
def read_data(filename):
    data = pd.read_csv(filename, skiprows=7, skipfooter=1, engine='python')
    data = data[data.iloc[:, 0] != 'END']
    freq = data.iloc[:, 0].astype(float)
    s11_mag = data.iloc[:, 1].astype(float)
    s11_deg = data.iloc[:, 2].astype(float)
    s12_mag = data.iloc[:, 3].astype(float)
    s12_deg = data.iloc[:, 4].astype(float)
    s21_mag = data.iloc[:, 5].astype(float)
    s21_deg = data.iloc[:, 6].astype(float)
    s22_mag = data.iloc[:, 7].astype(float)
    s22_deg = data.iloc[:, 8].astype(float)
    return freq, s11_mag, s11_deg, s12_mag, s12_deg, s21_mag, s21_deg, s22_mag, s22_deg

# Чтение данных из двух CSV файлов
freq1, s11_mag1, s11_deg1, s12_mag1, s12_deg1, s21_mag1, s21_deg1, s22_mag1, s22_deg1 = read_data('S11.csv')  # Первый файл
freq2, s11_mag2, s11_deg2, s12_mag2, s12_deg2, s21_mag2, s21_deg2, s22_mag2, s22_deg2 = read_data('S21 EH(2).csv') # Второй файл

# Частота, на которой нужно провести вертикальную линию (в Гц)
vertical_line_freq = 13.56e6

# Создание рисунка для MAG в dB на линейной шкале
fig_mag, axes_mag = plt.subplots(nrows=2, ncols=2, figsize=(12, 7))

# Построение графиков для MAG в dB на линейной шкале из первого файла
axes_mag[0, 0].plot(freq1, 20 * np.log10(s11_mag1), label='S11(MAG) (dB) - Loop')
axes_mag[0, 1].plot(freq1, 20 * np.log10(s12_mag1), label='S12(MAG) (dB) - Loop')
axes_mag[1, 0].plot(freq1, 20 * np.log10(s21_mag1), label='S21(MAG) (dB) - Loop')
axes_mag[1, 1].plot(freq1, 20 * np.log10(s22_mag1), label='S22(MAG) (dB) - Loop')

# Построение графиков для MAG в dB на линейной шкале из второго файла
axes_mag[0, 0].plot(freq2, 20 * np.log10(s11_mag2), label='S11(MAG) (dB) - EH antenna', linestyle='--')
axes_mag[0, 1].plot(freq2, 20 * np.log10(s12_mag2), label='S12(MAG) (dB) - EH antenna', linestyle='--')
axes_mag[1, 0].plot(freq2, 20 * np.log10(s21_mag2), label='S21(MAG) (dB) - EH antenna', linestyle='--')
axes_mag[1, 1].plot(freq2, 20 * np.log10(s22_mag2), label='S22(MAG) (dB) - EH antenna', linestyle='--')

# Добавление вертикальной линии на каждом графике MAG
for ax in axes_mag.flat:
    ax.axvline(x=vertical_line_freq, color='r', linestyle='--', label='13.56 MHz', linewidth=0.9)

# Добавление легенды к каждому графику MAG
for ax in axes_mag.flat:
    ax.legend(loc='lower right')

# Изменение формата представления научной нотации на осях X и Y
for ax in axes_mag.flat:
    ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(axis='both', style='plain')  # Изменение формата подписей на линейный

# Установка кратных 10 значениям и подписей на оси X, начиная с 10 МГц
for ax in axes_mag.flat:
    ax.set_xticks(np.arange(0e6, 51e6, 10e6))
    ax.set_xticklabels([f'{int(x / 1e6)}' for x in np.arange(0e6, 51e6, 10e6)])

# Добавление описаний осей для графиков MAG в dB
for i in range(2):
    for j in range(2):
        axes_mag[i, j].set_xlabel('Frequency, MHz')
        axes_mag[i, j].grid(True)
        if j == 0:
            axes_mag[i, j].set_ylabel('Magnitude (dB)')

# Установка общего заголовка для графиков MAG в dB
fig_mag.suptitle('S-Parameters (MAG)')

# Регулировка расстояния между сабплотами для графиков MAG в dB
plt.tight_layout()

# Создание рисунка для DEG
fig_deg, axes_deg = plt.subplots(nrows=2, ncols=2, figsize=(12, 7))

# Построение графиков для DEG из первого файла
axes_deg[0, 0].plot(freq1, s11_deg1, label='S11(DEG) - Loop')
axes_deg[0, 1].plot(freq1, s12_deg1, label='S12(DEG) - Loop')
axes_deg[1, 0].plot(freq1, s21_deg1, label='S21(DEG) - Loop')
axes_deg[1, 1].plot(freq1, s22_deg1, label='S22(DEG) - Loop')

# Построение графиков для DEG из второго файла
axes_deg[0, 0].plot(freq2, s11_deg2, label='S11(DEG) - EH antenna', linestyle='--')
axes_deg[0, 1].plot(freq2, s12_deg2, label='S12(DEG) - EH antenna', linestyle='--')
axes_deg[1, 0].plot(freq2, s21_deg2, label='S21(DEG) - EH antenna', linestyle='--')
axes_deg[1, 1].plot(freq2, s22_deg2, label='S22(DEG) - EH antenna', linestyle='--')

# Добавление вертикальной линии на каждом графике DEG
for ax in axes_deg.flat:
    ax.axvline(x=vertical_line_freq, color='r', linestyle='--', label='13.56 MHz', linewidth=0.9)

# Добавление легенды к каждому графику DEG
for ax in axes_deg.flat:
    ax.legend(loc='lower right')

# Изменение формата представления научной нотации на осях X
for ax in axes_deg.flat:
    ax.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
    ax.ticklabel_format(axis='x', style='plain')  # Изменение формата подписей на линейный

# Установка кратных 10 значениям и подписей на оси X, начиная с 10 МГц
for ax in axes_deg.flat:
    ax.set_xticks(np.arange(0e6, 51e6, 10e6))
    ax.set_xticklabels([f'{int(x / 1e6)}' for x in np.arange(0e6, 51e6, 10e6)])

# Добавление описаний осей для графиков DEG
for i in range(2):
    for j in range(2):
        axes_deg[i, j].set_xlabel('Frequency, MHz')
        axes_deg[i, j].grid(True)
        axes_deg[i, j].set_ylabel('Phase (deg)')

# Установка общего заголовка для графиков DEG
fig_deg.suptitle('S-Parameters (DEG)')

# Регулировка расстояния между сабплотами для графиков DEG
plt.tight_layout()

# Отображение рисунков
plt.show()
