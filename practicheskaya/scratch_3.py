def civra(pas):
    i = 0
    for i in range(len(pas)):
        if pas[i] >= "0" and pas[i] <= "9":
            return True
    return False


def dlina(pas):
    if len(pas) >= 4:
        return True
    else:
        return False


def zaglav(pas):
    for i in range(len(pas)):
        if pas[i] >= "A" and pas[i] <= "Z":
            return True
    return False


def mal(pas):
    for i in range(len(pas)):
        if pas[i] >= "a" and pas[i] <= "z":
            return True
    return False


def main():
    pas = input()
    if civra(pas) == True and dlina(pas) == True and zaglav(pas) == True and mal(pas) == True:
        print("пароль имба")
    if civra(pas) == False and len(pas) < 4:
        print("нет цифр")
    if dlina(pas) == False:
        print("надо больше символов")
    if zaglav(pas) == False:
        print("нет заглавных")
    if mal(pas) == False:
        print("нет строчных")


if __name__ == '__main__':
    main()
