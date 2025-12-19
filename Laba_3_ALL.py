import numpy as np
# служебное слово as означает, что мы можем обозвать подключаемый
# нами модуль так, как мы захотим, например np вместо numpy
import matplotlib.pyplot as plt
# формируем и рисуем массив нормального распределения чисел:
mean = 3 # мат.ожидание
sigma = 1.6 # СКО
N = 174 # длина массива
massive_normal = np.random.normal(mean,sigma,N)
# рисуем полученный массив
plt.figure(1)
plt.plot(massive_normal)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 1:
ampl = 1 # амплитуда сигнала
f0 = 16 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x1 = ampl * np.sin(f0 * t)
massive_sin1 = np.sin(x1)
# рисуем полученный массив
plt.figure(2)
plt.plot(massive_sin1)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 2:
ampl = 2 # амплитуда сигнала
f0 = 3 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x2 = ampl * np.sin(f0 * t)
massive_sin2 = np.sin(x2)
# рисуем полученный массив
plt.figure(3)
plt.plot(massive_sin2)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 3:
ampl = 1 # амплитуда сигнала
f0 = 0 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x3 = ampl * np.sin(f0 * t)
massive_sin3 = np.sin(x3)
# рисуем полученный массив
plt.figure(4)
plt.plot(massive_sin3)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 4:
ampl = 4 # амплитуда сигнала
f0 = 2 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x4 = ampl * np.sin(f0 * t)
massive_sin4 = np.sin(x4)
# рисуем полученный массив
plt.figure(5)
plt.plot(massive_sin4)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 5:
ampl = 5 # амплитуда сигнала
f0 = 8 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x5 = ampl * np.sin(f0 * t)
massive_sin5 = np.sin(x5)
# рисуем полученный массив
plt.figure(6)
plt.plot(massive_sin5)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 6:
ampl = 8 # амплитуда сигнала
f0 = 9 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x6 = ampl * np.sin(f0 * t)
massive_sin6 = np.sin(x6)
# рисуем полученный массив
plt.figure(7)
plt.plot(massive_sin6)
plt.grid("on") #сетка на графике

# формируем и рисуем массив с синусоидальным сигналом 7:
ampl = 9 # амплитуда сигнала
f0 = 11 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x7 = ampl * np.sin(f0 * t)
massive_sin7 = np.sin(x7)
# рисуем полученный массив
plt.figure(8)
plt.plot(massive_sin7)
plt.grid("on") #сетка на графике

Total_x= x1+x2+x3+x4+x5+x6+x7
massive_sin_all = np.sin(Total_x)
plt.figure(9)
plt.plot(massive_sin_all)
plt.grid("on") #сетка на графике

# Аддитивная смесь
additive_mixture = Total_x + massive_normal
plt.figure(10)
plt.plot(additive_mixture)
plt.grid("on") #сетка на графике
# Мультипликативная смесь
multiplicative_mixture = Total_x * massive_normal

# Вычисление спектров с помощью numpy FFT
spectrum_additive = np.fft.fft(additive_mixture)
spectrum_signal = np.fft.fft(Total_x)
spectrum_noise = np.fft.fft(massive_normal)
spectrum_multiplicative = np.fft.fft(multiplicative_mixture)

# Частотная ось
freqs = np.fft.fftfreq(N, d=(2*np.pi)/N)

# Вычисление амплитудных спектров (модуль)
amp_spectrum_additive = np.abs(spectrum_additive)
amp_spectrum_signal = np.abs(spectrum_signal)
amp_spectrum_noise = np.abs(spectrum_noise)
amp_spectrum_multiplicative = np.abs(spectrum_multiplicative)

# Фазовые спектры
phase_spectrum_additive = np.angle(spectrum_additive)
phase_spectrum_signal = np.angle(spectrum_signal)

# Обратное преобразование Фурье
reconstructed_additive = np.fft.ifft(spectrum_additive)
reconstructed_multiplicative = np.fft.ifft(spectrum_multiplicative)
reconstructed_signal = np.fft.ifft(spectrum_signal)
reconstructed_noise = np.fft.ifft(spectrum_noise)

# Построение графиков
plt.figure(figsize=(15, 10))

