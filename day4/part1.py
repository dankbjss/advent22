def get_assignment_integers(line):
    assignments = line.strip().split(",")
    assignment_integers = []
    for assignment in assignments:
        no_hyphen = assignment.split("-")
        numbers = [int(number) for number in no_hyphen]
        assignment_integers += numbers
    
    return assignment_integers

def check_intersection_lengths(assignment_integers):
    section_one = [number for number in range(assignment_integers[0], assignment_integers[1] + 1)]
    section_two = [number for number in range(assignment_integers[2], assignment_integers[3] + 1)]
    intersection = list(set(section_one).intersection(section_two))
    if len(intersection) == len(section_one) or len(intersection) == len(section_two):
        return True

if __name__ == "__main__":
    count = 0
    with open("day4/input.txt", "r") as file:
        for line in file:
            assignment_integers = get_assignment_integers(line)
            if check_intersection_lengths(assignment_integers):
                count += 1
    print(count)