from part1 import get_letter_value

def get_elf_groups(file):
    elves = [elf.strip() for elf in file]
    elf_groups = [elves[x : x+3] for x in range(0, len(elves), 3)]
    return elf_groups

def get_common_item(elf_group):
    common_item = list(
        set(elf_group[0]).intersection(
            elf_group[1], elf_group[2]
            )
        )
    return common_item[0]

if __name__ == "__main__":
    common_item_values = []
    with open("day3/input.txt", "r") as file:
        elf_groups = get_elf_groups(file)
        for elf_group in elf_groups:
            common_item = get_common_item(elf_group)
            common_item_values.append(get_letter_value(common_item))
    print(sum(common_item_values))
