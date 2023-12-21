# Contains Duplicate

## Question
* Given two strings `s` and `t`, return `true` *if* `t` is an anagram of `s`, and `false` otherwise.
* An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

### Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:
* `1 <= s.length, t.length <= 5 * 104`
* `s and t consist of lowercase English letters`

## Solution:

* The code takes two variables: `s` and `t`, both `Strings`.
* It then checks if `s` and `t` have the same size, if they don't the code will return `False` since anagrams must have the same size.
* A `Set` containin all the characters of the variable `s` is created then both variables are iterated checking if each character appears the same amount of times, *if* they do the code will return `True`, other wise it will return `False`


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False

        return True
```