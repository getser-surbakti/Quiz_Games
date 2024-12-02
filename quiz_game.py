


questions = [
    {
        "prompt" :"What is the capital of France?",
        "options" : ["A. Paris","B. London","C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt" : "What is the smallest prime nummber?",
        "options" : ["A. 1","B. 2","C. 3","D. 5"],
        "answer" : "B"
    },
    {
        "prompt":"What is the 7 divide by 0.5?",
        "options": ["A. 0.35","B. 14","C. 35","D. 7.5"],
        "answer":"B"
    }

] 

def run_quiz(questions):
    score=0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input("Enter your answer (A,B,C,D): ")
        if answer == question["answer"]:
            print("Correct!!\n")
            score +=1
        else:
            print("Incorrect!, The correct answer was", question["answer"], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)
