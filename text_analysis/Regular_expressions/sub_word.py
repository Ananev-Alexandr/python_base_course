import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'human', r'computer', line)
    print(result)