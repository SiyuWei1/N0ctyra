input_file = open("babynames2010s.txt","r")
boy_names = []
girl_names = []

for line in input_file:
  columns = line.split()
  boy_name = columns[1]
  girl_name = columns[3]
  boy_names.append(boy_name)
  girl_names.append(girl_name)

input_file.close()
print("Names that appear on both the boys and girls\"list:")
for name in boy_names:
    if name in girl_names:
        print(name)
