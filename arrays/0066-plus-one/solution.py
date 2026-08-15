class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # This is the first instinct solution but it has the complexity of O(N^2)
        # l = len(digits)
        # p = l-1
        # total = 0
        # for i in range(l):
        #     total += (digits[i] * 10**p)
        #     p-=1
        # total += 1
        # total_list = [int(digit) for digit in str(total)]
        # return total_list
    
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
        digits.insert(0,1)
        return digits
