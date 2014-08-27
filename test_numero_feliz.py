
def testIsHappy():
    assert isHappy(7) == True
    assert isHappy(97) == True
    assert isHappy(95) == False
    assert isHappy(130) == True
    assert isHappy(1000) == True

def isHappy(n):
    sum = 0
    for i in str(n):
        sum += int(i)**2

    if sum == 1:
        return True
    elif len(str(sum)) > 1:
        return isHappy(sum)
    else:
        return False



