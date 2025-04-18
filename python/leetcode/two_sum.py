def twosum(nums,target):
    for i in range(len(nums)):
        for i1 in range(len(nums)):
            if nums[i]+nums[i1]==target and i !=i1 :
                return(i,i1)

print([1,2,3,4],3)
print(twosum([1,2,3,4],3))