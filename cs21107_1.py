# The password for admin is fatima..........
# CS-107-MUHAMMAD ABDURRAHMAN
# CS-002-FATIMA SIDDIQUI
# CS-014-BARIRA BABAR

# ----------------------------------------------------------------------------------
import random


def quizz():
    '''This functions reads the file content,shuffles the file,prints question and options in different lines
     and then update score of players.It also tells whether the answer is correct or wrong'''
    content = f.read()
    content = content.split('\n')
    random.shuffle(content)
    count = 0
    for i in range(10):
        ques = content[i]
        ques = ques.split(';')
        print(f"Q{i + 1}{ques[0]}")
        print(f"a){ques[1]}")
        print(f"b){ques[2]}")
        print(f"c){ques[3]}")
        ans = input("Please Enter Answer in terms of a,b or c:")
        ans=ans.lower()
        if ans == ques[4]:
            print('Correct')
            count += 1
        else:
            print('Wrong')
            print('The correct answer is :', ques[4])
    print('Your total score is :', count)
    print('Thanks for playing', yourname, 'have a good day...')
    f.close()


def addques():
    '''This function asks admin if he/she wants to add questions in the file.
    After appending question it also asks the admin if he/she want to view the question bank again'''
    f.write('\n')
    q = input('Please enter your question here:')
    a = input('please enter your first option:')
    b = input('please enter your second option:')
    c = input('please enter third option:')
    ans = input('please enter the correct answer variable in terms of a,b or c:')
    x = ': ' + q + ';' + a + ';' + b + ';' + c + ';' + ans
    f.write(x)
    print('Your Question is added successfully!')
    view = input('\t\t\t\t\t\t\t\t\t\tDo you want to see changes?\n\t\t\t\t\t\t\t\t\ta)Yes\t\t\t\t\t\t\tb)No\n:')
    view=view.lower()
    if view == 'a':

        f.seek(0)
        content = f.read()
        content = content.split('\n')
        count = 1
        for i in content:
            ques = i.split(';')
            print((f"Q{count}{ques[0]}"))
            print(f"a){ques[1]}")
            print(f"b){ques[2]}")
            print(f"c){ques[3]}")
            print(f"Ans={ques[4]}")
            count += 1
        f.close()
    else:
        quit()
    f.close()


def view_file():
    '''This function is used to view the question bank.'''
    content = f.read()
    content = content.split('\n')
    count = 1
    for i in content:
        ques = i.split(';')
        print((f"Q{count}{ques[0]}"))
        print(f"a){ques[1]}")
        print(f"b){ques[2]}")
        print(f"c){ques[3]}")
        print(f"Ans={ques[4]}")
        count += 1
    f.close()


yourname = input('PLEASE ENTER YOUR NAME:')
yourname=yourname.upper()
print('\t\t\t\t\t\t\t-------------WELCOME TO THE QUIZZ GAME:',yourname,'-------------')
print('\t\t\t\t\t\t\t\t\t\t\t\tPLEASE SELECT A MODE:')
print('\t\t\t\t\t\t\t\ta:PLAYER:\t\t\t\t\t\t\t\tb:ADMIN:')
print('')
mode = input('ENTER THE MODE IN TERMS OF :(a) OR :(b):')
mode=mode.lower()
if mode == 'a':
    print('\t\t\t\t\t\t\t\t\t\t\tSELECT THE AREA YOU WANT TO PLAY IN:')
    print('\t\t\t\t\t\t\t\ta: GENERAL KNOWLEDGE\t\t\t\t\t\t\t\tb: SPORTS')
    print('')
    mode = input('ENTER YOUR CHOICE IN TERMS OF a OR b:')
    print('')
    mode = mode.lower()
    if mode == 'a':
        print('\t\t\t\t\t\t\t\t\t\t\tWELCOME TO GENERAL KNOWLEDGE QUIZZ:')
        print('')
        f = open('cs21107_3.txt')
        quizz()
    elif mode == 'b':
        print('\t\t\t\t\t\t\t\t\t\t\tWELCOME TO THE SPORTS QUIZZ:')
        print('')
        f = open('cs21107_2.txt')
        quizz()
    else:
        print('Inappropriate command please run again')
        quit()
elif mode == 'b':
    print('\t\t\t\t\t\t  -------------HEY', yourname, 'WELCOME TO THE ADMIN PANEL!-----------')
    print('')
    pas = input('Please enter password:')
    while pas != 'fatima':
        print('Incorrect password\nPlease enter password again:', end='')
        pas = input()
    if pas == 'fatima':
        print('\t\t\t\t\t\t\t\t\t\tWHICH MODE YO WANT TO BE ACCESSED?:\n \t\t\t\t\t\t\t\t1:General Knowledge\t\t\t\t\t\t2:Sports')
        print('')
        select = input('WHICH MODE DO YOU WANT :(1) OR :(2):')
        if select == '1':
            print('\t\t\t\t\t\t\t\t\t\t\t\t\tWHAT DO YOU WANT?\n\t\t\t\t\t\t\tFOR VIEWING ENTER :(v),\t\t\t\t\t FOR ADDING QUESTIONS ENTER :(a)')
            panel = input('Enter keyword here:')
            panel=panel.lower()
            if panel == 'v':
                f = open('cs21107_3.txt')
                view_file()
            elif panel == 'a':
                print('')
                f = open('cs21107_3.txt', 'a+')
                addques()
            else:
                print('Please enter appropriate keywords..')
                quit()
        elif select == '2':
            print('\t\t\t\t\t\t\t\t\t\t\t\t\tWHAT DO YOU WANT?\n\t\t\t\t\t\t\tFOR VIEWING ENTER :(v),\t\t\t\t\tFOR ADDING QUESTION ENTER :(a)')
            panel = input('Enter Keyword here:')
            panel=panel.lower()
            if panel == 'v':
                f = open('cs21107_2.txt')
                view_file()
            elif panel == 'a':
                print('')
                f = open('cs21107_2.txt', 'a+')
                addques()
            else:
                print('Please enter appropriate keywords..')
                quit()
        else:
            print('Enter appropriate command..')
    else:
        print('\t\tPlease Enter Correct Password!\n\t\tRun program again:)')
        quit()
else:
    print('please enter appropriate command and run again')
    quit()
# --------------------------------------------------------------------------
# The password for admin is fatima......
