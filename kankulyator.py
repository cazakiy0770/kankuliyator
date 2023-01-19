print('dasturni tuxtatish uchun a b deb yozish kerak') 

while True:
    a=int(input('a='))
    b=int(input('b='))
    while True:
        amal=input('+/-/*/div/sqrt/**:')
        if amal=='+':
            c=a+b
        elif amal=='-':
            c=a-b
        elif amal=='*':
            c=a*b
        elif amal=='div':
            c=a/b
        elif amal=='sqrt':
            c=sqrt(a+b)
        elif amal=='**':
            c=a**b
        else:
            c='a b'
            break
        print('javobi=',c)    


        
