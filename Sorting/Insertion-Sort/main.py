nums = list(map(float, input().split()))
n = len(nums)
for j in range(1, n):
    key = nums[j]
    i = j-1
    while i>=0 and nums[i] > key:
        nums[i+1] = nums[i]
        i -= 1
    nums[i+1] = key

print(nums)