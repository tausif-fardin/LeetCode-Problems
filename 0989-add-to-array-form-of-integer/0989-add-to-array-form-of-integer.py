class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        # Convert array-form to integer
        num_int = 0
        for digit in num:
            num_int = num_int * 10 + digit

        # Add k to integer
        sum_int = num_int + k

        # Convert sum back to array-form
        sum_arr = []
        if sum_int == 0:
            return [0]
        while sum_int > 0:
            digit = sum_int % 10
            sum_arr.append(digit)
            sum_int //= 10
        return sum_arr[::-1]


