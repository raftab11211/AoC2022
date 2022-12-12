import os
file = open(os.path.join(os.getcwd(), "AoC2022/Day3/input.txt"))

values = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13,
          "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}


def get_priority(character):
    if character.isupper():
        return values[character.lower()] + 26
    return values[character.lower()]


def get_overlaps(itemsFirst, itemsSecond):
    priority = 0
    for key in itemsFirst:
        if itemsSecond.get(key) is not None:
            priority += get_priority(key)

    return priority


# pt1
total_priorities = 0
for line in file:
    line = line.replace("\n", "")
    first = line[0:(len(line) // 2)]
    second = line[len(line) // 2:len(line)]
    itemsFirst = {}
    itemsSecond = {}
    for char in list(first):
        if itemsFirst.get(char) is not None:
            itemsFirst[char]["count"] += 1
        else:
            itemsFirst[char] = {"count": 1}

    for char in list(second):
        if itemsSecond.get(char) is not None:
            itemsSecond[char]["count"] += 1
        else:
            itemsSecond[char] = {"count": 1}

    priority = get_overlaps(itemsFirst, itemsSecond)
    total_priorities += priority

print(total_priorities)

# pt2
file.seek(0)

def get_overlaps_pt2(items):
    priority = 0
    items_first = items[0]
    items_second = items[1]
    items_third = items[2]
    
    #sin
    for item_first in items_first:
        for item_second in items_second:
            if (item_first == item_second):
                for item_third in items_third:
                    if (item_first == item_third):
                        priority += get_priority(item_first)

    return priority

total_priority = 0
items_of_items = []
for line in file:
    line = line.replace("\n", "")
    items = []
    for char in list(line):
        if char not in items:
            items.append(char)

    items_of_items.append(items)

    if len(items_of_items) % 3 == 0:
        priority = get_overlaps_pt2(items_of_items)
        total_priority += priority
        items_of_items = []
    
print(total_priority)
