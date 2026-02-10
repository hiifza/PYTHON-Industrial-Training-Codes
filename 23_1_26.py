# Date: 23/01/26
# Problems:
# 387. First Unique Character in a String
# 303. Range Sum Query - Immutable
# 704. Binary Search
# 387. First Unique Character in a String

class Solution387:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1


# --------------------------------------------------
# 303. Range Sum Query - Immutable
# --------------------------------------------------

class NumArray:
    def __init__(self, nums):
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]


# --------------------------------------------------
# 704. Binary Search
# --------------------------------------------------

class Solution704:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


# --------------------------------------------------
# MAIN PROGRAM (User Input)
# --------------------------------------------------

if __name__ == "__main__":

    print("Choose Problem to Run:")
    print("1. First Unique Character in a String")
    print("2. Range Sum Query - Immutable")
    print("3. Binary Search")

    choice = int(input("Enter your choice (1/2/3): "))

    # ---------------- Problem 387 ----------------
    if choice == 1:
        s = input("Enter the string: ")
        sol = Solution387()
        result = sol.firstUniqChar(s)
        print("Index of first unique character:", result)

    # ---------------- Problem 303 ----------------
    elif choice == 2:
        nums = list(map(int, input("Enter array elements (space-separated): ").split()))
        numArray = NumArray(nums)

        q = int(input("Enter number of queries: "))
        for _ in range(q):
            left, right = map(int, input("Enter left and right indices: ").split())
            print("Sum:", numArray.sumRange(left, right))

    # ---------------- Problem 704 ----------------
    elif choice == 3:
        nums = list(map(int, input("Enter sorted array elements: ").split()))
        target = int(input("Enter target value: "))
        sol = Solution704()
        result = sol.search(nums, target)
        print("Index of target:", result)

    else:
        print("Invalid choice!")
