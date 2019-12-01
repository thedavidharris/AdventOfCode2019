def fuel_required(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + fuel_required(fuel)
    else:
        return 0

print(sum(fuel_required(num) for num in [int(line.strip()) for line in open("input.txt")]))