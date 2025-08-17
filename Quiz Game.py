questions=("How many elements are there in the periodic table?: ",
           "Which Animal lays the largest egg?: ",
           "What is the most abundant gas in Earth's Atmosphere?: ",
           "How many bone are there in human body?: ",
           "Which planet in the solar system is the hottest?: ")

options=(("A. 116", "B. 117", "C. 118", "D. 119"),
         ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
         ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
         ("A. 206", "B. 207", "C. 208", "D. 209"),
         ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answere=("C","D","A","A","B")
guesses=[]
score=0
question_num=0

for question in questions:
    print("----------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print("----------------------------------------------------------------")
        print(option)

    guess=input("Enter (A, B, C, D):  ").upper()
    guesses.append(guess)
    if guess== answere[question_num]:
        score+=1
        print("CORRECT")
    else:
        print(f"INCORRECT, THE CORRECT ANSWERE IS  {answere[question_num]}. ")

    question_num += 1

print("----------------------------------------------------------------")
print("                             RESULTS                            ")
print("----------------------------------------------------------------")

print("Answeres: ", end="")
for ans in answere:
    print(ans,end="")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess,end="")
print()
score=int(score / len(questions) *100)
print(f"{score}%")