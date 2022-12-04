import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day1/input.txt"))

calorieslist = [0]
calories = 0

for line in file:  
    if '\n' == line:
        calorieslist.append(0)
        calories = 0
    else:
        calorieslist[-1] += int(line)

calorieslist = sorted(calorieslist, reverse=True)

#pt1
print(calorieslist[0])

#pt2
print(sum(calorieslist[0:3]))
