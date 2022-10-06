n = int(input("Enter the number: "))
s = n
while n > 1:
    n -= 1
    s = s * n
print(f"The factorial of an entered number is {s}")

print(len(str(s)))
