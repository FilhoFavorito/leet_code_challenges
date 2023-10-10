from TwoSum import Solution
import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        solution = Solution()
        test1 = solution.twoSum([2,7,11,15], 9)
        test2 = solution.twoSum([3,2,4], 6)
        test3 = solution.twoSum([3,3], 6)

        self.assertEqual(test1, [0,1])
        print("test1 was sucessful")
        self.assertEqual(test2, [1,2])
        print("test2 was sucessful")
        self.assertEqual(test3, [0,1])
        print("test3 was sucessful")
if __name__ == '__main__':
    unittest.main()