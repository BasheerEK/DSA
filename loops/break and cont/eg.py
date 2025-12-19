numbers = [1, 5, 8, 10, 15, 20] 
 
for num in numbers: 
    if num % 2 != 0: 
        continue 
     
    print(f"Processing even number: {num}") 
     
    if num > 15: 
        break 