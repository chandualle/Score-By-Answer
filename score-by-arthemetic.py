import random
import time


def home():
    min_value = 1
    max_value = 4
    digits = random.randint(min_value, max_value)
    return digits

def get_numeric_input(prompt):
    while True:
        value = input(prompt + " ")
        if value.lstrip('-').isdigit():
            return int(value)
        else:
            print(value + " is not a number. Please enter a valid number.")

min_value = get_numeric_input("Enter Minimum Value:")
max_value = get_numeric_input("Enter Maximum Value:")
totalQuestions = get_numeric_input("How many questions:")
operators = ["+", "-", "*"]

def problem_generator():
    lowerNumber = random.randint(min_value, max_value)
    higherNumber = random.randint(min_value, max_value)
    take_operator = random.choice(operators)

    problem = str(lowerNumber) + " " + take_operator + " " + str(higherNumber)
    solution = eval(problem)
    return solution, problem


wrongAnswers = 0
startTime = time.time()
players = get_numeric_input("Enter number of players: ")

max_score = 4
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    for players_index in range(players):
        if players_scores[players_index] >= max_score:
            break

        print("Player Number", players_index + 1, "ready to play\n")
        print("Your present score is", players_scores[players_index], "\n")

        for i in range(totalQuestions):
            answer, problem = problem_generator()
            while True:
                userAnswer = input("Question is" + " " + problem + " " + "and Your answer is" + " : ")
                if userAnswer.lstrip('-').isdigit():
                    userAnswer = int(userAnswer)

                    if userAnswer == answer:
                        print("Yeah! Your Answer Is Correct")
                        break
                    elif userAnswer < answer:
                        print("You guessed a lower number")
                    else:
                        print("You guessed a higher number")
                    wrongAnswers += 1
                else:
                    print("Please enter a number")

            ready_play = input("You are ready to play (press 'S'): ")
            if ready_play.lower() != "s":
                break
            value1 = home()

            if value1 == 1:
                print("You got 1 and your score for this round is 0")
                present_score = 0
            elif value1 == 4:
                present_score = present_score + 2 * value1
                print("Yeah! You Got 4 and It means You got 8.. Your present score is:", present_score)
            else:
                present_score += value1
                print("You rolled value:", value1)
            print("Your present score is:", present_score)

            players_scores[players_index] += present_score

high_score = max(players_scores)
winning_player = players_scores.index(high_score) + 1

print("The game winner is Player", winning_player, "with a score of", high_score)
