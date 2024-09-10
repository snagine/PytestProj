import collections
import re
from math import ceil
from collections import defaultdict


class BaseAlgos:

    def __init__(self):
        pass

    def find_factorial_iter(self, num):
        result = 1
        for i in range(num, 1, -1):
            result *= i
        return result

    def find_factorial_recur(self, num):
        if num <= 2:
            return num
        return num * self.find_factorial_recur(num-1)

    def find_fibonacci_iter(self, n):
        if n <= 0:
            return []
        fib = [0, 1]
        while True:
            new_ele = fib[-1] + fib[-2]
            if new_ele >= n:
                break
            fib.append(new_ele)
        return fib

    # time complexity: O(n), space complexity: O(1)
    # input: ['s', 'h', 'y'] output : ['y', 'h', 's']
    def reverseList(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_index = 0
        right_index = len(s) - 1
        while left_index < right_index:
            s[right_index], s[left_index] = s[left_index], s[right_index]
            left_index += 1
            right_index -= 1

    # input "str" output "rts"
    def reverseString(self, s):
        return s[::-1]

    def reverseList2(self, l):
        return l[::-1]

    # input = [3, 0, 5], output = [0, 9, 25]
    # O(n) for squaring, O(n2) for sorting , so this is not efficient
    def square_and_sort(self, l):
        updated_list = [i*i for i in l] # [9, 0, 25]
        total_elements = len(updated_list) - 1
        # applying bubble sort
        for i in range(total_elements):
            for j in range(i+1, total_elements):
                if updated_list[i] > updated_list[j]:
                    updated_list[i], updated_list[j] = updated_list[j], updated_list[i]
        return l

    # using 2 pointer approach
    # input array is already sorted, so the biggest number will be right most, or left most
    # O(n)
    def square_and_sort_optimize(self, l):
        left_pointer = 0
        right_pointer = len(l) - 1
        output = []
        while left_pointer <= right_pointer :
            squared_val = 0
            if abs(l[left_pointer]) < abs(l[right_pointer]):
                squared_val = l[right_pointer] * l[right_pointer]
                output.insert(0, squared_val)
                right_pointer -= 1
            else:
                squared_val = l[left_pointer] * l[left_pointer]
                output.insert(0, squared_val)
                left_pointer += 1
        return output

    # find the subarray which adds to the given length
    def find_subarray_for_given_length(self, nums, k):
        # curr is the current sum of the window
        left = curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def reverse_words_in_a_sentence(self, s: str) -> str:
        l = s.split(" ") # O(n)
        rev_word = ""
        output_l = []
        for word in l: # O(n2)
            li = list(word)
            total_letters = len(li) - 1
            left_index = 0
            right_index = total_letters
            while left_index < right_index:
                li[left_index], li[right_index] = li[right_index], li[left_index]
                left_index += 1
                right_index -= 1
            rev_word = "".join(li) # O(n)
            output_l.append(rev_word)
        return " ".join(output_l)

    def runningSum(self, nums) -> int:
        output_l = []
        output_l.append(nums[0])
        total_ele = len(nums)
        for i in range(1, total_ele):
            new = nums[i] + output_l[i - 1]
            output_l.append(new)
        return output_l

    #O(n)
    def twoSum_byHash(self, nums, target) -> list:
        element_seen  = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in element_seen:
                return[element_seen[complement], i]
            element_seen[nums[i]] = i
        return [-1,-1]

    def find_win_length(self, nums, k):
        # curr is the current sum of the window
        left = curr = ans = 0
        for right in range(len(nums)):
            curr += nums[right]
            while curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans

    # O(n)
    def find_sameletter_indexes_in_string(self,s: str) -> list:
        seen = {}
        l = list(s)
        for i in range(len(l)):
            if l[i] not in seen:
                seen[l[i]] = 1
            else:
                seen[l[i]] += 1
        return seen

    # O(n)
    # find the number which is either x+1 or x-1
    # input: [2,6,4], 3, output: 2, 4
    def find_number_with_condition(self, nums, target):
        num1 = target + 1
        num2 = target - 1
        if num1 in nums and num2 in nums:
            return True
        return False

    # O(n)
    # is panagram ?
    # ex: if all letters in English are present
    def is_panagram(self, s: str) -> False:
        alph = 'abcdefghijklmnopqrstuvwxyz'
        alph_l = list(alph)
        check = list(s.lower())
        print(check)
        for i in range(len(alph_l)):
            if alph_l[i] not in check:
                return False
        return True

    def is_panagram_with_set(self, s: str) -> False:
        input_val = set(s.lower())
        if len(input_val) == 26:
            return True
        return False

    # find the only missing number in the range
    # ex: [0,1,3] , missing 1,2
    # O(n)
    def find_only_missing_number(self, l):
        new_l = range(len(l)+1)
        for i in range(len(new_l)):
            if i not in l:
                return new_l[i]
        return -1

    # find how many elements of x with x+1
    # i/p [1,2,3], output 2
    # i/p [1,1,3,3,5,5,7,7] output 0
    # O(n)
    def find_elements_with_increment(self, arr: list) -> int:
        counter = 0
        for i in range(len(arr)):
            if arr[i] + 1 in arr:
                counter +=1
        return counter

    # find occurances of losers with 0 times, 1 time
    # input matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    # Output: [[1,2,10],[4,5,7,8]]
    # Players 1, 2, and 10 have not lost any matches., Players 4, 5, 7, and 8 each have lost one match.
    def find_loss_occurances(self, matches):
        loss_map = {}
        for i in range(len(matches)):
            if matches[i][0] not in loss_map.keys():
                loss_map[matches[i][0]] = 0

            if matches[i][1] not in loss_map.keys():
                loss_map[matches[i][1]] = 1
            else:
                loss_map[matches[i][1]] += 1

        no_losses = []
        onetime_loss = []
        for key, val in loss_map.items():
            if val == 0:
                no_losses.append(key)
            if val == 1:
                onetime_loss.append((key))
        return [sorted(no_losses), sorted(onetime_loss)]

    # Input: nums = [5,7,3,9,4,9,8,9,3,1], Output: 8
    def find_largest_non_repeated(self, nums):
        seen = []
        removed = []
        for i in range(len(nums)):
            if nums[i] in seen:
                seen.remove(nums[i])
                removed.append(nums[i])
            else:
                if nums[i] not in removed:
                    seen.append(nums[i])
        return -1 if len(seen) == 0 else max(seen)

    def largestUniqueNumber(self, nums: list[int]) -> int:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        result = -1
        for num, count in counter.items():
            if count == 1:
                result = max(result, num)
        return result

    ##find number of word "balloon" occurances in a given text
    def findWordOccurances(self, text):
        def _my_counter(str):
            counter = {}
            for i in range(len(str)):
                if str[i] in target:
                    counter[str[i]] = counter.get(str[i], 0) + 1
            return counter

        target = "balloon"
        text_counter = _my_counter(text)
        target_counter = _my_counter(target)

        res = set()
        for key, val in target_counter.items():
            if key in text_counter:
                res.add(text_counter[key] // target_counter[key])
            else:
                res.add(0)
        return min(res)

    def is_ele_avail(self, l: list, target: int) -> bool:
        res = False
        if len(l) == 0:
            return res

        l.sort() # O(log n)
        left_in = 0
        right_in = len(l)

        while left_in < right_in:
            mid_in = (left_in + right_in) // 2
            if l[mid_in] < target: # target is higher than mid
                left_in = mid_in + 1
            elif l[mid_in] > target:
                right_in = mid_in
            else:
                return True
        return res

    def binary_search_last_occurance_index(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] > target:
                right = mid
            else:
                left = mid + 1

        return left - 1

    def binary_search_first_occurance_index(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    def minEatingSpeed2(self, piles: list[int], h: int) -> int:
        def hoursToEat(capacity: int):
            hours_to_finish_pile = 0
            for pile in piles:
                hours_to_finish_pile += ceil(pile / capacity)
            return hours_to_finish_pile <= h

        left_limit = 1
        right_limit = max(piles)
        while left_limit <= right_limit:
            mid = (left_limit + right_limit) // 2
            speed_check = hoursToEat(mid)
            if speed_check:
                right_limit = mid - 1
            else:
                left_limit = mid + 1
        return left_limit

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def check(k):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / k)
            return hours <= h

        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        # Sort 'nums'
        nums.sort()
        ans = []

        # For each query, collect numbers from lowest to highest.
        # If their sum exceeds the limit 'query', move on to the next query.
        for query in queries:
            count = 0
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break
            ans.append(count)

        return ans

    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)

    def twoSumSorted(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        while left < right:
            cur = nums[left] + nums[right]
            if cur > target:
                right -= 1
            elif cur < target:
                left += 1
            else:
                ans.append(left)
                ans.append(right)
                return ans
        return ans

    def find_bin_zero_flip_longest_length(self, s): #1101100111
        left = curr = ans = 0
        for right in range(len(s)):
            if s[right] == "0":
                curr += 1
            while curr>1:
                if s[left] == "0":
                    curr -= 1
                left +=1
            ans = max(ans, right - left +1)
        return ans

    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        left = ans = 0
        curr = 1

        for right in range(len(nums)):
            curr *= nums[right]
            while curr >= k:
                curr //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    def capitalized(self, s) -> str:
        l = s.split(" ")
        new = " ".join([i[0].upper() + i[1:] for i in l])
        return new

    def find_best_subarray(self, nums, k):
        curr = 0
        for i in range(k):
            curr += nums[i]

        ans = curr
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr)

        return ans

    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr = ans = 0
        for i in range(k):
            curr += nums[i]
        ans = curr / k

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr / k)
        return ans

    def longestOnes(self, nums: list[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1

    def longestOnes(self, nums: list[int], k: int) -> int:
        left = right = count = 0
        while right < len(nums):
            if nums[right] == 0:
                count += 1
            if count > k:
                if nums[left] == 0:
                    count -= 1
                left += 1
            right += 1
        return right - left

    def minStartValue(self, nums: list[int]) -> int:
        startVal = ans = 0
        for i in range(len(nums)):
            startVal += nums[i]
            ans = min(ans, startVal)

        return -ans + 1

    def find_longest_substring(self, s, k):
        counter = defaultdict(int)
        left = ans = 0
        for right in range(len(s)):
            counter[s[right]] += 1
            while len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

    def areOccurrencesEqual(self, s: str) -> bool:
        frequency = defaultdict(int)
        for right in range(len(s)):
            frequency[s[right]] += 1
        curr = frequency[s[0]]
        for key, val in frequency.items():
            if val != curr:
                return False
        return True

    def findMaxLength(self, nums: list[int]) -> int:
        maxlen = 0
        for start in range(len(nums)):
            zeros = ones = 0
            for end in range(start, len(nums)):
                if nums[end] == 0:
                    zeros += 1
                else:
                    ones += 1
                if zeros == ones:
                    maxlen = max(maxlen, end - start + 1)
        return maxlen

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = defaultdict(list)
        for i in range(len(strs)):
            sorted_word = "".join(sorted(strs[i]))
            hashmap[sorted_word].append(strs[i])
        return hashmap.values()




base_algos = BaseAlgos()
# res = base_algos.square_and_sort([3, 0, 5])
# res = base_algos.square_and_sort_optimize([-4,-1,0,3,10])
# res = base_algos.find_subarray_for_given_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
# s = "Let's take LeetCode contest"
# res = base_algos.reverse_words_in_a_sentence(s)
# res = base_algos.runningSum([1,2,3,4])
# res = base_algos.reverseString("str")
# res = base_algos.reverseList2(['s','t','r'])
# res = base_algos.twoSum_byHash([1,2,9,3,0], 12)
# res = base_algos.find_sameletter_indexes_in_string("abcbad")
# res = base_algos.find_number_with_condition([2,6,4], 7)
# res = base_algos.is_panagram("abcdefghijklmnopqrstuvwxyz")
# res = base_algos.is_panagram_with_set("abcdefghijklmnopqrstuvwxyz")
# res = base_algos.find_only_missing_number([0,2,3])
# res = base_algos.find_elements_with_increment([1,2,3])
# res = base_algos.find_loss_occurances([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
# res = base_algos.find_largest_non_repeated([5,7,3,9,4,9,8,9,3,1])
# res = base_algos.largestUniqueNumber([5,7,3,9,4,9,8,9,3,1])
# res = base_algos.maxNumberOfBalloons("loonbalxballpoon")#("nlaebolko")
# res = base_algos.findWordOccurances("lloo")#("nlaebolk")
# res = base_algos.is_ele_avail([6,4,9,10,5,3,9,6], 6) # True, 1. sort  2. perform binary search
# res = base_algos.binary_search_last_occurance_index([3,3,3,4,4,5,6,6,9], 3) #
# res = base_algos.binary_search_first_occurance_index([3,3,3,4,4,5,6,6,9], 3)
# res = base_algos.answerQueries([4, 2, 5, 1, 6, 13], [3, 10, 21, 2])
# piles = [3,6,7,11]
# h = 8 #4
# piles = [30,11,23,4,20], h = 5 #30
# piles = [30,11,23,4,20], h = 6 #23
# res = base_algos.minEatingSpeed2(piles, h)
# res = base_algos.isSubsequence("ab", "baab")
# res = base_algos.twoSumSorted([2,3,4], 6)
# res = base_algos.twoSum_byHash([3,2,4], 6)
# res = base_algos.find_win_length([3, 1, 2, 7, 4, 2, 1, 1, 5], 8)
# res = base_algos.find_bin_zero_flip_longest_length("1101100111")
# res = base_algos.numSubarrayProductLessThanK([1, 1, 1], 1)
# res = base_algos.capitalized("this is shylaja")
# res = base_algos.find_best_subarray([-3, 1, 4, 12, -8, 5, 6], 4)
# res = base_algos.findMaxAverage([1,12,-5,-6,50,3], 4)
# res = base_algos.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) # return 6
# res = base_algos.minStartValue([-3,2,-3,4,2]) # return 5
# res = base_algos.find_longest_substring("eceba", 2) # 3
# res = base_algos.areOccurrencesEqual("abacbc")
res = base_algos.findMaxLength([0,1,1,0]) # 2
res = base_algos.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(res)

# common mistakes
###################
# check indexes or values in conditions and loops
# edge cases like empty / negatives to be on the top
# have a default value to return after the edge case
# return in the middle of loops/ conditions whenever the criteria is met
# ask what to return on edge cases like -1 or False
# list comprehension : use "for" at the end
# cover in parantheses () if multiple math operations, especially as a denominator
# split the string to list is based on the delimitor, if there is no delimitor use slicing directly
# join list to string based on delimitor