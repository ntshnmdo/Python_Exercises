def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    for n in nums:
        i = abs(n) - 1 # i is index
        nums[i] = -1 * abs(nums[i]) # making ith index -ve

    res = [] # to check if value exist in res or not
    for i, n in enumerate(nums): # i is key and n is value so enumerate helps iterate both at once
        if n > 0: # that means n is not in res and that we want to return
            res.append(i + 1) # i + 1 is the index of the n 
    return res
