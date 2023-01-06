def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    
    x = str(x)
    right = len(x) - 1
    left = 0
    while right > left:
        if x[right] != x[left]:
            return False
        right -= 1
        left += 1
    return True

print(isPalindrome(123421))