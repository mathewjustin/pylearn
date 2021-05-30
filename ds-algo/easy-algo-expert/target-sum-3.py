import unittest


# Solution 3 using left and right pointer
# Will be having time complexity of O(LogN) the time complexity of the sorting algorithm.
# Where as this solution will be having O(1) Space complexity. As we are using 2 references only and it is constant

class Program:
    def twoNumberSum(array, targetSum):
        # Write your code here.
        array.sort()
        # -1, -4, 1, 3, 5, 6, 8 , 11 //13
        left_pointer = 0
        right_pointer = len(array)-1

        while left_pointer<right_pointer:
            current_sum = array[left_pointer] + array[right_pointer]
            if current_sum < targetSum:
                left_pointer += 1
            elif current_sum > targetSum:
                right_pointer -= 1
            elif current_sum == targetSum:
                return [array[left_pointer], array[right_pointer]]
        return []


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = Program.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
