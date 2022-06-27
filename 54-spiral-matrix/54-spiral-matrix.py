class Solution:
    def spiralOrder(self, matrix):
        output = []
        if matrix == []:
            return output
        row = len(matrix)
        col = len(matrix[0])
        top = 0
        right = col-1
        left = 0
        bottom = row-1
        direction = 0
        while len(output) < (row*col):
            if direction == 0:
                # left to right
                for j in range(left, right + 1):
                    output.append(matrix[top][j])
                top += 1
            elif direction == 1:
                # top to bottom
                for i in range(top, bottom + 1):
                    output.append(matrix[i][right])
                right -= 1
            elif direction == 2:
                # right to left
                for j in range(right, left-1, -1):
                    output.append(matrix[bottom][j])
                bottom -= 1
            else:
                # bottom to top
                for i in range(bottom, top-1, -1):
                    output.append(matrix[i][left])
                left += 1
            direction = (direction + 1) % 4
        return output