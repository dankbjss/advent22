def get_message_start_marker(line):
    for index, _ in enumerate(line):
        packet = [letter for letter in line[index : index + 14]]
        unique_packet_characters = list(set(packet))
        if len(packet) == len(unique_packet_characters):
            return f"{packet}, {index + 14}" 

if __name__ == "__main__":
    with open("day6/input.txt", "r") as file:
        line = file.readline()
    print(get_message_start_marker(line))