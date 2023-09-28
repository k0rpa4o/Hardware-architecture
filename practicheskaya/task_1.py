temp = int(input("введите температуру "))
voz = int(input("введите влажность воздуха "))
if voz > 100 or voz < 0:
    print("некоректно ввели осадки")
else:
    if voz >= 90:
        print("идут осадки")
    if voz < 90:
        print("осадки не идут")
    elif temp < 0:
        print("идет снег")
    elif temp >= 0:
        print("идет дождь")
