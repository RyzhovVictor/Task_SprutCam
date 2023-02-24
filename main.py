import re

# входная строка
input_str = "CYCLE82(10,-1.5,2,-27,,1,0,1,12)"

# регулярное выражение для извлечения параметров
pattern = r"CYCLE82\((?P<P1>[\d.-]+),(?P<P2>[\d.-]+),(?P<P3>[\d.-]+),(?P<P4>[\d.-]*),(?P<P5>[\d.-]*),(?P<P6>[\d.-]+),(?P<P7>\d+),(?P<P8>\d+),(?P<P9>\d+)\)"

# поиск параметров во входной строке
match = re.search(pattern, input_str)

if match:
    # извлечение параметров
    p1 = float(match.group("P1"))
    p2 = float(match.group("P2"))
    p3 = float(match.group("P3"))
    p4 = float(match.group("P4")) if match.group("P4") else None
    p5 = float(match.group("P5")) if match.group("P5") else None
    p6 = float(match.group("P6"))
    p7 = int(match.group("P7"))
    p8 = int(match.group("P8"))
    p9 = int(match.group("P9"))

    # определение плоскости расположения отверстия
    if p8 == 1:
        plane = "G17"
        z = p1
    elif p8 == 2:
        plane = "G18"
        z = p2
    else:
        plane = "G19"
        z = p3

    # формирование строки для перемещения в безопасную плоскость
    g0_str = f"{plane} G0 Z{p1}"

    # формирование строки для сверления
    if p9 == 12:
        z_val = f"{z - p4:.1f}"
    else:
        z_val = f"{z + p5:.1f}"

    if p6 > 0:
        g_str = "G82"
        p_str = f"P{int(p6)}"
    else:
        g_str = "G81"
        p_str = ""

    g1_str = f"{plane} {g_str} Z{z_val} R0.5 {p_str} F200"

    # вывод результатов
    print(g0_str)
    print(g1_str)
else:
    print("Invalid input")
