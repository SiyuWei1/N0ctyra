import random

def generate_temps():
    temps = []
    for i in range(10):
        num = random.randint(60, 80)
        temps.append(num)
    return temps

def write_data():
    temperature_list = generate_temps()
    file = open("daily_temps.txt", "W")
    for temp in temperature_list:
        file.write(str(temp) + '\n')
    file.close()

def analyze_data():
	total = 0
	count = 0
	file = open("daily_temps.txt", "r")
	for line in file:
		total += int(line.strip())
		count += 1
	file.close()
	if count > 0:
		average = total / count
		print(f"The average daily temperature was {average}°F.")

if __name__ == "__main__":
	write_data()
	analyze_data()
	
