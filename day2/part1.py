# rock, paper, scissors

ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"

def convert_letter_to_shape(letter):
    if letter in ["A", "X"]:
        return "rock"
    elif letter in ["B", "Y"]:
        return "paper"
    elif letter in ["C", "Z"]:
        return "scissors"
    else:
        pass

def get_round_outcome(opponent, player):
    # lose
    if opponent == PAPER and player == ROCK:
        return 0
    elif opponent == SCISSORS and player == PAPER:
        return 0
    elif opponent == ROCK and player == SCISSORS:
        return 0
    # win
    elif opponent == ROCK and player == PAPER:
        return 6
    elif opponent == PAPER and player == SCISSORS:
        return 6
    elif opponent == SCISSORS and player == ROCK:
        return 6
    # draw
    else:
        return 3

def get_shape_score(letter):
    if letter == "X":
        return 1
    elif letter == "Y":
        return 2
    else:
        return 3

def get_total(line):
    opponent = convert_letter_to_shape(line[0])
    player = convert_letter_to_shape(line[2])
    round_outcome = get_round_outcome(opponent, player)
    shape_score = get_shape_score(line[2])
    total = round_outcome + shape_score

    return total

if __name__ == "__main__":
    rounds = []
    with open("day2/input.txt", "r") as file:
        for line in file:
            round = get_total(line)
            rounds.append(round)
    
    print(sum(rounds))