N=79
guesses=10
print('Total allotted guesses: ',guesses)
while (1):
    m=int(input('Guess the Number: '))
    if m==N:
        print('Congratulations! You won!\n'
              ' with guesses remaining:', guesses-1)
        break
    elif m<N:
        print('Entered number is smaller. Try Again')
    elif m>N:
        print('Entered number is bigger. Try Again')
    guesses=guesses-1
    print('Guesses Left: ',guesses)
    if guesses==0:
        print('GAME OVER!')
        break
