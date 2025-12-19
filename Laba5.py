import numpy as np
import matplotlib.pyplot as plt

# ===================== ПАРАМЕТРЫ =====================
R_earth = 6371.21  # км, средний радиус Земли
beta_min_deg = 25   # градусов
beta_min = np.deg2rad(beta_min_deg)

# Параметры из таблицы для бригады 5
p_elliptic = [5, 5, 5, 5]
e_elliptic = [0.9, 0.5, 0.15, 0.3]

p_other = [2, 3, 3, 1]
e_other = [0, 1, 3, 1]

# ===================== ФУНКЦИИ =====================
def orbit_equation(p, e, theta):
    """Уравнение орбиты в полярных координатах"""
    return p / (1 + e * np.cos(theta))

def calculate_orbital_parameters(p, e):
    """Расчёт параметров орбиты"""
    if e < 1 and e >= 0:
        if e == 0:
            # Круговая орбита
            r = p
            h = r - R_earth
            return h, h
        else:
            # Эллиптическая орбита
            a = p / (1 - e**2)  # большая полуось
            r_perigee = a * (1 - e)  # перигей
            r_apogee = a * (1 + e)   # апогей
            h_perigee = r_perigee - R_earth
            h_apogee = r_apogee - R_earth
            return h_perigee, h_apogee
    else:
        # Парабола или гипербола (незамкнутые орбиты)
        return None, None

def zone_radius_angle(h):
    """Расчёт углового размера ЗР (θ) в радианах"""
    if h is None:
        return 0
    term = (R_earth * np.cos(beta_min)) / (R_earth + h)
    if abs(term) <= 1:
        theta_val = np.arccos(term) - beta_min
        return max(theta_val, 0)  # не отрицательный
    return 0

# ===================== 1. ПОСТРОЕНИЕ ОРБИТ =====================
# 1.1 Эллиптические орбиты
print("=== ЭЛЛИПТИЧЕСКИЕ ОРБИТЫ ===")

# Создаем фигуру для эллиптических орбит
fig1, axes1 = plt.subplots(2, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 10))
axes1 = axes1.flatten()

for i, (p, e) in enumerate(zip(p_elliptic, e_elliptic)):
    # Генерируем углы
    theta = np.linspace(-2*np.pi, 2*np.pi, 256)
    # Рассчитываем радиусы
    r = orbit_equation(p, e, theta)
    
    # Строим орбиту
    axes1[i].plot(theta, r, linewidth=2)
    axes1[i].set_title(f'Эллиптическая: p={p}, e={e}', pad=20)
    axes1[i].grid(True)
    
    # Рассчитываем параметры
    h_per, h_apo = calculate_orbital_parameters(p, e)
    if h_per is not None:
        print(f"Орбита {i+1}: высота перигея={h_per:.2f} км, высота апогея={h_apo:.2f} км")

plt.suptitle('Эллиптические орбиты (лабораторное задание)', fontsize=16)
plt.tight_layout()
plt.show()

# 1.2 Круги, параболы, гиперболы
print("\n=== КРУГОВЫЕ, ПАРАБОЛИЧЕСКИЕ, ГИПЕРБОЛИЧЕСКИЕ ОРБИТЫ ===")

# Создаем фигуру для разных типов орбит
fig2, axes2 = plt.subplots(2, 2, subplot_kw={'projection': 'polar'}, figsize=(12, 10))
axes2 = axes2.flatten()

