a=int(input("Enter the value to find : "))
numbers=[20,6,46,83,99,2,5,6,8,45,98,91]
count=-1
for i in numbers:
    count = count + 1
    if i == a:
        print("The element Exist at position ",count)
        break
else:
    print("The elemenmt does not Exist ")
        