# Use map to convert a list of strings ['1', '2', '3'] into integers. 

num = ['1' , '2' , '3']
changed=map(lambda x:int(x) , num)
print(list(changed))