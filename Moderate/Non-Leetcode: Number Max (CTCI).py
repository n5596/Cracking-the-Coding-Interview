def flip(a):
    return 1^a

def sign(a):
    # Using right shift operator to find the sign bit of a 32 bit number
    # if a >= 0, a >> 31 will be 0 (as the sign bit is 0)
    # if a < 0, a >> 31 will be -1 as the sign bit is 1
    
    # 0x1 = 1 so -1&1 =1 and 0&1=0
    # (a>>31) & 0x1 = 0 if a >= 0
    #               = 1 if a < 0
    
    # flip((a>>31) & 0x1) = 1 if a >= 0
    #                     = 0 if a < 0
    return flip((a>>31) & 0x1)
    
def find_max_CTCI(a, b):
    sa = sign(a)
    sb = sign(b)
    
    c = a-b
    sc = sign(c)
    
    use_sign_of_a = sa^sb # a and b have different signs so there might be overflow
    use_sign_of_c = flip(sa^sb) # a and b have same sign so no need to worry about overflow
    
    k = use_sign_of_a*sa+use_sign_of_c*sc
    # if a and b have different signs -> use sign of a else use sign of (a-b)
    
    q = flip(k)
    return k*a+q*b

# Testing
for i in range(5090):
    a = random.randint(-1000000, 10000000)
    b = random.randint(-1000000, 10000000)
    
    c = find_max_CTCI(a, b)
    
    if c != max(a, b):
        print("Incorrect answer for testcase:", i)
