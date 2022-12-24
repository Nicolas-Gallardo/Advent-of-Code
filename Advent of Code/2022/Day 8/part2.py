import math

def seen_trees(x,y,row,column):
    left_trees = 0
    right_trees = 0
    top_trees = 0
    bottom_trees = 0
    left = [i for i in row[0:x]]
    left.reverse()
    right = [i for i in row[x+1:len(row)]]
    top = [i for i in column[0:y]]
    top.reverse()
    bottom = [i for i in column[y+1:len(column)]]
    for i in left:
        if i < row[x]:
            left_trees += 1
        if i >= row[x]:
            left_trees += 1
            break
    for i in right:
        if i < row[x]:
            right_trees += 1
        if i >= row[x]:
            right_trees += 1
            break
    for i in top:
        if i < row[x]:
            top_trees += 1
        if i >= row[x]:
            top_trees += 1
            break
    for i in bottom:
        if i < row[x]:
            bottom_trees += 1
        if i >= row[x]:
            bottom_trees += 1
            break
    return [left_trees, right_trees, top_trees, bottom_trees]

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
    scores = []            
    for i in range(len(rows)):
        if i == 0 or i == len(rows)-1:
            continue
        for k in range(len(columns)):
            if k == 0 or k == len(columns)-1:
                continue
            scores.append(math.prod(seen_trees(k,i,rows[i],columns[k])))
    highest_score = max(scores)
    print(f"The highest score is {highest_score}")
    return 0

if __name__ == "__main__":
    main()