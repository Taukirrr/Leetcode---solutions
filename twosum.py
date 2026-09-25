def twosum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        compliment = target - num
        if(compliment in hashmap):
            return[hashmap[compliment],i]
        else:
            hashmap[num] = i

nums = [1,2,3,4]

print(twosum(nums,6))
