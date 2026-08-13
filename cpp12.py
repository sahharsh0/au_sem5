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
        
        # Separate the digits into odd and even lists
        odd_digits = sorted([d for d in digits if d % 2 == 1], reverse=True)
        even_digits = sorted([d for d in digits if d % 2 == 0], reverse=True)
        
        # Create a new list to hold the largest possible value
        largest_num = []
        
        # Iterate through the original digits and replace them with the largest available digit of the same parity
        for d in digits:
            if d % 2 == 1:  # Odd digit
                largest_num.append(odd_digits.pop(0))
            else:  # Even digit
                largest_num.append(even_digits.pop(0))
        
        # Convert the list of digits back to an integer
        return int(''.join(map(str, largest_num)))  
print(Solution().LargestInteger(1234))  