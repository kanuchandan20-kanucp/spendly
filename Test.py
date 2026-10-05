start_range = int(input("Enter the starting range:"))
end_range = int(input("enter the ending range:"))

numbers = range(start_range,end_range+1)
sum = 0
for i in numbers:
    sum = sum + i
print(f"Sum value for this activity is {sum}")