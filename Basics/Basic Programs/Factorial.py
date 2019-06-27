def factorial(n):
    return 1 if (n==1 or n==0)else n*factorial(n-1)

a = int(input("Enter nuumber: "))
print(factorial(a))
