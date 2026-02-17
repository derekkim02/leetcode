class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rows = len(image)
        cols = len(image[0])


        queue = [(sr,sc)]
        
        original_color = image[sr][sc]

        if original_color == color:
            return image

        while queue:
            r, c = queue.pop(0)
            if image[r][c] != original_color:
                continue
            if r + 1 < rows:
                queue.append((r + 1, c))
            if r - 1 >= 0:
                queue.append((r - 1, c))
            if c + 1 < cols:
                queue.append((r, c + 1))
            if c - 1 >= 0:
                queue.append((r, c - 1))

            image[r][c] = color
        return image

            