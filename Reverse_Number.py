
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
def reverse(self, x: int) -> int:
    negFlag = False
    if (x < 0):
        negFlag = True
        x = -x
    pReverseNum = 0
    reverseNum = 0
    while x > 0:
        lastDigit = x % 10
        reverseNum = (reverseNum*10)+lastDigit

        if (reverseNum >= 2147483647 or reverseNum <= -2147483648):
            return 0
        if ((reverseNum - lastDigit) // 10 != pReverseNum):
            return 0
        pReverseNum = reverseNum
        x = x//10

    return -reverseNum if (negFlag == True) else reverseNum
