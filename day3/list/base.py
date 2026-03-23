nums=[10,20,30,40]
print(nums[0])#for indexing from first
print(nums[-1])#for indexing from end


#--------------------------------------
#updating
nums[1]=25
print(nums)


#--------------------------------------
nums.append(50)#add element at the end
nums.insert(1,20)#isert element at a specific value
nums.insert(4,35)
print(nums)


#--------------------------------------
nums.remove(35)#removes the specific value
nums.pop(2)#removes the value by index
print(nums)


#--------------------------------------
print(len(nums)) #to find no of elements in a list


#--------------------------------------
for i in nums:
    print(i)

    

#--------------------------------------
