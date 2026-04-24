filename = input()
try:
	with open(filename, "r") as file:
		for line in file:
			parts = line.split()
			if not parts:
				continue
			name = parts[0]
			try:
				age = int(parts[1]) + 1
                print(name, age)
            except ValueError:
                print(name, 0)
except OSError:
    print("Error: File not found.")
