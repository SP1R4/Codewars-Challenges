def next_smaller(n):
    num = [int(i) for i in str(n)]
    next_smallest = float("-inf")
    nsc = float("-inf")
    pos = len(num)-1
    
    if (len(num) == 1 or num == sorted(num)):
        return -1
        
    for i in range(len(num)-1, 0, -1):
        if num[i] < num[i-1]:
            pos -= 1
            break
        pos -= 1
    
    for i in range(pos, len(num)):
        if (num[i] < num[pos] and num[i] > next_smallest):
            next_smallest = num[i]
            nsc = i
    
    num[pos], num[nsc] = num[nsc], num[pos]
    num2 = num[pos+1:]
    num2.sort(reverse = True)
    
    for i in range(len(num2)):
        num[i+pos+1] = num2[i]
        
    num = [str(x) for x in num]
    s = "".join(num)
    
    return int(s) if s[0] != '0' else -1
