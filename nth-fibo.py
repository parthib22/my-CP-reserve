class Solution:
    def nthFibonacci(self, n: int) -> int:
        # code here
        x = 0
        y = 1
        for i in range(n):
            x = x + y
            y = x - y
        return x


if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
    n = int(input())

    obj = Solution()
    res = obj.nthFibonacci(n)

    print(res)
