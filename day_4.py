def does_contain(a, b):
    if a[0] <= b[0] and b[1] <= a[1]:
        return True
    if b[0] <= a[0] and a[1] <= b[1]:
        return True
    return False

def is_overlapping(a, b):
    return max(a[0], b[0]) <= min(a[1], b[1])

def get_interval(data):
    a, b = data.split("-")
    return int(a), int(b)

def camp_cleanup_part_one():
    ans = 0
    with open("file.txt") as file:
        for line in file:
            line = line.rstrip("\n")
            first, second = line.split(",")
            first, second = get_interval(first), get_interval(second)
            if is_overlapping(second, first):
                #print(first, second)
                ans += 1
        print(ans)

camp_cleanup_part_one()
