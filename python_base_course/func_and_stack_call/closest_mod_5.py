def closest_mod_5(x):
    if x % 5 == 0 and x >= 5:
        return x
    return (((x + 5 - 1) // 5) * 5)

    

x = int(input())
print(closest_mod_5(x))