# График 1: Временные сигналы
plt.subplot(4, 3, 1)
plt.plot(t, additive_mixture, 'b-', label='Аддитивная смесь', linewidth=1)
plt.plot(t, multiplicative_mixture, 'r-', label='Мультипликативная смесь', alpha=0.7, linewidth=1)
plt.title('Временные области сигналов')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# График 2: Отдельные компоненты
plt.subplot(4, 3, 2)
plt.plot(t, Total_x, 'g-', label='Чистый сигнал', linewidth=1)
plt.plot(t, massive_normal, 'm-', label='Шум', alpha=0.7, linewidth=1)
plt.title('Отдельные компоненты')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# График 3: Амплитудный спектр аддитивной смеси
plt.subplot(4, 3, 3)
plt.plot(freqs[:N//2], amp_spectrum_additive[:N//2], 'b-', linewidth=1)
plt.title('Спектр аддитивной смеси (амплитуда)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)

# График 4: Амплитудный спектр сигнала
plt.subplot(4, 3, 4)
plt.plot(freqs[:N//2], amp_spectrum_signal[:N//2], 'g-', linewidth=1)
plt.title('Спектр чистого сигнала (амплитуда)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)

# График 5: Амплитудный спектр шума
plt.subplot(4, 3, 5)
plt.plot(freqs[:N//2], amp_spectrum_noise[:N//2], 'r-', linewidth=1)
plt.title('Спектр шума (амплитуда)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)

# График 6: Амплитудный спектр мультипликативной смеси
plt.subplot(4, 3, 6)
plt.plot(freqs[:N//2], amp_spectrum_multiplicative[:N//2], 'm-', linewidth=1)
plt.title('Спектр мультипликативной смеси (амплитуда)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)

# График 7: Фазовый спектр аддитивной смеси
plt.subplot(4, 3, 7)
plt.plot(freqs[:N//2], phase_spectrum_additive[:N//2], 'c-', linewidth=1)
plt.title('Спектр аддитивной смеси (фаза)')
plt.xlabel('Частота, Гц')
plt.ylabel('Фаза, рад')
plt.grid(True)

# График 8: Фазовый спектр сигнала
plt.subplot(4, 3, 8)
plt.plot(freqs[:N//2], phase_spectrum_signal[:N//2], 'y-', linewidth=1)
plt.title('Спектр чистого сигнала (фаза)')
plt.xlabel('Частота, Гц')
plt.ylabel('Фаза, рад')
plt.grid(True)

# График 9: Сравнение спектров
plt.subplot(4, 3, 9)
plt.plot(freqs[:N//2], amp_spectrum_signal[:N//2], 'g-', label='Сигнал', alpha=0.7, linewidth=1)
plt.plot(freqs[:N//2], amp_spectrum_noise[:N//2], 'r-', label='Шум', alpha=0.7, linewidth=1)
plt.plot(freqs[:N//2], amp_spectrum_additive[:N//2], 'b-', label='Аддитивная смесь', alpha=0.7, linewidth=1)
plt.title('Сравнение спектров (амплитуда)')
plt.xlabel('Частота, Гц')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# График 10: Восстановленные сигналы (обратное преобразование)
plt.subplot(4, 3, 10)
plt.plot(t, additive_mixture, 'b-', label='Исходная аддитивная смесь', alpha=0.7, linewidth=1)
plt.plot(t, np.real(reconstructed_additive), 'r--', label='Восстановленная', linewidth=2)
plt.title('Обратное преобразование Фурье\n(аддитивная смесь)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# График 11: Восстановленный сигнал
plt.subplot(4, 3, 11)
plt.plot(t, Total_x, 'g-', label='Исходный сигнал', alpha=0.7, linewidth=1)
plt.plot(t, np.real(reconstructed_signal), 'r--', label='Восстановленный', linewidth=2)
plt.title('Обратное преобразование Фурье\n(чистый сигнал)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

# График 12: Восстановленный шум
plt.subplot(4, 3, 12)
plt.plot(t, massive_normal, 'm-', label='Исходный шум', alpha=0.7, linewidth=1)
plt.plot(t, np.real(reconstructed_noise), 'r--', label='Восстановленный', linewidth=2)
plt.title('Обратное преобразование Фурье\n(шум)')
plt.xlabel('Время')
plt.ylabel('Амплитуда')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()