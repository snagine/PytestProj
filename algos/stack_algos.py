class StackAlgos:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and abs(ord(stack[-1]) - ord(s[i])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)

    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        for i in range(len(nums1)):
            # next_gen = -1
            if nums1[i] in nums2:
                pos = nums2.index(nums1[i]) # get the index
                if pos == len(nums2) - 1 or nums2[pos] > nums2[pos + 1]:
                    next_gen = -1
                else:
                    next_gen = nums2[pos + 1]
                stack.append(next_gen)
        return stack


from collections import deque
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()

    def next(self, val: int) -> float:
        if self.size - 1 < len(self.queue):
            self.queue.popleft()
        self.queue.append(val)
        return round(sum(self.queue) / len(self.queue), 2)

stack_algos = StackAlgos()
# print(stack_algos.makeGood(("leEeetcode")))
#"leEeetcode"-> leetcode
# abBAcC -> ""
# "s" -> "s"

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(2)
# param_1 = obj.next(1)
# param_2 = obj.next(10)
# param_3 = obj.next(3)
# param_3 = obj.next(5)
# param_4 = obj.next(4)
# print(param_1)
# print(param_2)
# print(param_3)
# print(param_4)

res = stack_algos.nextGreaterElement([4,1,2], [1,3,4,2])
print(res)