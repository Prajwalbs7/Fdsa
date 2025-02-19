def sum_of_digits(n):
    sum = 0
    if (n == 0):
        return 0
    return n % 10 + sum_of_digits(n // 10)
n = int(input("Enter a number:"))
print(sum_of_digits(n))
