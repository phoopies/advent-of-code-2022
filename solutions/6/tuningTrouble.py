filename = "./solutions/6/data.txt"


def get_data(filename: str) -> str:
    with open(filename, "r") as f:
        return f.readline().strip()


def part1(signal: str, req_length=4) -> int:
    start_of_packet = ""
    rev_signal_list = [c for c in signal[::-1]]
    while len(start_of_packet) < req_length:
        c = rev_signal_list.pop()
        i = start_of_packet.find(c)
        if i >= 0:
            start_of_packet = start_of_packet[i + 1 :]
        start_of_packet += c
    print(start_of_packet)
    return len(signal) - len(rev_signal_list)


def part2(signal: str) -> int:
    return part1(signal, 14)


signal = get_data(filename)

print(part1(signal))
print(part2(signal))
