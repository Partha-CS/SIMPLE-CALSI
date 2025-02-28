x='Yes'
while x =='Yes' or x=='yes':
    a=int(input('Enter first no.:'))
    b=int(input('Enter second no.:'))
    y = input('Enter a sign b/w +,-,*,/:')
    if y=='+':
        c=a+b
        print('Sum is',c)
    elif y=='-':
        c=a-b
        print('Subtraction is',c)
    elif y=='*':
        c=a*b
        print('Multiplication is',c)
    elif y=='/':
        c=a/b
        print('division is',c)
    else:
        print('Give a valid input')
    x=input('Enter Yes to run code or NO to stop code:')