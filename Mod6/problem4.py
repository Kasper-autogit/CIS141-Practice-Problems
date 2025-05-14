'''#4.  Create a list of integers.
Write code that counts how many numbers are positive
and how many are negative, then print both counts.
'''

nums = [5, -3, 8, -1, 0, -7, 2]
positive_count = 0
negative_count = 0
for i in nums:
    if i > 0:
        positive_count += 1
    elif i < 0:
        negative_count += 1
print("Positive numbers:", positive_count)
print("Negative numbers:", negative_count)
