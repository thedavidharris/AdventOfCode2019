print(sum((num//3)-2 for num in [int(line.strip()) for line in open("input.txt")]))