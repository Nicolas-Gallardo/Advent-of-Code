from hands import *            

def main():
    
    file = "input.txt"
    me = Player()
    opponent = Player()
    with open(file) as f:
        for line in f:
            if 'A' in line:
                opponent.set_hand(Rock)
            elif 'B' in line:
                opponent.set_hand(Paper)
            elif 'C' in line:
                opponent.set_hand(Scissor)
            if 'X' in line:
                me.set_hand(Rock)
            elif 'Y' in line:
                me.set_hand(Paper)
            elif 'Z' in line:
                me.set_hand(Scissor)
            me.play_against(opponent)
    print(f'my final score is {me.score}')
    return 0

if __name__ == "__main__":
    main()