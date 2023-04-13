def find_max_GFG(a, b):
    return a*bool((a//b))+b*bool((b//a))

# Testing
for i in range(500):
    a = random.randint(0, 10000000)
    b = random.randint(0, 10000000)
    
    c = find_max_GFG(a, b)
    
    if c != max(a, b):
        print("Incorrect answer for testcase:", i)
