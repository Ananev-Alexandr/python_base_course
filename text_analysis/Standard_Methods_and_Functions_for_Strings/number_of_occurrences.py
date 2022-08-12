s, a, b = input(), input(), input()
count_num = 0


while True:
    if count_num <= 1000:
        if a in s:
            s = s.replace(a, b)
            count_num += 1
            continue
        if s.count(a) == 0:
            print(count_num)
            break
    else:
        print('Impossible')
        break
