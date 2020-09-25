def moveZeroes(nums):
    """
        Do not return anything, modify nums in-place instead.
        """
    for i in range(len(nums) - 1):
        print(i)
        if nums[i] == 0:
            j = i + 1
            while nums[j] == 0 and j < len(nums) - 1:
                j += 1
            nums[i] = nums[j]
            nums[j] = 0
            print(nums)


moveZeroes([0, 1, 0, 3, 12])
