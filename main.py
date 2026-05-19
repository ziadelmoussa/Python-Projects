print("Welcome to Quiz App! \n")




questions = {
    "SCIENCE": [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["A. Gold", "B. Osmium", "C. Oxygen", "D. Helium"],
            "answer": "C"
        },
        {
            "question": "What gas do humans need to breathe in to survive?",
            "options": ["A. Nitrogen", "B. Carbon Dioxide", "C. Hydrogen", "D. Oxygen"],
            "answer": "D"
        },
        {
            "question": "What is the center of an atom called?",
            "options": ["A. Nucleus", "B. Electron", "C. Proton", "D. Neutron"],
            "answer": "A"
        },
        {
            "question": "How many states of matter are commonly studied (Solid, Liquid, Gas)?",
            "options": ["A. One", "B. Two", "C. Three", "D. Four"],
            "answer": "C"
        }
    ],
    "MATH": [
        {
            "question": "What is 5 multiplied by 6?",
            "options": ["A. 11", "B. 25", "C. 30", "D. 35"],
            "answer": "C"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
            "answer": "B"
        },
        {
            "question": "How many sides does a hexagon have?",
            "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
            "answer": "B"
        },
        {
            "question": "Solve this equation: 15 - (3 + 2)",
            "options": ["A. 10", "B. 14", "C. 5", "D. 12"],
            "answer": "A"
        },
        {
            "question": "What is the next number in this sequence: 2, 4, 6, 8, ...?",
            "options": ["A. 9", "B. 10", "C. 11", "D. 12"],
            "answer": "B"
        }
    ],
    "GEOGRAPHY": [
        {
            "question": "What is the capital of France?",
            "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
            "answer": "D"
        },
        {
            "question": "Which country is famous for its pyramids?",
            "options": ["A. Italy", "B. Mexico", "C. Egypt", "D. Greece"],
            "answer": "C"
        },
        {
            "question": "What is the tallest mountain above sea level in the world?",
            "options": ["A. Mount Kilimanjaro", "B. Mount Everest", "C. K2", "D. Mount Fuji"],
            "answer": "B"
        },
        {
            "question": "Which continent is the South Pole located on?",
            "options": ["A. Africa", "B. Asia", "C. Antarctica", "D. Australia"],
            "answer": "C"
        }
    ]
}

available_categories = list(questions.keys())

valid_options = ["A", "B", "C", "D"]

def game():
    
    score = 0
    
    
    for num, cat in enumerate(available_categories, 1):
        print(f"{num}. {cat}")
    print("")
    
    
    
    while True:
        try:
            choice = int(input("Enter the category number: "))
            if 1<= choice <= len(available_categories):
                selected_cat = available_categories[choice - 1]
                break
            else:
                 print(f"Please enter a number between 1 and {len(available_categories)}.\n")
        except ValueError:
            print("Invalid input! Please enter a number.\n")
            
            
    print(f"\n--- Starting {selected_cat} Quiz ---\n")
    
    
    
    active_questions = questions[selected_cat]
    
    for num, item in enumerate(active_questions, 1):
        print(f"Question {num}: {item['question']}")
        
        
        for option in item['options']:
            print(option)
        
        
            
        print("")
        
        
        while True:
            answer = input("Enter your answer: ")
            
            if answer.upper() not in valid_options:
                print("Enter an option from the given")
            else:
                break
        
    
        
        if answer.upper() == item['answer']:
            print("Your answer is correct!\n")
            score += 1
        else:
            print(f"Your answer is incorrect, the answer is {item['answer']}.\n")
            
            
    print("Quiz Finshed!\n")
    print(f"Your score is {score}/5\n")
    print(f"Your percentage is {(score/5)*100}%\n")
    
    
def reset_game():
    while True:
        game()
        
        while True:
            play_again = input("Want to play again ? (Y/N): ")
            
            if play_again.upper() == "Y":
                print("\nStarting a new game...\n")
                break
            elif play_again.upper() == "N":
                print("\nGoodbye!")
                return
            else:
                print("Enter a valid letter!")


reset_game()
