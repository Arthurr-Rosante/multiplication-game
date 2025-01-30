import os
import random
import time

def clear_screen(delay=0):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    """ Displays the main menu for the game. """

    while True:
        clear_screen()
        print('\n| Multiplication Table |')
        print('| Start (1) | Quit (0) |')
        choice = input("Enter your Choice: ").strip()

        if choice == '0':
            print('Goodbye!')
            exit(0)
        elif choice == '1':
            choose_difficulty()
            break
        else:
            print('Invalid choice. Please enter (1) to Start or (0) to Quit.')

def choose_difficulty():
    """Prompts the user to select a difficulty level."""

    while True:
        clear_screen()
        print("\n| Choose a Game Mode             |")
        print("| Easy (1) | Base (2) | Hard (3) |")
        difficulty = input("Select difficulty: ").strip()

        if difficulty in ('1', '2', '3'):
            play_game(difficulty)
        else:
            print('Invalid difficulty. Please choose 1, 2 or 3.')

def play_game(difficulty: str):
    """Runs the game based on the selected difficulty."""

    diff = int(difficulty)
    num_phases = 10 + diff
    scores = []

    for i in range(0, num_phases):
        n1 = random.randint(0, diff * 10)
        n2 = random.randint(0, diff * 10)
        answer = n1 * n2

        try:
            user_answer = int(input(f"[{i+1}/{num_phases}]          | {n1} x {n2} | Answer: ").strip())
        except ValueError:
            print("\n Invalid Input | proceeding...")
            continue
        
        is_correct = user_answer == answer
        scores.append({
            "nums": [n1, n2],
            "answer": answer,
            "given_answer": user_answer,
            "result": int(is_correct)
        })

        if is_correct:
            print("\n(V) Correct Answer!")
        else:
            print(f"\n(X) Incorrect | Right Answer: {answer}")
        clear_screen(delay=0.25)

    total_questions = len(scores)
    correct_answers = sum(entry["result"] for entry in scores)
    accuracy = (correct_answers / total_questions * 100) if total_questions > 0 else 0

    print(f"""
    | Statistics                        
    |--------------------------
    | Total Questions   : {total_questions} 
    | Right Answers     : {correct_answers} 
    | Accuracy          : {accuracy:.2f}% 
    """)
    
    while True:
        clear_screen()
        keep_playing = input('\n| Would you like to keep playing? |\n| Play Again (1) | Quit(0) |\n');
        if keep_playing == '1':
           return
        elif keep_playing == '0':
            print('Thanks for playing, Goodbye!')
            exit(0)
        else:
            print('Invalid Choice. Please enter (1) to play again or (0) to quit.')
            time.sleep(1)


if __name__ == '__main__':
    main_menu()