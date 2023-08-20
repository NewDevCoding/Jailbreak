current_score = 0
answered_questions = 0
to_go = 10 - answered_questions
underscore = '--------------------'
congrat_message = 'Congragulations! That is the correct answer!'
fail_message = 'Sorry, incorrect answer.'

congrat_messages = ['We have a winner!', 'You got it!', 'You are on a roll!', 'That is correct!', 'Congragulations, you are right!']


def question1():
    print('Question 1:')
    print('Who was the 17th president of the United States?')
    print(underscore)
    print('A: George Washington')
    print('B: Joe Biden')
    print('C: Andrew Jackson')
    print('D: Millard Fillmore')

def question2():
    print('Question 2:')
    print('When did Neil Armstrong land on the moon?')
    print(underscore)
    print('A: 1957')
    print('B: 1969')
    print('C: 1945')
    print('D: 2023')

def question3():
    print('Question 3:')
    print('What was Justin Biebers first hit song?')
    print(underscore)
    print('A: Baby')
    print('B: All around the world')
    print('C: Kings and Queens')
    print('D: 2 much')

def question4():
    print('Question 4')
    print('Where was the first atomic bomb dropped on Japan?')
    print(underscore)
    print('A: Tinian')
    print('B: Fukishima')
    print('C: Nagasaki')
    print('D: Hiroshima')


def question5():
    print('Question 5')
    print('Who founded Microsoft?')
    print(underscore)
    print('A: Steve Jobs')
    print('B: Bill Gates')
    print('C: Millard Fillmore')
    print('D: Henry Ford')

def question6():
    print('Question 6')
    print('Who Was Meriwether Lewis partner?')
    print(underscore)
    print('A: Clark Kent')
    print('B: Daniel Boone')
    print('C: William Clark')
    print('D: Elmo')

def question7():
    print('Question 7')
    print('Which state was the Alamo located?')
    print(underscore)
    print('A: New york')
    print('B: Texas')
    print('C: New Mexico')
    print('D: Californa')

def question8():
    print('Question 8')
    print('Who lead the Haitian Revolution?')
    print(underscore)
    print('A: Toussaint L`ouverture')
    print('B: The Bolsheviks')
    print('C: Lafayette')
    print('D: King Henry V')

def question9():
    print('Question 9')
    print('Who founded the crypto exchange FTX?')
    print(underscore)
    print('A: Mark Zuckerberg')
    print('B: Rasputin')
    print('C: Warren Buffet')
    print('D: Sam Bankman Fried')

def question10():
    print('Question 10')
    print('Where was the original capitol of the USA?')
    print(underscore)
    print('A: Roswell, New Mexico')
    print('B: Philidelphia, Pensylvania')
    print('C: Washington DC, Virginia')
    print('D: Newark, New Jersey')

def question11():
    print('Question 11')
    print('What is the correct ratio for the Sine of a triangle?')
    print(underscore)
    print('A: Opposite/Adjacent')
    print('B: Adjacent/Hypotenuse')
    print('C: Opposite/Hypotenuse')
    print('D: Hypotenuse/Adjacent')

def question12():
    print('question 12')
    print('What company created Monopoly?')
    print(underscore)
    print('A: Hasbro')
    print('B: Avalon Hill')
    print('C: Parker Brothers')
    print('D: Days of Wonder')

def question13():
    print('Question 13')
    print('What is the first book of the New Testament?')
    print(underscore)
    print('A: Leviticus')
    print('B: Mark')
    print('C: Genesis')
    print('D: Matthew')

def question14():
    print('Question 14')
    print('When did the Soviet Union collapse?')
    print(underscore)
    print('A: 1991')
    print('B: 1975')
    print('C: 1992')
    print('D: 1945')

def question15():    
    print('Question 15')
    print('What other company did the founder of Tesla create?')
    print(underscore)
    print('A: Blue Origin')
    print('B: Rivian')
    print('C: Amazon')
    print('D: Space X')


            


print('Welcome to Who Wants to be a Millionaire!!')
print('You will be presented with 15 questions. You are required to answer at least 10 of them. Any others you answer correctly will give you bonus cash, but if you answer incorrectly you will be penalized.')
print('--------------------')
print('Please enter "begin game" to start')
print('--------------------')

user_input = input()
if user_input == 'begin game':
    question1()

answer_question1 = input()

if answer_question1 == 'C':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question2()
answer_question2 = input()

if answer_question2 == 'B':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question3()
answer_question3 = input()

if answer_question3 == 'A':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question4()
answer_question4 = input()

if answer_question4 == 'D':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)


question5()
answer_question5 = input()

if answer_question5 == 'B':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)


question6()
answer_question6 = input()

if answer_question6 == 'C':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question7()
answer_question7 = input()

if answer_question7 == 'B':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question8()
answer_question8 = input()

if answer_question8 == 'A':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question9()
answer_question9 = input()

if answer_question9 == 'D':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question10()
answer_question10 = input()

if answer_question10 == 'B':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question11()
answer_question11 = input()

if answer_question11 == 'C':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question12()
answer_question12 = input()

if answer_question12 == 'C':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question13()
answer_question13 = input()

if answer_question13 == 'D':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question14()
answer_question14 = input()

if answer_question14 == 'A':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

question15()
answer_question15 = input()

if answer_question15 == 'D':
    print(congrat_message)
    current_score += 1
    print('Current score: ' + str(current_score))
    print(underscore)
else:
    print(fail_message)
    current_score -= 1
    print('Current score: ' + str(current_score))
    print(underscore)

total_prize = current_score * 1000

if total_prize < 0:
    print('Sorry, no prize for you. You earned negative points')
else:
    print('Congragulations! You earned $' + str(total_prize) + ' dollars!')