rows = 4
for i in range(rows):
    star = '*' * (2 * i + 1)
    faza = ' ' * (rows - i - 1)
    print(faza + star)