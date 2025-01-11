class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        q = []
        v = set()

        m = len(grid)
        n = len(grid[0])
        
        q1 = []

        oranges = set()
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    q1.append((row,col))
                if grid[row][col] != 0:
                    oranges.add((row, col))

        q.append(q1)

        count = 0
        while len(q) != 0:
            stage = q.pop()
            next_stage = []

            while len(stage) != 0:
                pos = stage.pop()
                row = pos[0]
                col = pos[1]
                
                v.add((row, col))
    
                new_pos = [
                    (row, col + 1),
                    (row, col - 1),
                    (row + 1, col),
                    (row - 1, col)
                ]

                for new_row, new_col in new_pos:
                    if new_row < 0 or new_row >= m:
                        continue
                    if new_col < 0 or new_col >= n:
                        continue
                    if (new_row, new_col) in v:
                        continue
                    if (new_row, new_col) in stage:
                        continue
                    if grid[new_row][new_col] != 1:
                        continue
                    
                    next_stage.append((new_row, new_col))
            if len(next_stage) != 0:
                count += 1
                q.append(next_stage)

        return count if v == oranges else -1

print(Solution().orangesRotting([[2,2],[1,1],[0,0],[2,0]])) # 4