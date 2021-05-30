import unittest

# Solution 2 using the hash tables, to memoize the already visited node
# As we are not using double iterations, and only with 1 single iteration we are calculating, time complexity is O(N)
# Space complexity will be O(N) because of the hash table.

class Program:
    def twoNumberSum(array, targetSum):
        # Write your code here.
        numberToLookFor = 0;
        alreadyLooked={};
        for i in array:
            numberToLookFor = targetSum - i;
            if numberToLookFor in alreadyLooked:
                return [numberToLookFor,i]
            else:
                alreadyLooked[i]=True
        return []

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = Program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