for i, (p, e) in enumerate(zip(p_other, e_other)):
    # Определяем тип орбиты
    if e == 0:
        orbit_type = "Круговая"
        theta = np.linspace(0, 2*np.pi, 500)
    elif e == 1:
        orbit_type = "Параболическая"
        # Для параболы избегаем углов, где знаменатель = 0
        theta = np.linspace(-0.9*np.pi, 0.9*np.pi, 500)
    elif e > 1:
        orbit_type = "Гиперболическая"
        # Для гиперболы ограничиваем углы
        max_angle = np.arccos(-1/e) - 0.1  # немного меньше предельного угла
        theta = np.linspace(-max_angle, max_angle, 500)
    else:
        orbit_type = "Эллиптическая"
        theta = np.linspace(0, 2*np.pi, 500)
    
    # Рассчитываем радиусы
    r = orbit_equation(p, e, theta)
    
    # Строим орбиту
    axes2[i].plot(theta, r, linewidth=2)
    axes2[i].set_title(f'{orbit_type}: p={p}, e={e}', pad=20)
    axes2[i].grid(True)
    
    # Рассчитываем параметры
    if e < 1:
        h_per, h_apo = calculate_orbital_parameters(p, e)
        if h_per is not None:
            print(f"{orbit_type} {i+1}: высота={h_per:.2f} км")

plt.suptitle('Различные типы орбит (домашнее задание)', fontsize=16)
plt.tight_layout()
plt.show()

# ===================== 2. ЗАВИСИМОСТЬ РАЗМЕРА ЗР ОТ ВЫСОТЫ =====================
print("\n=== РАСЧЁТ ЗАВИСИМОСТИ ЗР ОТ ВЫСОТЫ ===")

# Диапазон высот от 100 до 50000 км
h_array = np.linspace(100, 50000, 200)  # км
theta_array_deg = []

# Рассчитываем θ для каждой высоты
for h_val in h_array:
    term = (R_earth * np.cos(beta_min)) / (R_earth + h_val)
    if abs(term) <= 1:
        theta_rad = np.arccos(term) - beta_min
        theta_rad = max(theta_rad, 0)  # не отрицательный
    else:
        theta_rad = 0
    theta_array_deg.append(np.rad2deg(theta_rad))

# График зависимости
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.plot(h_array, theta_array_deg, 'b-', linewidth=2)
ax3.set_xlabel('Высота орбиты, км', fontsize=12)
ax3.set_ylabel('Угловой размер ЗР (θ), градусы', fontsize=12)
ax3.set_title(f'Зависимость углового размера ЗР от высоты (β_min = {beta_min_deg}°)', fontsize=14)
ax3.grid(True, alpha=0.3)

# Отмечаем высоты для эллиптических орбит
colors = ['red', 'green', 'blue', 'purple']
for i, (p, e) in enumerate(zip(p_elliptic, e_elliptic)):
    if e < 1:
        h_per, h_apo = calculate_orbital_parameters(p, e)
        if h_per is not None:
            # Рассчитываем θ для перигея
            term_per = (R_earth * np.cos(beta_min)) / (R_earth + h_per)
            if abs(term_per) <= 1:
                theta_per_rad = np.arccos(term_per) - beta_min
                theta_per_deg = np.rad2deg(max(theta_per_rad, 0))
            else:
                theta_per_deg = 0
            
            # Рассчитываем θ для апогея
            term_apo = (R_earth * np.cos(beta_min)) / (R_earth + h_apo)
            if abs(term_apo) <= 1:
                theta_apo_rad = np.arccos(term_apo) - beta_min
                theta_apo_deg = np.rad2deg(max(theta_apo_rad, 0))
            else:
                theta_apo_deg = 0
            
            # Отмечаем точки на графике
            ax3.scatter(h_per, theta_per_deg, color=colors[i], s=100, 
                       label=f'Орбита {i+1}: h_per={h_per:.0f} км')
            ax3.scatter(h_apo, theta_apo_deg, color=colors[i], s=100, marker='s',
                       label=f'Орбита {i+1}: h_apo={h_apo:.0f} км')

ax3.legend(fontsize=9, loc='upper right')
plt.tight_layout()
plt.show()

# ===================== 3. ВЫВОД РЕЗУЛЬТАТОВ =====================
print("\n=== РЕЗУЛЬТАТЫ РАСЧЁТОВ ===")
print(f"β_min = {beta_min_deg}°")

