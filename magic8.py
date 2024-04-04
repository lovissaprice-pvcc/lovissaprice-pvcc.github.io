#NAME: Lovissa Price
#   Prog purpose: This Magic 8-Ball code uses a Python tuple since the
#   user does not have the ability to change the 8-Ball answers.
#   However, the program could have used a Python list instead of a tuple.
#   NOTE: Tuples use parentheses; lists use square brackets

import random
answer_8_ball = ("as I see it, yes", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again", "don't count on it", "it is certain", "it is decidedly so", "most likely", "my reply is no", "my sources say no", "outlook good", "outlook not so good", "reply hazy, try again", "signs point to yes", "without a doubt", "yes", "you may rely on it", "keep dreaming", "absolutely!")

def main():

    print("I am the MAGIC-8 BALL and can answer any YES or NO questions!")

    another_question = True
    while another_question:
        answer = random.choice(answer_8_ball)

        print("\nShake the MAGIC-8 BALL")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("the MAGIC-8 BALL says " + answer)

        askAgain = input("\nWould you like to ask me another question?")
        if askAgain.upper() == "N" or askAgain == "n":
            another_question = False

    print("\nCome back again when you have other important questions...")
    print("...Magic-8 Ball OUT.")

main()
