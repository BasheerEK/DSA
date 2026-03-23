numbers=[20,6,46,83,99,2,5,6,8,45,98,91]
reversed_numbers=[]
# new=numbers[-1]
for num in range(len(numbers)-1,-1,-1):
    reversed_numbers.append(numbers[num])
print(reversed_numbers)    