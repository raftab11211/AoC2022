import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day4/example_input.txt"))

inclusive_pairs_pt1 = 0
inclusive_pairs_pt2 = 0
for line in file:
    line = line.replace("\n", "")

    first_pair = line.split(",")[0]
    second_pair = line.split(",")[1]

    first_index_first_pair = int(first_pair.split("-")[0])
    second_index_first_pair = int(first_pair.split("-")[1])

    first_index_second_pair = int(second_pair.split("-")[0])
    second_index_second_pair = int(second_pair.split("-")[1])

    if ((first_index_first_pair >= first_index_second_pair and second_index_first_pair <= second_index_second_pair) or
            (first_index_first_pair <= first_index_second_pair and second_index_first_pair >= second_index_second_pair)):
        inclusive_pairs_pt1 += 1

    if ((second_index_first_pair >= first_index_second_pair and first_index_first_pair <= second_index_second_pair) or (first_index_second_pair <= second_index_first_pair and second_index_second_pair >= second_index_first_pair)):
        inclusive_pairs_pt2 += 1

print(inclusive_pairs_pt1)
print(inclusive_pairs_pt2)
