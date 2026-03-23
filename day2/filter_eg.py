nums = [1, 5, 8, 10, 12, 13] 
# Keep only even numbers 
evens = filter(lambda x: x % 2 == 0, nums) 
print(list(evens))
