# ----------------------------------
#
# IPND Stage 2 Final Project
#
# ----------------------------------
# Norbert's Fill-in-the-Blanks Mercedes quiz
#
# Developer: Norbert Neuber


# global
level_index_list = ["easy", "medium", "hard"]
blanks = "__"
max_wrong = 5

# Quiz questions and answers
easy_quiz = "Mercedes-Benz is a global __1__ manufacturer and a division " + \
            "of German company __2__ AG. The brand is known for luxury" + \
            " vehicles, buses, coaches, and trucks. The headquarters of" + \
            " __3__-Benz are in __4__, Baden-Wuerttemberg, Germany."
easy_answer = ["AUTOMOBILE", "DAIMLER", "MERCEDES", "STUTTGART"]

medium_quiz = "The first car. In __1__, Carl Benz is awarded German patent" + \
              " number 37435 for a __2__-wheeled, self-propelled " + \
              "'Motorwagen'. With a rear-mounted __3__-cylinder engine,  " + \
              "the first __4__ forever changes the way people move, and  " + \
              "sparks a legacy of innovation that continues to this day."
medium_answer = ["1886", "THREE", "SINGLE", "AUTOMOBILE"]

hard_quiz = "The first female driver: __1__ Benz, Carl's __2__, decided to" + \
            " help promote his invention by taking it on a 120-mile tour " + \
            "__3__ his prior knowledge. She also served as her own " + \
            "__4__ on the trip."
hard_answer = ["BERTHA", "WIFE", "WITHOUT", "MECHANIC"]


# asks user for level selection
def level():
    level_feedback = " "
    while level_feedback not in level_index_list:
        level_feedback = raw_input("Enter a difficulty level " + level_index_list[0] + " / " + level_index_list[1] + " / " + level_index_list[2] + ". What is your choice? ").lower()
    return level_feedback


# checks if the answer is correct and answer was not already used
def check_answer(user_answer, answer_list, session_answer):  
    if user_answer not in session_answer:
        for n in answer_list:
            if n in user_answer:
                answer_index = answer_list.index(user_answer)
                session_answer.append(user_answer)
                return answer_index
        return None
    else:
        return None


# replaces blanks i.e. __1__ with the checked answer
def replacement(quiz, blank_position_long, answer_correct):
    if blank_position_long in quiz:
        quiz = quiz.replace(blank_position_long, answer_correct)
        return quiz


# after the quiz session user can start the quiz again.
def play_again():
    yn = ""
    while yn != "y" and yn != "n":
        yn = raw_input("Do you want to play again? y/n   ").lower()
    if yn == "n":
        return False
    else:
        return True


# management active quiz_session
def quiz_session(quiz, answer_list):
    # inital print of the Quiz
    print
    print "Here is your " + level_feedback.upper() + " quiz:"
    print "--------------------"
    print quiz
    session_answer = []  # is needed for filtering out answer duplicates
    count_wrong = 0
    count_right = 0
    while count_right <= len(answer_list):
        print
        user_answer = raw_input("Type in any right replacement: ").upper()
        print
        result_check_answer = check_answer(user_answer, answer_list, session_answer)
        if result_check_answer is not None:
            blank_position_long = blanks + str(result_check_answer + 1) + blanks  # i.e. __1__
            quiz = replacement(quiz, blank_position_long, user_answer)
            print
            print "Great Job! '" + user_answer + "' is correct! "
            print str(count_wrong) + " / " + str(max_wrong) + " wrong answers"
            print "--------------------"
            print quiz
            count_right += 1
            if count_right > len(level_index_list):
                success = True
                return success
        else:
            count_wrong += 1
            print "Answer '" + user_answer + "' was not correct. Try again! "
            print str(count_wrong) + " / " + str(max_wrong) + " wrong answers"
            print "--------------------"
            print quiz
            if count_wrong == max_wrong:
                return False

# Big "Switch" - Here the games starts and ends
tryAgain = True
success = ""
while tryAgain is True:
    # This part is welcome and level selection
    print
    print "Welcome!"
    print "This Quiz is about the history of Mercedes-Benz. Enjoy it!"
    print "You can't give more than " + str(max_wrong) + " wrong answers!"
    print
    level_feedback = level()
    # leads to the right quiz level
    if level_feedback == level_index_list[0]:  # easy
        success = quiz_session(easy_quiz, easy_answer)
    if level_feedback == level_index_list[1]:  # medium
        success = quiz_session(medium_quiz, medium_answer)
    if level_feedback == level_index_list[2]:  # hard
        success = quiz_session(hard_quiz, hard_answer)
    # after the quiz
    if success is True:
        print
        print "Congratulations!"
        tryAgain = play_again()
    if success is False:
        print
        print 'Game Over!'
        tryAgain = play_again()
