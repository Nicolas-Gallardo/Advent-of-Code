from part1 import sum_priorities

def main():

    file = "input.txt"
    sum_of_priorities = 0
    with open(file) as f:
        badge = ""
        group_rucksack = []
        for n, line in enumerate(f):
            group_rucksack.append(line.replace("\n",""))
            if n%3-2 == 0:
                for i in group_rucksack[0]:
                    if (i in group_rucksack[1]) and \
                        (i in group_rucksack[2]):
                        badge = i
                        break
                group_rucksack = []
                sum_of_priorities += sum_priorities(badge)
    print(f"The sum of the badge's priorities is {sum_of_priorities}")
    return 0

if __name__ == "__main__":
    main()