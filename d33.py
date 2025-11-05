def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n_terms = int(input("Enter number of terms: "))
for i in range(n_terms):
    print(fibonacci(i), end=" ")
