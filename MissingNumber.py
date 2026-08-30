# Find the Missing Number
# You are given a list containing n-1 unique integers in the range from 1 to n. 
# Write a function find_missing(nums) to find the one missing integer
placeholder = [1,2,4,5,6,7]
def missing_num(nums):
    counter = nums[0]
    for i in nums:
        if counter != i:
            break
        counter += 1
    if counter > nums[-1]:
        return f"There is no missing number in {nums}"
    else:
        return f"The missing number is {counter} in the list {nums}"
print(missing_num(placeholder))