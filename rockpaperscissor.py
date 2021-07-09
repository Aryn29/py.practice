import random
Computer_input=['Rock','Paper','Scissors']
C=0
U=0
rounds=0
while (1):
    User_input = input('Select your choice(R,P,S): ')
    computer_choices = random.choice(Computer_input)
    if User_input=='R':
        if computer_choices=='Paper':
            C=C+1
            rounds=rounds+1
            print('Computer wins this round!',C)
        elif computer_choices=='Rock':
            rounds=rounds+1
            print('Result tied.')
        elif computer_choices=='Scissors':
            U=U+1
            rounds=rounds+1
            print('User wins this round!',U)
    if User_input=='P':
        if computer_choices=='Paper':
            rounds=rounds+1
            print('Round tied.')
        elif computer_choices=='Rock':
            U=U+1
            rounds=rounds+1
            print('User wins this round!',U)
        elif computer_choices=='Scissors':
            C=C+1
            rounds=rounds+1
            print('Computer wins this round!',C)
    if User_input=='S':
        if computer_choices=='Paper':
            C=C+1
            rounds=rounds+1
            print('Computer wins this round!',C+1)
        elif computer_choices=='Rock':
            U=U+1
            rounds=rounds+1
            print('User wins this round!',U+1)
        elif computer_choices=='Scissors':
            rounds=rounds+1
            print('Round tied.')
    if rounds == 10:
        break
if U>C:
    print('USER IS THE WINNER, BY',U-C,'POINTS!!')
else:
    print('COMPUTER IS THE WINNER, BY',C-U,'POINTS!!')
print('Points by User: ',U)
print('Points by Computer: ',C)
