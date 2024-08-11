class Solution {
    public int finalPositionOfSnake(int n, List<String> commands) {
        int row = 0;
        int col = 0;

        for(String s : commands){
            if (s.equals("DOWN"))
                col++;        
            else if(s.equals ("RIGHT"))
                row++;
            else if (s.equals("LEFT"))
                row--;
            else if (s.equals("UP"))
                col--;
        }
        return (col*n)+row;
    }   
}