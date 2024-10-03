print("\033c")

n = int(input("enter a number: "))
sum = 0

for i in range(0,n+1) :
    sum = sum + i
    print(f"for {i}th iteration sum is {sum}")