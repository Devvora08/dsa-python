def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r = 0
        c = len(matrix[r]) -1 

        while r < len(matrix) and c >= 0:
            mid = matrix[r][c]
            
            if target == mid:
                return True
            elif target < mid:
                c -= 1
            else: 
                r += 1
        
        return False