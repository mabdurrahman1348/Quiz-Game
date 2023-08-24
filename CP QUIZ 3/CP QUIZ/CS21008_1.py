import random


def openfile():
    '''This function read all the content of the opened file, read it's content and print it's contents to user'''
    content = f.read()
    print(content)
    f.close()


def addques():
    '''This function append question with its choices and answer by taking inputs form user'''
    f.write('\n')
    q = input('Please enter question here:-')
    a = input('please enter option ''a'':-')
    b = input('please enter option ''b'':-')
    c = input('please enter option ''c'':-')
    d = input('Please enter option ''d'':-')
    ans = input('please enter the correct answer variable in terms of a,b or c:')
    x = ':- ' + q + ';a)' + a + ';b)' + b + ';c)' + c + ';d)' + d + ';' + ans
    f.write(x)
    f.close()


def quiz():
    '''This function reads question file, splits it's content by \n,
     prints the question and takes player's answer in input and if answer
      is wrong it prints 'Wrong answer :(' and if answer is correct it
      prints 'Correct answer :)' and adds a score'''
    count = 0
    content = f.read()
    lines = content.split('\n')
    random.shuffle(lines)
    for i in range(10):
        ques = (lines[i])
        ques = ques.split(';')
        print(f"Q{i + 1} {ques[0]}")
        print(ques[1])
        print(ques[2])
        print(ques[3])
        print(ques[4])
        ans = input('Enter answer:-')
        if ans.lower() == ques[5]:
            print('Correct answer :) ')
            count += 1
        else:
            print('Wrong answer :( ')
            print('Correct answer is:-', ques[5])
    f.close()
    print(username, 'your total score is:-', count)
    print('                                                     THANK YOU FOR PLAYING')
    s1 = open('CS21008_5.txt', 'a+')
    t = f'Player:- {username} his/her score is {count}.'
    s1.write(t)
    s1.write('\n')
    s1.close()


ua = input('You want to login,\nAs Player(#1) or as Admin(#2);\nEnter number:-')
if ua == '1':
    print('')
    print('''\n                                                  --------** Welcome to Quiz **--------''')
    username = input('Enter your name:-')
    print('Hey,', username, '!',
          '\n Lets get started with quiz \nFollowing are three categories to chose for quiz upon your personal '
          'interest;')
    print('Option#1-"Computer",', '\tOption#2-"Pakistan Studies",', '\tOption#3-"Science".')
    print('\n                                             --------** So let''s start quiz good luck **--------')
    o = input('Input option#:-')
    if o == '1':
        f = open("CS21008_2.txt")
        quiz()
    if o == '2':
        f = open('CS21008_3.txt')
        quiz()
    if o == '3':
        f = open('CS21008_4.txt')
        quiz()
    # elif o != '2' or o != '2' or o != '2':
    #     print('Invalid input run again ')
if ua == '2':
    print('Hello admin;')
    pw = input('Enter Password:-')
    if pw == '1234':
        print('Please enter which question do you want to edit or see:\n Option#1-"Computer",',
              '\tOption#2-"Pakistan Studies",', '\tOption#3-"Science",',
              '\tOption#4- "Players and their score".')
        bank = input('Enter Option#:-')
        if bank == '1':
            print('Please select an option\n a:View question bank\t\tb:Add question to bank')
            mode = input('Enter mode:')
            if mode == 'a':
                f = open('CS21008_2.txt')
                openfile()
            if mode == 'b':
                f = open('CS21008_2.txt', 'a+')
                addques()
        if bank == '2':
            print('Please select an option\n a:View question bank\t\tb:Add question to bank')
            mode = input('Enter mode:')
            if mode == 'a':
                f = open('CS21008_3.txt')
                openfile()
            if mode == 'b':
                f = open('CS21008_3.txt', 'a+')
                addques()
        if bank == '3':
            print('Please select an option\n a:View question bank\t\tb:Add question to bank')
            mode = input('Enter mode:')
            if mode == 'a':
                f = open('CS')
                openfile()
            if mode == 'b':
                f = open('CS21008_4.txt', 'a+')
                addques()
        if bank == '4':
            s = open('CS21008_5.txt', 'r')
            print(s.read())
        elif bank != '1' or bank != '2' or bank != '3' or bank != '4':
            print('Invalid input run again ')

    elif ua != '1' or ua != '2':
        print('Invalid input run again ')