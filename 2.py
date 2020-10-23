def Fibonacci(a):
    if a == 1 or a == 2:
        return a
    else:
        return Fibonacci(a - 1) + Fibonacci(a - 2)


s = 0
a = 2
while Fibonacci(a) < 4000000:
    if Fibonacci(a) % 2 == 0:
        s += Fibonacci(a)
    a += 1
print(s)
