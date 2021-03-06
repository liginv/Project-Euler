"""Project Euler - Problem 2:
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
                1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
#!/usr/bin/python3.6

sum = 0
fibo = list()
even = list()

for i in range(0, 33):
    if i == 0:
        fibo.append(1)
    elif i == 1:
        fibo.append(2)
        even.append(2)
    else:
        new = fibo[i - 2] + fibo[i - 1]
        if new < 4000000:
            fibo.append(new)
            if new % 2 == 0:
                even.append(new)

print(f"The Fibonacci Series: {fibo}")
print(f"The even termed valued terms: {even}")

for i in even[0:]:
    sum += i

print(f"The sum of even-valued terms: {sum}")