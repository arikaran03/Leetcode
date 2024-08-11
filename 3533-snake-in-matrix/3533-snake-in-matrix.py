class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        row = 0
        col = 0

        for i in commands:

            if i == "DOWN":
                col +=1        
            elif i == "RIGHT":
                row+=1
            elif i == "LEFT":
                row-=1
            elif i == "UP":
                col-=1
        
        return (col*n)+row