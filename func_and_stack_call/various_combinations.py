def various_combinations(fist_value, second_value):
    if second_value == 0:
        return 1
    elif second_value > fist_value:
        return 0
    else:
        return various_combinations(fist_value - 1, second_value) + various_combinations(fist_value - 1, second_value - 1)


fist_value, second_value = map(int, input().split())
print(various_combinations(fist_value,second_value))
