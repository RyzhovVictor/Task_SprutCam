# Попросить пользователя ввести строку в формате ‘’CYCLE82(P1,P2,P3,P4,P5,P6,P7,P8,P9)”.
input_string = input("Введите строку в формате 'CYCLE82(P1,P2,P3,P4,P5,P6,P7,P8,P9)': ")

# Извлечь значения параметров из входной строки и присвоить их соответствующим переменным.
params = input_string.split("(")[1].split(")")[0].split(",")
p1, p2, p3, p4, p5, p6, p7, p8, p9 = [float(param) if param else 0 for param in params]

# Определить значение символа "Z" в зависимости от плоскости расположения отверстия.
if p8 == 1:
    z_symbol = "Z"
    p8 = 17
elif p8 == 2:
    z_symbol = "Y"
    p8 = 18
else:
    z_symbol = "X"
    p8 = 19

# Сформировать первую выходную строку в зависимости от плоскости расположения отверстия.
first_line = f"G{int(p8)} G0 {z_symbol}{int(p1)}"

# Определить тип цикла (81 или 82) в зависимости от наличия выдержки на глубине сверления.
if p6:
    cycle_type = 82
else:
    cycle_type = 81

# Сформировать вторую выходную строку в соответствии с типом цикла и плоскостью расположения отверстия.
if cycle_type == 82:
    second_line = f"G{int(cycle_type)} {z_symbol}{int(p4)} R{p2 + p3} P{int(p6)} F200"
else:
    second_line = f"G{int(cycle_type)} {z_symbol}{p5 + p2} R{int(p2 + p3)} F200"

# Вывести результат на экран.
print(first_line)
print(second_line)
