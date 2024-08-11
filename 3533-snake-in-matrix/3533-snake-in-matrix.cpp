class Solution {
public:
    int finalPositionOfSnake(int n, vector<string>& commands) {
        int row = 0;
        int col = 0;

        for(string s : commands){
            
            if (s=="DOWN")
                col++;        
            else if(s=="RIGHT")
                row++;
            else if (s=="LEFT")
                row--;
            else if (s=="UP")
                col--;
        }
        return (col*n)+row;
    }
};