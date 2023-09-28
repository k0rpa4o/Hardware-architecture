ch = int(input("введите врмя: "))

if ch >=3 and ch <= 5:
    print("раннее утро")
elif ch >=6 and ch <= 10:
    print("утро")
elif ch >=11 and ch <= 15:
    print("день")
elif ch >=16 and ch <= 21:
    print("вечер")
else:
    print("ночь")
