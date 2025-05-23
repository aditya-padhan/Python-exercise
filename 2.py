num = int(input("Enter a number : "))
sum = 0
i = 1
while i <= num :
    j = 0
    sum = 0
    while j <= i:
        sum += j*j
        j += 1
    print(sum)
    i += 1