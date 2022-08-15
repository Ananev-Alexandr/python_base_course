import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'(\w{0,})\1+', r'\1', line)
    for i in range(5):
        result = re.sub(r'(\w{0,})\1+', r'\1', result)
    print(result)
    