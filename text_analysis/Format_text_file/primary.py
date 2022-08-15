import csv


primary_dict = {}


def find_primary(reader):
    for primary_type in reader:
        primary = primary_type[5]
        if primary not in primary_dict:
            primary_dict[primary] = 1
        else:
            primary_dict[primary] += 1


with open("2.csv") as f:
    reader = csv.reader(f)
    find_primary(reader)


for key, value in primary_dict.items():
    if value == max(primary_dict.values()):
        print(key, value)
