name_list=['C1','C2','C3']
def getdate():
    import datetime
    return datetime.datetime.now()
def log(n):
    if n=='C1':
        response=input('What do you want to log?(e or f): ') 
        if response=='e':
            with open('C1e.txt', 'a') as C1e:
                C1e.write("\n-"+input('Enter exercise: ')+'-'+str([str(getdate())]))
        elif response=='f':
            with open('C1f.txt', 'a') as C1f:
                C1f.write("\n-"+input('Enter food: ')+'-'+str([str(getdate())]))
    elif n=='C2':
        response = input('What do you want to log?(e or f): ')
        if response == 'e':
            with open('C2e.txt', 'a') as C2e:
                C2e.write('\n'+"-"+input('Enter exercise: ')+'-'+str([str(getdate())]))
        elif response == 'f':
            with open('C2f.txt', 'a') as C2f:
                C2f.write('\n'+"-"+input('Enter food: ')+'-'+str([str(getdate())]))
    elif n=='C3':
        response = input('What do you want to log?(e or f): ')
        if response == 'e':
            with open('C3e.txt', 'a') as C3e:
                C3e.write('\n'+"-"+input('Enter exercise: ')+'-'+str([str(getdate())]))
        elif response == 'f':
            with open('C3f.txt', 'a') as C3f:
                C3f.write('\n'+"-"+input('Enter food: ')+'-'+str([str(getdate())]))

def retrieve(n):
    if n=='C1':
        a=input('Do you want to view food or exercise? (choose f or e):')
        if a=='e':
            with open ('C1e.txt') as C1er:
                for i in C1er:
                    print(i,end="")
        if a=='f':
            with open ('C1f.txt') as C1fr:
                for i in C1fr:
                    print(i,end="")
    if n=='C2':
        a = input('Do you want to view food or exercise? (choose f or e):')
        if a == 'e':
            with open('C2e.txt') as C2er:
                for i in C2er:
                    print(i, end="")
        if a == 'f':
            with open('C2f.txt') as C2fr:
                for i in C2fr:
                    print(i, end="")
    if n=='C3':
        a = input('Do you want to view food or exercise? (choose f or e):')
        if a == 'e':
            with open('C3e.txt') as C3er:
                for i in C3er:
                    print(i, end="")
        if a == 'f':
            with open('C3f.txt') as C3fr:
                for i in C3fr:
                    print(i, end="")
# User Input-------
client=input('Please Enter client name: ')
log_retrieve=input('Do you want to log or retrieve data? (Write L or R): ')

if client== 'C1':
    if log_retrieve=='L':
        log('C1')
    elif log_retrieve=='R':
        retrieve('C1')
    g=input('Do you want to add more? (L or R or No): ')
    if g=='L':
        log('C1')
    elif g=='R':
        retrieve('C1')
    elif g=='No':
        print('Changes Saved.')
if client== 'C2':
    if log_retrieve=='L':
        log('C2')
    elif log_retrieve=='R':
        retrieve('C2')
    g = input('Do you want to add more? (L or R or No): ')
    if g == 'L':
        log('C2')
    elif g == 'R':
        retrieve('C2')
    elif g == 'No':
        print('Changes Saved.')
if client== 'C3':
    if log_retrieve=='L':
        log('C3')
    elif log_retrieve=='R':
        retrieve('C3')
    g = input('\nDo you want to add more? (L or R or No): ')
    if g == 'L':
        log('C3')
    elif g == 'R':
        retrieve('C3')
    elif g == 'No':
        print('Changes Saved.')

