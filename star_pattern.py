N=int(input('Enter the number of rows: '))
boolean=int(input('Enter 1 or 0: '))
if boolean==1:
    for i in range (0,N+1): 
        print('*'*i) 
if boolean==0:
    for j in range (N,0,-1): 
        print('*'*j)
