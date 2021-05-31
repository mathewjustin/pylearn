import unittest

#Time complexity is O(N) Space complexity is O(1)

class ValidateSubSequence:
    def isValidSubsequence(array, sequence):
        # Write your code here.
        sequenceTracker=0
        for num in array:
            if sequenceTracker==len(sequence):
                break
            if  sequence[sequenceTracker] == num:
                sequenceTracker+=1

        return sequenceTracker == len(sequence)




class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [22, 25, 6]
        self.assertTrue(ValidateSubSequence.isValidSubsequence(array, sequence))
