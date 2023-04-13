def sumSwap(nums1, nums2, n, m):
    # write your code here
    
    nums2.sort()

    def binary_search(l, r, target):
        if l > r:
            return False

        mid = (l+r)//2

        if nums2[mid] == target:
            return True
        elif nums2[mid] < target:
            return binary_search(mid+1, r, target)
        return binary_search(l, mid-1, target)

    s1 = sum(nums1)
    s2 = sum(nums2)

    if (s1-s2) % 2 == 1:
        return False

    target = (s1-s2)//2
    
    for val in nums1:
        if binary_search(0, m-1, val-target):
            return True

    return False
