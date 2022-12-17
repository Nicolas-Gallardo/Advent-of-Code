def sum_priorities(item: str) -> int:
    if item.islower():
        return ord(item)-ord("a") + 1
    else:
        return ord(item)-ord("A") + 27

def main():

    file = "input.txt"
    sum_of_priorities = 0
    with open(file) as f:
        for line in f:
            rucksack = line.replace("\n","")
            compartment1 = rucksack[0:len(rucksack)//2]
            compartment2 = rucksack[len(rucksack)//2:len(rucksack)]
            item = ""
            for i in compartment1:
                if i in compartment2:
                    item = i
                    break
            sum_of_priorities += sum_priorities(item)
    print(f"The sum of priorities is {sum_of_priorities}")
    return 0

if __name__ == "__main__":
    main()