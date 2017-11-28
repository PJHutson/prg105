import questions        # importing questions file


def main():         # make questions
    q1 = questions.Question("What is 2+2?", "A. fish", "B. 5", "C. 4", "D. All of the above", "C")
    q2 = questions.Question("What is the best food ever created?", "A. pizza", "B. sushi", "C. cheeseburger", "D. Spaghetti", "A")
    q3 = questions.Question("What is the capital of Illinois?", "A. chicago", "B. crystal lake", "C. springfield", "D. nashville", "C")
    q4 = questions.Question("What sport do the Packers play?", "A. baseball", "B. football", "C. hockey", "D. tennis", "B")
    q5 = questions.Question("Who is our current president?", "A. Obama", "B. George W. Bush", "C. Teddy Roosevelt", "D. Trump", "D")
    q6 = questions.Question("What does, Je parler en Francais, mean?", "A. I speak French", "B. I am French", "C. I love French", "D. Nothing", "A")
    q7 = questions.Question("What country is Illinois part of?", "A. Canada", "B. USA", "C. Mexico", "D. China", "B")
    q8 = questions.Question("What country touches the USA?", "A. Russia", "B. Thailand", "C. Canada", "D. Brazil", "C")
    q9 = questions.Question("Who did Trump beat for the presidency?", "A. Clinton", "B. The Rock", "C. Romney", "D. Obama", "A")
    q10 = questions.Question("What is Meijer?", "A. A food brand", "B. A school", "C. A computer", "D. A retail store", "D")
    player1 = 0     # initial scores set to 0
    player2 = 0

    set_1 = [q1, q3, q5, q7, q9]        # sets of questions
    set_2 = [q2, q4, q6, q8, q10]

    print("player1: ")      # giving player 1 set 1
    for query in set_1:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter for your answer: ").upper().strip(" ")
        if guess == query.get_answer():
            print("You're right!")          # if correct then print so
            player1 += 1
            print("Player 1 earned:", str(player1), "point(s).")
    print("player2: ")
    for query in set_2:
        print("\n")
        print(query.get_question())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter for your answer: ").upper().strip(" ")
        if guess == query.get_answer():
            print("You're right!")
            player2 += 1
    print("Player 2 earned:", str(player2), "point(s).")

main()
