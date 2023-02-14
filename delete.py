with open("data.txt") as f:
    lines = f.read() ##Assume the sample file has 3 lines
    first = lines.split('\n', 1)[0]

print(first)