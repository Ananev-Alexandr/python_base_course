import os


lis = []
for currend_dir, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith('.py'):
            nice_dir = currend_dir.replace("\\", "/")
            lis.append(nice_dir + '\n')
            break

sorted(lis)

with open("tesxt.txt", "w") as w:
    for elem in lis:
        w.write(elem)
