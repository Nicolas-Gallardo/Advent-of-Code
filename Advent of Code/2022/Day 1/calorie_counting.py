def main():
    input = open("input.txt","r")
    input_string = input.read() 
    input.close()
    x = input_string.split("\n\n")
    list_of_calories = []
    for i in range(len(x)):
        calories = x[i].split("\n")
        sum_of_calories = sum(list(map(int,calories)))
        list_of_calories.append(sum_of_calories)
    max_value = max(list_of_calories)    
    print(f"the most calories is {max_value}")
    return 0

if __name__ == "__main__":
    main()