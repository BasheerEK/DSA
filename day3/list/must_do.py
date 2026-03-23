#  Count even and odd numbers
#  Reverse list without reverse()
#  Remove duplicates


numbers=[1,2,3,4,5,6,7,8,9,10]

print(numbers)

total=sum(numbers)
average=total/len(numbers)

print("sum of numbers is : ",total)
print("Average of numbers is : ",average)

largest=0
for num in numbers:
    if num >= largest:
        largest=num
smallest=largest
for num in numbers:
    if num <= smallest:
        smallest=num
print(f"Largest number is {largest}")        
print(f"Smallest number is {smallest}")  

even_count=0
odd_count=0
for num in numbers:
    if num % 2 == 0 :
        even_count += 1
    else :
        odd_count += 1

new=[]
for i in range(len(numbers)-1,-1,-1):
    new.append(numbers[i])
print(new)    