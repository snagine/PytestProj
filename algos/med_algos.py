from math import ceil


class MedAlgos:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True

                for dx, dy in directions:
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))

            return False

        m = len(heights)
        n = len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def isInThreshold(k):
            threshold_inner = 0
            for num in nums:
                threshold_inner += ceil((1.0 * num) / k)
            return threshold_inner <= threshold

        left = 1  # 0
        right = max(nums)  # 9

        while left <= right:  # [1,2,5,9]
            mid = (left + right) // 2  # 5, 2
            if isInThreshold(mid):
                right = mid - 1  # 5
            else:
                left = mid + 1  # 1
        return left




med_algos = MedAlgos()

# heights = [[1,2,3],[3,8,4],[5,3,5]]
# res = med_algos.smallestDivisor(heights)


nums =  [1,2,5,9] #[44,22,33,11,1]
threshold = 6 #5

res = med_algos.smallestDivisor(nums, threshold)
print(res)