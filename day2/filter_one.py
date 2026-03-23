# Use filter to keep only words longer than 3 letters from ['hi', 'hello', 'yo', 'python']. 

words=['hi', 'hello', 'you', 'python']
three_letter=filter(lambda x:len(x)==3 ,words)
print(list(three_letter))
