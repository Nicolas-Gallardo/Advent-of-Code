def is_visible(x,y,row,column):
    max_height_left = max(row[0:x])
    max_height_right = max(row[x+1:len(row)])
    max_height_top = max(column[0:y])
    max_height_bottom = max(column[y+1:len(column)])
    if row[x]<=max_height_left and row[x]<=max_height_right and \
        row[x]<=max_height_top and row[x]<=max_height_bottom:
        return False
    return True

def main():
    file = "input.txt"
    rows = []
    columns = []
    with open(file) as f:
        for line in f:
            row_str = line.replace("\n","")
            row_int = [int(i) for i in row_str]
            rows.append(row_int)
            if len(columns) == 0:
                columns = [[i] for i in row_int]
                continue
            for i in range(len(row_int)):
                columns[i].append(row_int[i])
    trees_visible = len(rows)*2 + (len(columns)-2)*2
    for i in range(len(rows)):
        if i == 0 or i == len(rows)-1:
            continue
        for k in range(len(columns)):
            if k == 0 or k == len(columns)-1:
                continue
            if is_visible(k,i,rows[i],columns[k]):
                trees_visible += 1
    print(f"There are {trees_visible} trees visible from outside")
    return 0

if __name__ == "__main__":
    main()