def fibonacci():
    n = int(input("Nth Term:"))
    a = 0
    b = 1
    if (n == 0):
        return print(f"Term #0 is:", a);
    for i in range(n-1):
        c=a+b
        a=b
        b=c
    print(f"Term #{n} is:", b)

fibonacci()