class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # # 1. Initialize our DP array with the very bottom row of the triangle
        # dp=triangle[-1][:]

        # # 2. Start from the second-to-last row and iterate upwards to row 0
        # for row in range(len(triangle)-2,-1,-1):
        #     # 3. Iterate through every element in the current row
        #     for i in range(len(triangle[row])):
        #         # The minimum path sum from this specific node is its own value
        #         # PLUS the smaller of the two possible paths directly below it.
        #         # dp[i] is the left child, dp[i + 1] is the right child.
        #         dp[i]=triangle[row][i]+min(dp[i],dp[i+1])

        # # 4. Once the loops finish, the top element (index 0) holds the final answer
        # return dp[0]

        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(
                    triangle[row + 1][col], triangle[row + 1][col + 1]
                )
        return triangle[0][0]

