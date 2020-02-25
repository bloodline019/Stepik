n = int(input())  # принимаем число матчей.
out_results = {}
for i in range(n):
    first_team, score1, second_team, score2 = input().split(";")  # Ввод:Команда1;Забила1команда;Команда2;Забила2команда
    for team in (first_team, second_team):
        if team not in out_results:
            out_results[team] = [0 for i in range(5)]  # Для каждой команды формируем список из 5 нулей.
        out_results[team][0] += 1  # Увеличиваем количество игр на 1 для каждой команды.

    if score1 == score2:
        for team in (first_team, second_team):
            out_results[team][4] += 1
            out_results[team][2] += 1
    else:
        if score1 > score2:
            winner, looser = first_team, second_team
        else:
            winner, looser = second_team, first_team
        out_results[winner][4] += 3  # Всего_игр Побед Ничьих Поражений Всего_очков
        out_results[winner][1] += 1  # 0         1     2      3          4
        out_results[looser][3] += 1
for i in out_results:
    print('{}:{} {} {} {} {}'.format(i, *out_results[i]))  # В первую ячейку назв.команды, остальные пять - статистика
    # в виде распакованного списка через '*'.
