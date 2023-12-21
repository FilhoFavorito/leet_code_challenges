from ValidAnagram import Solution
import unittest

class TestSum(unittest.TestCase):
    def test_list_int(self):
        solution = Solution()
        test1 = solution.isAnagram("anagram", "nagaram")
        test2 = solution.isAnagram("part", "trap")
        test3 = solution.isAnagram("rat", "car")

        self.assertEqual(test1, True)
        print("test1 was sucessful")
        self.assertEqual(test2, True)
        print("test2 was sucessful")
        self.assertEqual(test3, False)
        print("test3 was sucessful")

if __name__ == '__main__':
    unittest.main()