class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        previous = [1]
        result = [previous]
        for i in range(numRows - 1):
            current = []
            current.append(1)
            for j in range(len(previous)-1):
                current.append(previous[j]+previous[j+1])
            current.append(1)
            previous = current
            result.append(current)
        return result
