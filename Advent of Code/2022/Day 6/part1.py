def marker(s:str, dc:int) -> int:
    for i in range(len(s)):
        seq = s[i:i+dc]
        for k in seq: 
            if seq.count(k) >= 2:
                break
            if k == seq[dc-1]:
                return i+dc

def start_of_packet_marker(s:str) -> int:
    return marker(s,4)

def start_of_message_marker(s:str) -> int:
    return marker(s,14)
    
def main():
    file = "input.txt"
    signal = ""
    with open(file) as f:
        signal = f.read()
    packet_marker = start_of_packet_marker(signal)
    message_marker = start_of_message_marker(signal)
    print(f"First packet marker after character {packet_marker}")
    print(f"First message marker after character {message_marker}")
    return 0

if __name__ == "__main__":
    main()

