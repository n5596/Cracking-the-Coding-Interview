def sumSwap(nums1, nums2, n, m):
    # write your code here
    
    table = set()

    for val2 in nums2:
        table.add(val2)

    s1 = sum(nums1)
    s2 = sum(nums2)

    if (s1-s2) % 2 == 1: # odd so impossible
        return False

    target = (s1-s2)//2

    for val1 in nums1:
        if val1-target in table:
            return True
    return False
