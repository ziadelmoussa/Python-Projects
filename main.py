print("Welcome to Quiz App! \n")

score = 0;

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
        "answer": "B"
    },
    
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    
        {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    
    {
        "question": "How many bones are there in an adult human body?",
        "options": ["A. 106", "B. 206", "C. 306", "D. 406"],
        "answer": "B"
    },
    
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["A. Gold", "B. Osmium", "C. Oxygen", "D. Helium"],
        "answer": "C"
    }

]

for num, item in enumerate(questions, 1):
    print(f"Question {num}: {item['question']}")
    
    
    for option in item['options']:
        print(option)
        
    print("")
    answer = input("Enter your answer: ")
    
    
    
    if answer.upper() == item['answer']:
        print("Your answer is correct!\n")
        score += 1
    else:
        print(f"Your answer is incorrect, the answer is {item['answer']}.\n")
        
        
print("Quiz Finshed!\n")
print(f"Your score is {score}/5\n")
print(f"Your percentage is {(score/5)*100}%")
