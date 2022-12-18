def main():
    file = "input.txt"
    stacks = [[]]
    n_stacks = 0
    height = 0
    with open(file) as f:
        # With this for you obtain la cantidad de stacks and
        # the max height 
        for line in f:
            if "1" in line:
                line = line.replace("\n","")
                line = line.replace(" ","")
                n_stacks = max(list(map(int,[x for x in line])))
                break
            height += 1
        f.seek(0,0)
        # With this for it is filled the list of stacks with empty stacks
        for i in range(n_stacks-1): 
            stacks.append([])
        # Here every stack is filled
        for k in range(height):
            for i in range(n_stacks):
                crate = f.read(3)
                x = f.read(1)
                if (x == "\n" and " " in crate) or (" " in crate): 
                    continue
                crate = crate[1]
                stacks[i].append(crate)
        # The elements are reversed for an easy manipulation like a stack LIFO
        for i in stacks:
            i.reverse()
        stacks2 = [i.copy() for i in stacks] #stack for part2
        # Applying the instructions
        for line in f:
            inst = line.split(" ")
            if inst[0] == "move":
                n = int(inst[1])
                fromm = int(inst[3])-1
                to = int(inst[5])-1
                x = []
                for i in range(n):
                    stacks[to].append(stacks[fromm].pop())
                    x.append(stacks2[fromm].pop())
                x.reverse()    
                stacks2[to].extend(x)
                x.clear()
        # Writting the message
        msg1 = ""
        msg2 = ""
        for i in stacks:
            msg1 += str(i.pop())
        for i in stacks2:
            msg2 += str(i.pop())
        print(f"The message for Part 1 is {msg1}")
        print(f"The message for Part 2 is {msg2}")
    return 0
if __name__ == "__main__":
    main()