n=10
series = 'fibbonacci'

if series == 'fibbonacci':
    a=0
    b=1
    for i in range(n-1):
        c=a+b
        print c
        a=b
        b=c