print("\n1. Параметры эллиптических орбит:")
for i, (p, e) in enumerate(zip(p_elliptic, e_elliptic)):
    h_per, h_apo = calculate_orbital_parameters(p, e)
    if h_per is not None:
        print(f"   Орбита {i+1} (p={p}, e={e}):")
        print(f"     Высота перигея: {h_per:.2f} км")
        print(f"     Высота апогея: {h_apo:.2f} км")
        
        # Рассчитываем θ для перигея
        term_per = (R_earth * np.cos(beta_min)) / (R_earth + h_per)
        if abs(term_per) <= 1:
            theta_per_rad = np.arccos(term_per) - beta_min
            theta_per_deg = np.rad2deg(max(theta_per_rad, 0))
        else:
            theta_per_deg = 0
            
        # Рассчитываем θ для апогея
        term_apo = (R_earth * np.cos(beta_min)) / (R_earth + h_apo)
        if abs(term_apo) <= 1:
            theta_apo_rad = np.arccos(term_apo) - beta_min
            theta_apo_deg = np.rad2deg(max(theta_apo_rad, 0))
        else:
            theta_apo_deg = 0
            
        print(f"     θ в перигее: {theta_per_deg:.2f}°")
        print(f"     θ в апогее: {theta_apo_deg:.2f}°")

print("\n2. Для других орбит:")
for i, (p, e) in enumerate(zip(p_other, e_other)):
    if e == 0:
        print(f"   Круговая орбита (p={p}, e={e}):")
        h = p - R_earth
        term = (R_earth * np.cos(beta_min)) / (R_earth + h)
        if abs(term) <= 1:
            theta_rad = np.arccos(term) - beta_min
            theta_deg = np.rad2deg(max(theta_rad, 0))
        else:
            theta_deg = 0
        print(f"     Высота: {h:.2f} км")
        print(f"     θ: {theta_deg:.2f}°")
    elif e < 1 and e > 0:
        print(f"   Эллиптическая орбита (p={p}, e={e}):")
        h_per, h_apo = calculate_orbital_parameters(p, e)
        if h_per is not None:
            print(f"     Высота перигея: {h_per:.2f} км")
            print(f"     Высота апогея: {h_apo:.2f} км")
    else:
        orbit_type = "Параболическая" if e == 1 else "Гиперболическая"
        print(f"   {orbit_type} орбита (p={p}, e={e}):")
        print(f"     Незамкнутая орбита")

print("\n=== РАСЧЁТ ЗАВЕРШЕН ===")

# ===================== 4. СЕМЕЙСТВО ЗАВИСИМОСТЕЙ =====================
print("\n=== СЕМЕЙСТВО ЗАВИСИМОСТЕЙ ЗР ОТ ВЫСОТЫ ===")

# Разные значения β_min
beta_values_deg = [5, 15, 25, 35]
h_range = np.linspace(100, 50000, 200)

fig4, ax4 = plt.subplots(figsize=(10, 6))

for beta_deg in beta_values_deg:
    beta_rad = np.deg2rad(beta_deg)
    theta_vals = []
    
    for h_val in h_range:
        term = (R_earth * np.cos(beta_rad)) / (R_earth + h_val)
        if abs(term) <= 1:
            theta = np.arccos(term) - beta_rad
            theta_vals.append(np.rad2deg(max(theta, 0)))
        else:
            theta_vals.append(0)
    
    ax4.plot(h_range, theta_vals, label=f'β_min = {beta_deg}°', linewidth=2)

ax4.set_xlabel('Высота орбиты, км', fontsize=12)
ax4.set_ylabel('Угловой размер ЗР (θ), градусы', fontsize=12)
ax4.set_title('Семейство зависимостей θ от высоты для разных β_min', fontsize=14)
ax4.grid(True, alpha=0.3)
ax4.legend(fontsize=10)
plt.tight_layout()
plt.show()

print("Графики построены успешно!")