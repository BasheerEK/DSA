# Count even and odd numbers

numbers= [ 2, 6, 4,5,87,3,6,8,9,78,2,584,854,54,47,84,8485,45] 
odd=0
even=0
for num in numbers :
    if num % 2 == 0 :
        even += 1
    else:
        odd += 1
print(f"Number of odd in list : {odd}")    
print(f"Number of even in list : {even}")    
print(len(numbers))
