from string import ascii_lowercase, ascii_uppercase

def get_compartments(line):
    stripped_line = line.strip()
    point_break = int(len(stripped_line) / 2)
    compartment_1 = stripped_line[0 : point_break]
    compartment_2 = stripped_line[point_break :]
    return [compartment_1, compartment_2]

def get_unique_item(compartments):
    first_compartment = [letter for letter in compartments[0]]
    second_compartment = [letter for letter in compartments[1]]
    unique_item_set = set([letter for letter in first_compartment if letter in second_compartment])
    unique_item = list(unique_item_set)[0]
    return unique_item

def get_letter_value(unique_item):
    if unique_item in ascii_lowercase:
        for index, letter in enumerate(ascii_lowercase):
            if unique_item == letter:
                return index + 1
    else:
        for index, letter in enumerate(ascii_uppercase):
            if unique_item == letter:
                return index + 27


if __name__ == "__main__":
    letter_values = []
    with open("day3/input.txt", "r") as file:
        for line in file:
            compartments = get_compartments(line)
            unique_item = get_unique_item(compartments)
            letter_value = get_letter_value(unique_item)
            letter_values.append(letter_value)
    print(sum(letter_values))
