import sys, re


for line in sys.stdin:
    line = line.rstrip()
    result = re.sub(r'\b(a{0,100})a\b', r'argh', line, count=1, flags=re.IGNORECASE)
    print(result)
    