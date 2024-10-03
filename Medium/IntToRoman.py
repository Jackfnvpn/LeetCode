#link: https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:  
        roman_numbers={
        "M":1000,
        "CM":900,
        "D":500,
        "CD":400,
        "C":100,
        "XC":90,
        "L":50,
        "XL":40,
        "X":10,
        "IX":9,
        "V":5,
        "IV":4,
        "I":1,
        }

        roman_number=""

        while (num>0):
            string_num=str(num)
            for number in roman_numbers:
                if num-roman_numbers[number]>=0:
                    roman_number+=number  
                    num=num-roman_numbers[number]
                    break
        return roman_number
