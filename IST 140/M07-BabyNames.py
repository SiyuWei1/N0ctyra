boys = []
girls = []

with open("babynames2010s.txt", "r") as file:
    for line in file:
        parts = line.split()
        if len(parts) == 5:
            boys.append(parts[1])
            girls.append(parts[3])

print("Names that appear in both the boys' and girls' lists:")
for name in boys:
    if name in girls:
        print(name)
