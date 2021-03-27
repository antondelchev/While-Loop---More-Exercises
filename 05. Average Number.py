n = int(input())

sum_total = 0
counter = 0

while counter < n:
    number = int(input())
    sum_total += number
    counter += 1

print(f"{(sum_total / counter):.2f}")
