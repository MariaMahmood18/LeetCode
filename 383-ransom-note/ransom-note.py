from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # # Strategy no. 1
        # magazine_dict = {} # To store the magazine letters against its occurence

        # for letter in magazine:
        #     if letter in magazine_dict:  # Check if the letter already exists in the dictionary
        #         magazine_dict[letter] += 1 
        #     else: 
        #         magazine_dict[letter] = 1  # add new item to dictionary

        # for letter in ransomNote:
        #     if magazine_dict.get(letter, 0) == 0:
        #         return False
        #     else:
        #         magazine_dict[letter] -= 1
        # return True


        # Strategy no.2
        magazine_counter = Counter(magazine)

        for letter in ransomNote:
            if magazine_counter[letter] == 0:
                return False
            else:
                magazine_counter[letter] -= 1

        return True

        