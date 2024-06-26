def get_password(n):
    used_pairs = set()
    result = ""
    for i in range(1, 21):
        for j in range(i+1, 21):
            if n % (i +j) == 0:
                pair = str(i) + str(j)
                if pair not in used_pairs:
                    used_pairs.add(pair)
                    result += pair
    return result
n = int(input("Введите число от 3 до 20: "))
password = get_password(n)
print(f"Пароль для числа {n}: {password}")