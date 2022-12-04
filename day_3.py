def get_compartments(s):
    n = len(s)
    return s[:n // 2], s[n // 2:]


def get_priority(item):
    is_upper = item.isupper()
    if is_upper:
        return ord(item) - 38
    else:
        return ord(item) - 96


def rucksack_part_one():
    total_priority = 0
    with open("file.txt") as file:
        for line in file:
            first, second = get_compartments(line)
            common = set(first).intersection(set(second))
            total_priority += sum(map(get_priority, common))
        print(total_priority)


def rucksack_part_two():
    total_priority = 0
    with open("file.txt") as file:
        group = []
        for line in file:
            line = line.rstrip("\n")
            if len(group) == 3:
                common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
                total_priority += sum(map(get_priority, common))
                group = [line]
            else:
                group.append(line)
        common = set(group[0]).intersection(set(group[1])).intersection(set(group[2]))
        total_priority += sum(map(get_priority, common))
        print(total_priority)
rucksack_part_two()
