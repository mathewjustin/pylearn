if __name__=='__main__':
    n=int(input().strip())
    if n%2==0: #n is even number
        if n>=6 and n<=20:
            print('Weird')
        if n>=2 and n<=5 or n >20:
            print('Not Weird')
    else:
        print('Weird')
