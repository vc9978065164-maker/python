#Write a program to demonstrate recursion usingfactorial or Fibonacci series

def fibo(n):
    if n<=1:
        return 1
    return fibo(n-1)+fibo(n-2)
re=fibo(5)
print(re)   
