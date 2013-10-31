n=10
series = 'fibbonacci'

if series == 'fibbonacci':
    x=0
    y=1
    for i in range(n-1):
        z=x+y
        print z
        x=y
        y=z
