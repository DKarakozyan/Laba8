import numpy as np
import matplotlib.pyplot as plt

# формируем и рисуем массив нормального распределения чисел:
mean = 3 # мат.ожидание
sigma = 1.6 # СКО
N = 174 # длина массива
massive_normal = np.random.normal(mean,sigma,N)

# формируем и рисуем массив с синусоидальным сигналом 1:
ampl = 1 # амплитуда сигнала
f0 = 16 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
fd = N/max_limit_x # частота дискретизации, отсчётов в секунду
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x1 = ampl * np.sin(f0 * t)
massive_sin1 = np.sin(x1)

plt.figure(1)
plt.plot(massive_sin1)
plt.grid("on") #сетка на графике

# Приведение отчётов к частотам (для синусоидального сигнала)
M = 4*N
f_range = np.zeros(M)
for smp_ref in range(-int(M/2), int(M/2)):
    f_range[smp_ref] = (smp_ref / M)*fd;
# выполняем прямое преобразование Фурье
# первый аргумент функции fft - массив с исходным сигналом
# второй аргумент функции fft - длина выходного массива спектра
fft_result = np.fft.fft(massive_sin1, M)/N
# полученный спектр - комплексный, график должен содержать только его модуль
# т.е. амплитудный спектр
mod_fftshift_result = abs(fft_result)
# рисуем полученный массив
plt.figure(2)
plt.plot(f_range, mod_fftshift_result)
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

# формируем и рисуем массив с синусоидальным сигналом 3:
ampl = 1 # амплитуда сигнала
f0 = 0 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x3 = ampl * np.sin(f0 * t)
massive_sin3 = np.sin(x3)

# формируем и рисуем массив с синусоидальным сигналом 4:
ampl = 4 # амплитуда сигнала
f0 = 2 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x4 = ampl * np.sin(f0 * t)
massive_sin4 = np.sin(x4)

# формируем и рисуем массив с синусоидальным сигналом 5:
ampl = 5 # амплитуда сигнала
f0 = 8 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x5 = ampl * np.sin(f0 * t)
massive_sin5 = np.sin(x5)

# формируем и рисуем массив с синусоидальным сигналом 6:
ampl = 8 # амплитуда сигнала
f0 = 9 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x6 = ampl * np.sin(f0 * t)
massive_sin6 = np.sin(x6)

# формируем и рисуем массив с синусоидальным сигналом 7:
ampl = 9 # амплитуда сигнала
f0 = 11 # частота сигнала
min_limit_x = 0 # наименьшее значение оси x
max_limit_x = 2*np.pi # набольшее значение оси x
N = 174 # длина массива
t = np.linspace(min_limit_x, max_limit_x, N) # создаём ось
x7 = ampl * np.sin(f0 * t)
massive_sin7 = np.sin(x7)

Total_x= x1+x2+x3+x4+x5+x6+x7
massive_sin_all = np.sin(Total_x)
plt.figure(3)
plt.plot(massive_sin_all)
plt.grid("on") #сетка на графике

# Приведение отчётов к частотам (для смеси синусоидальных сигналов)
M = 4*N
f_range = np.zeros(M)
for smp_ref in range(-int(M/2), int(M/2)):
    f_range[smp_ref] = (smp_ref / M)*fd;
# выполняем прямое преобразование Фурье
# первый аргумент функции fft - массив с исходным сигналом
# второй аргумент функции fft - длина выходного массива спектра
fft_result = np.fft.fft(massive_sin_all, M)/N
# полученный спектр - комплексный, график должен содержать только его модуль
# т.е. амплитудный спектр
mod_fftshift_result = abs(fft_result)
# рисуем полученный массив
plt.figure(4)
plt.plot(f_range, mod_fftshift_result)
plt.grid("on") #сетка на графике

# Аддитивная смесь
additive_mixture = Total_x + massive_normal
plt.figure(5)
plt.plot(additive_mixture)
plt.grid("on") #сетка на графике

# Приведение отчётов к частотам (для смеси синусоидальных сигналов)
M = 4*N
f_range = np.zeros(M)
for smp_ref in range(-int(M/2), int(M/2)):
    f_range[smp_ref] = (smp_ref / M)*fd;
# выполняем прямое преобразование Фурье
# первый аргумент функции fft - массив с исходным сигналом
# второй аргумент функции fft - длина выходного массива спектра
fft_result = np.fft.fft(additive_mixture, M)/N
# полученный спектр - комплексный, график должен содержать только его модуль
# т.е. амплитудный спектр
mod_fftshift_result = abs(fft_result)
# рисуем полученный массив
plt.figure(6)
plt.plot(f_range, mod_fftshift_result)
plt.grid("on") #сетка на графике

a4h = np.zeros(M)
# резонансная частота фильтра в Гц
freq_rez = 20
# полоса пропускания фильтра в Гц 
polosa = 20

# нижняя граница полосы пропускания фильтра в Гц
min_a4h_freq = freq_rez - int(polosa/2)
# верхняя граница полосы пропускания фильтра в Гц
max_a4h_freq = freq_rez + int(polosa/2)

# в пределах полосы пропускания АЧХ фльтра пропускает сигнал без усиления
# за пределами полосы не пропускает вообще
for smp_ref in range(-int(M/2), int(M/2)):
    if (f_range[smp_ref] > min_a4h_freq):
        if (f_range[smp_ref] < max_a4h_freq):
            a4h[smp_ref] = 1
    if (f_range[smp_ref] < -min_a4h_freq):
        if (f_range[smp_ref] > -max_a4h_freq):
            a4h[smp_ref] = 1

# рисуем полученную АЧХ фильтра
plt.figure(7)
plt.plot(f_range, a4h)
plt.grid("on") #сетка на графике

filtered_add_smes_spektr = a4h*fft_result
filtered_add_smes = N*np.fft.ifft(filtered_add_smes_spektr)

# требуется взять количество отсчётов, равное количеству в исходном массиве:
invert_fft_mas_len = int(len(filtered_add_smes)*N/M)
# рисуем полученный массив
plt.figure(8)
plt.plot(t, filtered_add_smes[0:invert_fft_mas_len])
plt.grid("on") #сетка на графике

