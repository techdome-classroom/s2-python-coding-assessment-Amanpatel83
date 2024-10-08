class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to their corresponding integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        result = 0
        
        # Traverse the string from left to right
        for i in range(len(s)):
            # If the current value is smaller than the next value, subtract it
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                # Otherwise, add it to the result
                result += roman_map[s[i]]
        
        return result


