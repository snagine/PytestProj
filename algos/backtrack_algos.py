class BackTrack:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()

        ans = []
        backtrack([])
        return ans

    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans

    def combine(self, n: int, k: int) -> list[list[int]]:
        def backtrack(curr, i):
            if len(curr) == k:
                ans.append(curr[:])
                return

            for num in range(i, n + 1):
                curr.append(num)
                backtrack(curr, num + 1)
                curr.pop()

        ans = []
        backtrack([], 1)
        return ans

    def letterCombinations(self, digits: str) -> list[str]:
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations

    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(path, start, curr):
            if curr == target:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr + num <= target:
                    path.append(num)
                    backtrack(path, i, curr + num)
                    path.pop()

        ans = []
        backtrack([], 0, 0)
        return ans

    def validPalindrome_2(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        left = 0
        right = len(s) - 1
        while left < right :
            if s[left] != s[right]:
                new1 = s[:left] + s[left+1:]
                new2 = s[:right] + s[right+1:]
                if new1 == new1[::-1] or new2 == new2[::-2]:
                    return True
                else:
                    return False
            else:
                left += 1
                right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l + 1:]
                tmp2 = s[:r] + s[r + 1:]
                if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                    return True
                else:
                    return False

        return True

    def validPalindrome_rec(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        count = 0






backtrack_algos = BackTrack()
# res = backtrack_algos.permute([1,2,3])
# res = backtrack_algos.subsets([1, 2, 3])
# res = backtrack_algos.combine(4, 2)
# res = backtrack_algos.letterCombinations2("34")
# res = backtrack_algos.combinationSum([2, 3, ], 5)
# res = backtrack_algos.validPalindrome("abcdddxba")
res = backtrack_algos.validPalindrome_2("abcdddba")
# res = backtrack_algos.validPalindrome_rec("abcdxba")
print(res)