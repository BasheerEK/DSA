numbers = [1, 2, 3, 4] 

# The Long Way 
squares = [] 
for n in numbers: 
    squares.append(n ** 2) 
print(squares)  
  
# The List Comprehension Way 
# Read as: "n squared FOR every n IN numbers" 
squares_comp = [n ** 2 for n in numbers] 
print(squares_comp)