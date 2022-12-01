def calories_counting_part_one():
    """
    Problem: https://adventofcode.com/2022/day/1
    """
    ans = 0
    current = 0
    with open("file.txt") as file:
        for line in file:
            if line == "\n":
                ans = max(ans, current)
                current = 0
            else:
                num = int(line.rstrip("\n"))
                current += num
        print(ans)
        return ans

def calories_counting_part_two():
    """
    Problem: https://adventofcode.com/2022/day/1
    """
    calories = []
    current = 0
    with open("file.txt") as file:
        for line in file:
            if line == "\n":
                calories.append(current)
                current = 0
            else:
                num = int(line.rstrip("\n"))
                current += num
        calories.sort(reverse=True)
        ans = sum(calories[:3])
        print(ans)
        return ans

