from part1 import get_assignment_integers

def check_for_any_overlap(assignment_integers):
    section_one = [number for number in range(assignment_integers[0], assignment_integers[1] + 1)]
    section_two = [number for number in range(assignment_integers[2], assignment_integers[3] + 1)]
    all_integers = list(section_one + section_two)
    unique_integers = set(all_integers)
    if len(all_integers) != len(unique_integers):
        return True


if __name__ == "__main__":
    count = 0
    with open("day4/input.txt", "r") as file:
        for line in file:
            assignment_integers = get_assignment_integers(line)
            if check_for_any_overlap(assignment_integers):
                count += 1
    print(count)