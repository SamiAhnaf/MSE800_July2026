def fibonacci(n):
    a=0
    b=1
    print("Fibonacci series up to", n, ";")
    while a <= n:   
        print(a, end=" ") 
        a, b = b, a + b
    print()
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def main():
    n = int(input("Enter a number (N): "))
    fibonacci(n)
    fact = factorial(n)
    print("Factorial of", n, "is:", fact)
if __name__ == "__main__":
    main()