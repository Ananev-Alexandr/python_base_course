import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'\b(\w)(\w)+?', r'\2\1', line)
    print(result)
    