def fibonacci(n):
    a, b = 0,1
    while a < n:
        print(a, end="")
        a,b = b, a+b
        print()

n = int(input("Até que número gostarias de ver a sequência de Fibonacci? "))
fibonacci(n)
