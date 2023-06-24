# area = [
#     [0, 1, 2, 3],
#     [1, "_", "_", "_"],
#     [2, "_", "_", "_"],
#     [3, "_", "_", "_"]
# ]

# for i in range(4):
#     for j in range(4):
#         print(M[i][j], end=" ")
#     print()
# Слишком громоздкий вариант поля, но я его полюбила, поэтому оставлю для истории


def battle_area(a):
    print(' ', 'a', 'b', 'c')
    for i in range(len(area)):
        print(str(i+1), *area[i])

def users_move(a):
    while True:
        move_it = input('Введите две координаты без пробелов и запятых, начиная с буквы: ').lower()
        if len(move_it) != 2:
            print('Вы ввели не две кооординаты')
            continue
        if not (str(move_it[0]) in ('a', 'b', 'c')) or not (int(move_it[1]) in (1, 2, 3)):
            # Кому нужны сложные диапазоны, если там по три варианта?
            print('Вы где-то ошиблись. Введите координаты по типу "a2" или "b3"')
            continue
        if move_it[0] == 'a':
            ve = 0
        elif move_it[0] == 'b':   # Я знаю, что это выглядит ужасно
            ve = 1                # Но другие варианты были ещё хуже
        else: ve = 2
        ho = (int(move_it[1]) - 1)
        if area[ho][ve] != '_':
            print("Вы уже сюда ходили")
            continue
        break
    return ho, ve

def bot_move(a):
    import random
    def bot_win(a):
        # def bot_want_win(l1, l2, l3):
        #     if l1 == 'o' and l2 == 'o' and l3 == '_' or \
        #             l1 == 'o' and l2 == '_' and l3 == 'o' or \
        #             l1 == '_' and l2 == 'o' and l3 == 'o':
        #         return True
        #     elif l1 == 'x' and l2 == 'x' and l3 == '_' or \
        #             l1 == 'x' and l2 == '_' and l3 == 'x' or \
        #             l1 == '_' and l2 == 'x' and l3 == 'x':
        #         return True
        #     else:
        #         return False
        def bot_want_win(l1, l2, l3):
            if (l1 == 'o' and l2 == 'o' and l3 == '_') or \
                    (l1 == 'o' and l2 == '_' and l3 == 'o') or \
                (l1 == '_' and l2 == 'o' and l3 == 'o') or \
                    (l1 == 'x' and l2 == 'x' and l3 == '_') or \
                (l1 == 'x' and l2 == '_' and l3 == 'x') or \
                    (l1 == '_' and l2 == 'x' and l3 == 'x'):
                return True
            else:
                return False
        for n in range(3):
            if bot_want_win(a[n][0], a[n][1], a[n][2]):
                f1 = [n, 0]
                f2 = [n, 1]
                f3 = [n, 2]
                return f1, f2, f3
            elif bot_want_win(a[0][n], a[1][n], a[2][n]):
                f1 = [0, n]
                f2 = [1, n]
                f3 = [2, n]
                return f1, f2, f3
            elif bot_want_win(a[0][0], a[1][1], a[2][2]):
                f1 = [0, 0]
                f2 = [1, 1]
                f3 = [2, 2]
                return f1, f2, f3
            elif bot_want_win(a[2][0], a[1][1], a[0][2]):
                f1 = [2, 0]
                f2 = [1, 1]
                f3 = [0, 2]
                return f1, f2, f3
        return False
    while True:
        ve, ho = random.randrange(0, 3), random.randrange(0, 3)
        if a[ve][ho] != '_':
            continue
        if bot_win(a):
            f1, f2, f3 = bot_win(a)
            coord = [f1, f2, f3]
            for i in coord:           # Чтобы оно не просто тыкало в клетки, а стремилось к победе
                ve, ho = i[0], i[1]
                if a[ve][ho] == '_':
                    break
            # print(coord)
            # print(ve, ho)
            # Это было нужно для проверки
        break
    if ho == 0:
        ho_letter = 'a'
    elif ho == 1:
        ho_letter = 'b'
    else:
        ho_letter = 'c'
    print("Бот выбрал координаты:", ho_letter, ve + 1)
    return ve, ho

def epic_wim(a, user):
    # if ((a[0][0] and a[0][1] and a[0][2]) == user) or \
    #         ((a[1][0] and a[1][1] and a[1][2]) == user) or \
    #           ((a[2][0] and a[2][1] and a[2][2]) == user) or \
    #         ((a[0][0] and a[1][0] and a[2][0]) == user) or \
    #           ((a[0][1] and a[1][1] and a[2][1]) == user) or \
    #         ((a[0][2] and a[1][2] and a[2][2]) == user) or \
    #           ((a[0][0] and a[1][1] and a[2][2]) == user) or \
    #         ((a[0][2] and a[1][1] and a[2][0]) == user):
    #     return True
    # else:
    #     return False
    #
    # Это была ужасная попытка
    #
    def check_win(l1, l2, l3, user):
        if l1 == user and l2 == user and l3 == user:
            return True
    for i in range(3):
        if check_win(a[i][0], a[i][1], a[i][2], user) or \
                check_win(a[0][i], a[1][i], a[2][i], user) or \
                check_win(a[0][0], a[1][1], a[2][2], user) or \
                check_win(a[0][2], a[1][1], a[2][0], user):
            return True
    return False

def fight(a):
    battle_area(a)
    count = 0
    while count < 9:
        if count % 2 == 0:
            user = "x"
            print(f'Ходит {user}')
        else:
            user = "o"
            print(f'Ходит {user}')
        ho, ve = users_move(area)
        area[ho][ve] = user
        if epic_wim(a, user):
            battle_area(a)
            print(f"Победил {user}")
            battle_area(a)
        count += 1
    else:
        battle_area(a)
        print('Ничья')

def bot_fight(a):
    battle_area(a)
    count = 0
    while count < 9:
        if count % 2 == 0:
            user = "x"
            print(f'Ходит игрок {user}')
            ho, ve = users_move(area)
            area[ho][ve] = user
        else:
            user = "o"
            print(f'Ходит бот {user}')
            ho, ve = bot_move(a)
            area[ho][ve] = user
        if epic_wim(a, user):
            battle_area(a)
            print(f"Победил {user}")
        battle_area(a)
        count += 1
    else:
        print('Ничья')
        battle_area(a)

def big_fatality(a):
    print("Добро пожаловать в 'Крестики-нолики'!")
    while True:
        choice = input('Если хотите поиграть с ботом, введите "1", если хотите поиграть самостоятельно, нажмите "0": ')
        if choice not in ('0', '1'):
            print('Похоже, вы ввели что-то не то')
            continue
        break
    if choice == '0':
        print('Удачноё игры!')
        fight(a)
    else:
        bot_fight(a)

area = [['_']*3 for _ in range(3)]

big_fatality(area)





