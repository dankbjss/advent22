from copy import deepcopy

def read_calories(input):
    all_elves_calories = []
    elf_calories = []

    for line in input:
        if line != "\n":
            elf_calories.append(int(line))

        else:
            all_elves_calories.append(deepcopy(elf_calories))
            elf_calories.clear()

    return all_elves_calories

def get_totals(elf_calories):
    totals = []

    for elf in elf_calories:
        totals.append(sum(elf))

    return totals
    
if __name__ == "__main__":
    with open("day1/input.txt", "r") as file:
        elf_calories = read_calories(file)
        totals = get_totals(elf_calories)
        print(max(totals))


