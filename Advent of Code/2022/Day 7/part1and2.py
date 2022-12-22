from filesystem import *
from pathlib import Path

def main():
    dir = Directory("/")
    cmd = CommandPrompt(dir)
    file = "input.txt"
    with open(file) as f:
        command = ""
        for line in f:
            strs = line.split()
            if line[0] == "$":
                command = strs[1]
            if command == "cd":
                folder = strs[2]
                cmd.cd(folder)
                command = ""
            elif command == "ls":
                if line[0] == "$":
                    continue
                if strs[0] == "dir":
                    folder = strs[1]
                    cmd.md(folder)
                else:
                    size = int(strs[0])
                    name = strs[1]
                    cmd.touch(name,size) 
    print(f"The sum of the sizes of at most 100000 is {dir.sum_sizes_lte(100000)}")
    print(f"The size of the directory to delete is {dir.search_dir_for_update()}")
    return 0

if __name__ == "__main__":
    main()