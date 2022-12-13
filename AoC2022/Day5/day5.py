import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day5/input.txt"))
data = file.read().strip()
lines = [x.strip() for x in data.split('\n')]

# example
# stack_1 = list(reversed(["N", "Z"]))
# stack_2 = list(reversed(["D", "C", "M"]))
# stack_3 = list(reversed(["P"]))
# stacks = {"1": stack_1, "2": stack_2, "3": stack_3}
# range_to_print = 3
# start_reading_after = 5

# input
stack_1 = list(reversed(["V", "Q", "W", "M", "B", "N", "Z", "C"]))
stack_2 = list(reversed(["B", "C", "W", "R", "Z", "H"]))
stack_3 = list(reversed(["J", "R", "Q", "F"]))
stack_4 = list(reversed(["T", "M", "N", "F", "H", "W", "S", "Z"]))
stack_5 = list(reversed(["P", "Q", "N", "L", "W", "F", "G"]))
stack_6 = list(reversed(["W", "P", "L"]))
stack_7 = list(reversed(["J", "Q", "C", "G", "R", "D", "B", "V"]))
stack_8 = list(reversed(["W", "B", "N", "Q", "Z"]))
stack_9 = list(reversed(["J", "T", "G", "C", "F", "L", "H"]))

stacks = {"1": stack_1, "2": stack_2, "3": stack_3, "4": stack_4,
          "5": stack_5, "6": stack_6, "7": stack_7, "8": stack_8, "9": stack_9}
range_to_print = 9
start_reading_after = 10


def move_item(count, from_stack, to_stack):
    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())


def move_all_items(count, from_stack, to_stack):
    #The syntax voodoo required for slice or delete was a real PITA
    stack_sliced = stacks[from_stack][-count:]
    del stacks[from_stack][-count:]
    for item in stack_sliced:
        stacks[to_stack].append(item)


# pt1
for idx, line in enumerate(lines):
    if (idx >= start_reading_after):
        command_split = line.split(" ")
        move_count = command_split[1]
        from_stack = command_split[3]
        to_stack = command_split[5]
        move_item(int(move_count), from_stack, to_stack)

    idx += 1

stack_idx_to_print = 1
top_stack_str = ""
for i in range(range_to_print):
    top_stack_str += stacks[str(stack_idx_to_print)].pop()
    stack_idx_to_print += 1

print(top_stack_str)


# example
# stack_1 = list(reversed(["N", "Z"]))
# stack_2 = list(reversed(["D", "C", "M"]))
# stack_3 = list(reversed(["P"]))
# stacks = {"1": stack_1, "2": stack_2, "3": stack_3}
# range_to_print = 3
# start_reading_after = 5

# input
stack_1 = list(reversed(["V", "Q", "W", "M", "B", "N", "Z", "C"]))
stack_2 = list(reversed(["B", "C", "W", "R", "Z", "H"]))
stack_3 = list(reversed(["J", "R", "Q", "F"]))
stack_4 = list(reversed(["T", "M", "N", "F", "H", "W", "S", "Z"]))
stack_5 = list(reversed(["P", "Q", "N", "L", "W", "F", "G"]))
stack_6 = list(reversed(["W", "P", "L"]))
stack_7 = list(reversed(["J", "Q", "C", "G", "R", "D", "B", "V"]))
stack_8 = list(reversed(["W", "B", "N", "Q", "Z"]))
stack_9 = list(reversed(["J", "T", "G", "C", "F", "L", "H"]))

stacks = {"1": stack_1, "2": stack_2, "3": stack_3, "4": stack_4,
          "5": stack_5, "6": stack_6, "7": stack_7, "8": stack_8, "9": stack_9}
range_to_print = 9
start_reading_after = 10

# pt2
for idx, line in enumerate(lines):
    if (idx >= start_reading_after):
        command_split = line.split(" ")
        move_count = command_split[1]
        from_stack = command_split[3]
        to_stack = command_split[5]
        move_all_items(int(move_count), from_stack, to_stack)

    idx += 1

stack_idx_to_print = 1
top_stack_str = ""
for i in range(range_to_print):
    top_stack_str += stacks[str(stack_idx_to_print)].pop()
    stack_idx_to_print += 1

print(top_stack_str)
