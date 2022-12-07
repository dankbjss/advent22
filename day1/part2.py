from day1.part1 import read_calories, get_totals


if __name__ == "__main__":
    with open("day1/input.txt", "r") as file:
        elf_calories = read_calories(file)
        totals = get_totals(elf_calories)
        totals.sort(reverse=True)
        print(sum(totals[0:3]))