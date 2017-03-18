def is_pali(num):
        return str(num) == str(num)[::-1]        
def fn(n):
    max_pali = 1
    for x in range(n,1,-1):
        if x * n < max_pali: 
            break
        for y in range(n,x-1,-1):
            if is_pali(x*y) and x*y > max_pali:
                max_pali = x*y
            elif x * y < max_pali:
                break
    return max_pali

print fn(999)