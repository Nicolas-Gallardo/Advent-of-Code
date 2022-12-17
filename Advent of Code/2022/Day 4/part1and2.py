import intervals as I
def main():
    file = "input.txt"
    subset = 0
    inter = 0
    with open(file) as f:
        for line in f:
            ranges = line.split(",")
            elf1 = list(map(int,ranges[0].split("-")))
            elf2 = list(map(int,ranges[1].split("-")))
            section1 = I.closed(elf1[0],elf1[1])
            section2 = I.closed(elf2[0],elf2[1])
            if (section1 in section2) or (section2 in section1):
                subset += 1
            if section1.overlaps(section2):
                inter += 1
    print(f"the number of pairs in which one contains the other is {subset}")
    print(f"the number of pairs that overlaps is {inter}")
    return 0

if __name__ == "__main__":
    main()