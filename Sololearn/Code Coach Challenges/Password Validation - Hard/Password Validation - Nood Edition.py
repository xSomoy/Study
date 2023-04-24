password = input()
a = 0
b = 0
if (len(password)>=7):
    for i in password:
        if ( i.isdigit() ):
            a=a+1
        if (i == '!') | (i == '@') | (i == '#') | ( i == '$') | ( i == '%') | ( i == '&') | ( i == '*'):
            b=b+1
    if ( a < 2 ) | ( b < 2):
        print("Weak")
    else:
        print('Strong')
else:
    print("Weak")