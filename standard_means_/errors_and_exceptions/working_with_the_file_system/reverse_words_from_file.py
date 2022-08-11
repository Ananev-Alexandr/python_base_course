list_words = []
with open('test.txt') as file:
    for line in file:
        line = line.rstrip()
        list_words.append(line)
    list_words.reverse()
    for element in list_words:
        print(element)