numbers=[20,6,46,83,99,2,5,6,8,45,98,91]
new=[]
great=0
for num in numbers:
    if num >= great :
        great=num
for i in range(1,great):
    for num in numbers:
        if num == i :
            new.append(i)
print(new)                        
