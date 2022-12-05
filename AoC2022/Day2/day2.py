import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day2/input.txt"))

rock = 1  # A#X
paper = 2  # B#Y
scissors = 3  # C#Z

loss = 0
draw = 3
win = 6


#pt1
values = {"AY": 8, "BY": 5, "CY": 2, "AX": 4,
    "BX": 1, "CX": 7, "AZ": 3, "BZ": 9, "CZ": 6}

score = 0
for line in file:
    line = line.replace(" ", "").replace("\n", "")
    score += values[line]

print(score)

#pt2
values_pt2 = {"AY": 4, "BY": 5, "CY": 6, "AX": 3,"BX": 1, "CX": 2, "AZ": 8, "BZ": 9, "CZ": 7}

score_pt2 = 0
file.seek(0)
for line in file:
    line = line.replace(" ","").replace("\n","")
    score_pt2 += values_pt2[line]

print(score_pt2)
