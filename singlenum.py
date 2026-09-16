class solution:
    def __init__(self, nums):
        self.nums = nums

    def singlenum(self):
        result = 0

        for num in self.nums:
            result ^= num

        return result

single = solution([4, 2, 1, 2, 1])
print(single.singlenum())