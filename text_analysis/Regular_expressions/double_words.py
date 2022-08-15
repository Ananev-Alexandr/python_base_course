import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.search(r"\b(\w+)\1\b", line)
    if result is not None:
        print(line)