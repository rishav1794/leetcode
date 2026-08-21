class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)):
            lookup = {}
            for j in range(len(matrix[i])):
                value = matrix[i][j]

                if value in lookup:
                    return False
                lookup[value] = 1

        for i in range(len(matrix)):
            lookup = {}
            for j in range(len(matrix[i])):
                value = matrix[j][i]
            
                if value in lookup:
                    return False
            
                lookup[value] = 1
        
        return True
