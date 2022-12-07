from part1 import ROCK, PAPER, SCISSORS, convert_letter_to_shape, get_round_outcome

LOSE = "lose"
DRAW = "draw"
WIN = "win"

def convert_letter_to_outcome(letter):
    if letter == "X":
        return LOSE
    elif letter == "Y":
        return DRAW
    else:
        return WIN

def get_rock_choice(desired_outcome):
    if desired_outcome == LOSE:
        return SCISSORS
    elif desired_outcome == DRAW:
        return ROCK
    else:
        return PAPER

def get_paper_choice(desired_outcome):
    if desired_outcome == DRAW:
        return PAPER
    elif desired_outcome == LOSE:
        return ROCK
    else:
        return SCISSORS

def get_scissors_choice(desired_outcome):
    if desired_outcome == WIN:
        return ROCK
    elif desired_outcome == LOSE:
        return PAPER
    else:
        return SCISSORS

def get_player_choice(opponent_shape, desired_outcome):
    if opponent_shape == ROCK:
        return get_rock_choice(desired_outcome)
    elif opponent_shape == PAPER:
        return get_paper_choice(desired_outcome)
    else:
        return get_scissors_choice(desired_outcome)

def get_player_shape_score(player_shape):
    if player_shape == ROCK:
        return 1
    elif player_shape == PAPER:
        return 2
    else:
        return 3

def get_round_score(line):
    opponent_shape = convert_letter_to_shape(line[0])
    desired_outcome = convert_letter_to_outcome(line[2])
    player_shape = get_player_choice(opponent_shape, desired_outcome)
    outcome = get_round_outcome(opponent_shape, player_shape)
    player_shape_score = get_player_shape_score(player_shape)
    total = outcome + player_shape_score

    return total

if __name__ == "__main__":
    rounds = []
    with open("day2/input.txt", "r") as file:
        for line in file:
            round = get_round_score(line)
            rounds.append(round)
    
    print(sum(rounds))