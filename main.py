import random
a = random.randint(0, 100)
b=7
print("Вітаю! Я загадав число від 1 до 100. Спробуй його вгадати за 7 спроб.")


while b>0:
    num = int(input("Введіть ваше припущення: "))
    if num>a:
        print("Занадто велике!")
    elif num<a:
        print("Занадто маленьке!")
    else:
        print(f"Ви вгадали! Це число {a}")
        break

    b -= 1
if b == 0 and num != a:
    print(f"Cпроби закінчилися. Загадане число було: {a}")

