def towerOfHanoi(n):
    # Write your code here
    # Return a 2-D array
    
    memo = {}
    def recursive(num_disks, tA, tC, tB):
        # move from tA to tC using tB as buffer
        if num_disks == 0:
            return []

        # move top n-1 disks to buffer
        moves1 = recursive(num_disks-1, tA, tB, tC)
        moves1.append([tA, tC]) # move largest disk to correct place
        # move the n-1 disks at buffer to correct place
        moves2 = recursive(num_disks-1, tB, tC, tA)
        moves1.extend(moves2)
        return moves1

    return recursive(n, 1, 3, 2)
