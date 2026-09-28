def containsDuplicate(nums):
    hashmap={}
    for i,num in  enumerate(nums):
       
        if(num in hashmap):
            return True
        hashmap[num] = i
    
    return False

        
nums = [1,2,3,1]
print(containsDuplicate(nums))