def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
        # fib avval  0
    elif n == 0:
        return 0
    # fib dovvom 1
    elif n == 1:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
    # dar in qesmat adad haro motavali jam mikone

#dakhel tabe adad qarar bedid
#agar motavaje nashodid az 2 ta 10 adad bedin
print(Fibonacci())