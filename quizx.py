from art import *
import csv

tprint("Quizx", font="random")
print('Code by BHU_P3N')

# Initialize variables to store the score, question count, and applied questions
score = 0
question_count = 0
applied_questions = 0

options = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4
}

# Define a function to check if the answer is correct. If the answer is correct, it will print the correct answer
# and increment the score by 1. If the answer is wrong, it will display "Wrong answer" and increment the applied questions by 1.
def check_answer(guess, answer):
    global applied_questions, score
    if guess == answer:
        print('Correct answer')
        score += 1
    else:
        print('Sorry, wrong answer')

    applied_questions += 1

def show_score():
    print(f"Total score: {score}/{applied_questions}")

if __name__ == "__main__":
    print('Welcome to Quizx')

    with open("questions.csv", 'r') as csvfile:
        csvreader = csv.reader(csvfile)

        for row in csvreader:
            if question_count == 0:
                question_count += 1
            else:
                print(f"\n{row[0]}\n")
                for i in range(1, 5):
                    print(f"{i}. {row[i]}")
                print()

                correct_choice = False

                while not correct_choice:
                    guess = input("Type A, B, C, or D: ")
                    if guess.upper() in ['A', 'B', 'C', 'D']:
                        check_answer(row[options[guess.upper()]], row[5])
                        correct_choice = True

                question_count += 1

                if applied_questions == 10:
                    show_score()
                    play_again = input('Want to play again? (Y/N): ')
                    if play_again.upper() == 'N':
                        break
                    else:
                        question_count = 1
                        applied_questions = 0
                        score = 0

    if applied_questions != 10:
        show_score()

    tprint('Thank you!')
