#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.
import random
# The quiz data. Keys are states and values are their capitals.

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany',
   'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'}
'''
   # Generate 35 quiz files. 
for quizNum in range(3):
       # TODO: Create the quiz and answer key files.
    quizFile  = open(f'capitalsQuiz{quizNum+1}.txt','w')
    answerKey = open(f'answerkey{quizNum+1}.txt','w')

       # TODO: Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((''*20)+(f'State Capital Quiz (form{quizNum+1})'))
    quizFile.write('\n\n')
       # TODO: Shuffle the order of the states.

    states = list(capitals.keys())
    random.shuffle(states)
       # TODO: Loop through all 50 states, making a question for each.

    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers  = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = [correctAnswer] + wrongAnswers
        random.shuffle(answerOptions)
        # TODO: Write the question and answer options to the quiz file.
        quizFile.write(f'{questionNum+1}. What is the Capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}.{answerOptions[i]}\n")
        quizFile.write('\n')

        # TODO: Write the answer key to a file.
        answerKey.write(f" {questionNum + 1}.{'ABCD'[answerOptions.index(correctAnswer)]}")
    quizFile.close()
    answerKey.close()
'''

#Generates 35 quiz Files
for quizNum in range(35):
    #Answer Files
    qfile  = open(f'quizfile{quizNum+1}.txt', 'w')
    answer = open(f'Answer Key {quizNum+1}.txt', 'w')
    
    #Write the header of the Quiz
    qfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    qfile.write((''*20)+(f'Capitals Quiz Form {quizNum+1}'))
    
    #Shuffle state orders
    statenew = list(capitals.keys())
    random.shuffle(statenew)
    
    #loop through 50 states and make question for each
    for questionNum in range(50):
        correctAnswers = capitals[statenew[questionNum]]
        wrongAnswerss = list(capitals.values())
        del wrongAnswerss[wrongAnswerss.index(correctAnswers)]
        
        wrongAnswerss = random.sample(wrongAnswerss,3)
        AOptions = [correctAnswers] + wrongAnswerss
        random.shuffle(AOptions)
        #write the questions and answers to the file 
        qfile.write(f'{questionNum+1}. What is the Capital of {statenew[questionNum]}? \n')

        for i in range(4):
            qfile.write( f"{'ABCD'[i]}.{AOptions[i]} \n")

        qfile.write('\n')

        #answer file

        answer.write(f"{questionNum+1}.{'ABCD'[AOptions.index(correctAnswers)]}\n")
    answer.close()
    qfile.close()