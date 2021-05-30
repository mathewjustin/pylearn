import unittest

#Solution 1 without hash tables. Using double iteration but it knows which number to look for
# As we are using 2 iterations time complexity will be n sqare.
# As we are not using any extra space space complexity will be O(1)

class Program:
    def twoNumberSum(array, targetSum):
        # Write your code here.
        numberToLookFor = 0;

        for i in array:
            resultArray = []
            if i < 0:
                numberToLookFor = abs(i) + targetSum
            else:
                numberToLookFor = targetSum - i
            for x in array:
                if x == numberToLookFor and x != i:
                    resultArray.append(i)
                    resultArray.append(x)
                    return resultArray


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = Program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
