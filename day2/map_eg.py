nums = [1, 2, 3, 4] 
# Using lambda to double every number 
doubled = map(lambda x: x * 2, nums) 
# map returns a map object, convert to list to view 
print(list(doubled)) 