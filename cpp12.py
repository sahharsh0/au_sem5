'''
You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps
'''
class Solution(object):
    def LargestInteger(self,num):
        """
        :type num: int
        :rtype: int
        """
        digits = [int(d) for d in str(num)]
        
        odd_digits = sorted([d for d in digits if d % 2 == 1], reverse=True)
        even_digits = sorted([d for d in digits if d % 2 == 0], reverse=True)
        
        largest_num = []
        
        for d in digits:
            if d % 2 == 1:  # Odd digit
                largest_num.append(odd_digits.pop(0))
            else:  # Even digit
                largest_num.append(even_digits.pop(0))
        
        return int(''.join(map(str, largest_num)))  
print(Solution().LargestInteger(1234))   