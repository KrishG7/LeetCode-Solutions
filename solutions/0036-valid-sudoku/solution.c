bool isValidSudoku(char** board, int boardSize, int* boardColSize) {
    bool rows[9][9] = {false}, cols[9][9] = {false}, boxes[9][9] = {false};
    for(int i=0;i<boardSize;i++){
        for(int j=0;j<boardSize;j++){
            if(board[i][j]!='.'){
                int num=board[i][j]-'1';
                int k = (i / 3) * 3 + (j / 3);
                if (rows[i][num] || cols[j][num] || boxes[k][num]) 
                    return false;
                
                rows[i][num] = cols[j][num] = boxes[k][num] = true;
            }
        }
    }
    return true;
}
