# ----------------------------------
#
# IPND Stage 2 Final Project
#
# ----------------------------------
# Norbert's Fill-in-the-Blanks Mercedes quiz
#
# Developer: Norbert Neuber

import random

# global
lev_list = ["easy", "medium", "hard"]  # list of levels
blank = "_"  # used by blanks and blank_l
blanks = blank * 2  # used to create the blank position i.e. __1__
blank_l = blank * 30  # used to print a seperation line
max_wrong = 5  # defines max wrong answers possible in the game
quiz_run = True  # if quiz_run is False the program stops

# Quiz questions and answers for each level
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


# list of potential random right respones.
right_res = ["You know Mercedes, Friend!",
             "Great Drive!",
             "The best or nothing, Buddy!"]

# list of potential random wrong respones.
wrong_res = ["Try again, Guy!",
             "Incorrect, Buddy!",
             "That was your personal 'Elchtest', Friend!"]


def level():
    """This function asks user for the level of difficulty
    and selcets the question and anwser for the quiz.

    Called by function:
    run(quiz_run)

    Starts function:
    quiz_session(level_feedback, easy_quiz, easy_answer)
    """
    level_feedback = " "
    while level_feedback not in lev_list:
        enter = "Enter a difficulty level: "
        levels = lev_list[0] + " / " + lev_list[1] + " / " + lev_list[2]
        question = ". What is your choice? "
        level_feedback = raw_input(enter + levels + question).lower()
    if level_feedback == lev_list[0]:  # easy
        quiz_session(level_feedback, easy_quiz, easy_answer)
    elif level_feedback == lev_list[1]:  # medium
        quiz_session(level_feedback, medium_quiz, medium_answer)
    elif level_feedback == lev_list[2]:  # hard
        quiz_session(level_feedback, hard_quiz, hard_answer)


def check_answer(u_answer, answer_list, session_answer):
    """This function checks user's answer. In case the
    answer is correct it gives back the position of the
    blank for the later replacement. In case the answer
    is incorrect it gives back "None".

    Called by function:
    quiz_session(level_feedback, quiz, answer_list)

    Keyword arguments:
    u_answer -- user_answer
    answer_list -- list with the correct answers
    session_answer -- list with given correct answers in this session
    """
    if u_answer not in session_answer:
        for answers in answer_list:
            if answers in u_answer:
                answer_index = answer_list.index(u_answer)
                session_answer.append(u_answer)
                blank_pos = blanks + str(answer_index + 1) + blanks
                return blank_pos
        return None
    else:
        return None


# replaces blanks i.e. __1__ with the checked answer
def replacement(quiz, res_check_ans, answer_correct):
    """This function replaces a blank with a correct answer.
    It gives back the question string with the replaced blank.

    Called by function:
    quiz_session(level_feedback, quiz, answer_list)

    Keyword arguments:
    quiz -- quiz string of this session
    res_check_ans -- blank position i.e. __1__
    answer_correct -- checked correct answer
    """
    if res_check_ans in quiz:
        quiz = quiz.replace(res_check_ans, answer_correct)
        return quiz


def play_again():
    """This function ask the user after a quiz, if
    he wants to play again. It gives back quiz_run False
    (end of quiz) or True (restart quiz)

    Called by function:
    end_quiz (success)

    Starts function:
    run(quiz_run)
    """
    yn = " "
    while yn != "y" and yn != "n":
        yn = raw_input("Do you want to play again? y/n   ").lower()
    if yn == "n":
        quiz_run = False
        run(quiz_run)
    else:
        quiz_run = True
        run(quiz_run)


def print_welcome():
    """Welcome print for the user

    Called by function:
    run(quiz_run)
    """
    print "\n", "Welcome!"
    print "This Quiz is about the history of Mercedes-Benz. Enjoy it!"
    print "You get " + str(max_wrong) + " changes to answer correctly"


def print_inital(level_feedback, quiz):
    """Quiz inital print for the user, after level selection

    Called by function:
    quiz_session(level_feedback, quiz, answer_list)

    Keyword arguments:
    level_feedback -- selected level by the user
    quiz -- quiz string of this session
    """
    print "\n", blank_l
    print "Here is your " + level_feedback.upper() + " quiz:", "\n", quiz


def print_right(right, u_answer, count_wrong, quiz):
    """Feedback print for the user after a turn. Depends if
    answer was correct or incorrect. Part of the feedback is
    random.

    Called by function:
    quiz_session(level_feedback, quiz, answer_list)

    Keyword arguments:
    right -- True: answer correct / False: answer incorrect
    u_answer -- user's answer
    count_wrong -- number of wrong tries
    quiz -- quiz string of this session
    """
    print "\n", blank_l
    if right is True:
        print random.choice(right_res), " '",  u_answer,  "' is correct! "
    elif right is False:
        print random.choice(wrong_res), " '",  u_answer,  "' is incorrect! "
    print str(count_wrong) + " / " + str(max_wrong) + " wrong answers"
    print quiz


def end_quiz(success):
    """The function prints feedback to the user at the
    end of a quiz. Either Congratulations or Game Over.

    Called by function:
    quiz_session(level_feedback, quiz, answer_list)

    Starts function:
    play_again()

    Keyword arguments:
    success -- True: all blanks filled in correct / False: incorrect
    """
    if success is True:
        print "\n", "Congratulations!"
        try_again = play_again()
    elif success is False:
        print "\n", "Game Over!"
        try_again = play_again()


def quiz_session(level_feedback, quiz, answer_list):
    """The function manages a quiz session. First it asks user for a
    answer. As a function of correctness of user's answer: In case
    answer is correct replacement() is started and print right. In
    case the answer isn't correct print wrong. count_wrong and count_right
    counts the correct and incorrect answers. While not all possible
    answers are given by the user and the user has still tries the quiz
    goes on. Otherwise the function end_quiz() will start.

    Called by function:
    level()

    Starts function:
    check_answer(u_answer, answer_list, session_answer)
    replacement(quiz, res_check_ans, u_answer)
    print_right(right, u_answer, count_wrong, quiz)
    end_quiz(success)

    Keyword arguments:
    level_feedback -- selected level by the user
    quiz -- quiz string of this session
    answer_list -- list with the correct answers
    """
    print_inital(level_feedback, quiz)
    session_answer = []  # is needed for filtering out answer duplicates
    count_wrong = 0  # var counts wrong answers
    count_right = 0  # var counts right answers
    while count_right < len(answer_list) and count_wrong < max_wrong:
        print
        u_answer = raw_input("Type in any right replacement: ").upper()
        print
        res_check_ans = check_answer(u_answer, answer_list, session_answer)
        if res_check_ans is not None:
            quiz = replacement(quiz, res_check_ans, u_answer)
            right = True
            print_right(right, u_answer, count_wrong, quiz)
            count_right += 1
            if count_right > len(lev_list):
                success = True
                end_quiz(success)
        else:
            count_wrong += 1
            right = False
            print_right(right, u_answer, count_wrong, quiz)
            if count_wrong == max_wrong:
                success = False
                end_quiz(success)


def run(quiz_run):
    """The inital function of this game. If quiz_run is True
    print_welcome() and level() are started. Else a Good Bye
    message will be presented and game will end.

    Starts function:
    print_welcome()
    level()

    Keyword arguments:
    quiz_run -- initally True. If quiz_run is False the program stops
    """
    if quiz_run is True:
        print_welcome()
        level_feedback = level()
    else:
        print "Heute kommt nichts mehr. Also abschalten, tschuess.", "\n"

run(quiz_run)
