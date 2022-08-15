import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.search("cat.*cat", line)
    if result is not None:
        print(line)