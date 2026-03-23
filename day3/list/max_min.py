numbers=[20,6,46,83,99,2,5,6,8,45,98,91]
great=0
for num in numbers:
    if num >= great :
        great=num
print(f"The Maximum Value Is : {great}")        
low=great
for num in numbers:
    if num <= low :
        low=num
print(f"The Minimum Value Is : {low}")                