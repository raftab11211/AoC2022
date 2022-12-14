import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day6/input.txt"))
data = file.read().strip()
lines = [x.strip() for x in data.split('\n')]

# sliding window across 4 chars, check if unique


def is_unique_list(list):
    count_chars = {}
    for char in list:
        if (char in count_chars):
            # If the char exists in the dictionary then it must be a duplicate, fail fast
            return False
        else:
            count_chars[char] = 1

    return True

#pt1
print("pt1")
for line in lines:   
    current_chars = list(line[0:4])
    for idx, char in enumerate(line):
        if idx >= 4:
            current_chars.pop(0)
            current_chars.append(char)
            if is_unique_list(current_chars):
                print(f"idx:{idx + 1}")
                break
        
        idx += 1

#pt2
print("\r\npt2")
for line in lines:   
    current_chars = list(line[0:14])
    for idx, char in enumerate(line):
        if idx >= 14:
            current_chars.pop(0)
            current_chars.append(char)
            if is_unique_list(current_chars):
                print(f"idx:{idx + 1}")
                break
        
        idx += 1