class TicTacToe {
public:
    vector<int> rows;
    vector<int> cols;
    int diagonal=0;
    int antiDiagonal=0;

    TicTacToe(int n) {
        rows.assign(n, 0);
        cols.assign(n, 0);
        diagonal = 0;
        antiDiagonal = 0;    
    }
    
    int move(int row, int col, int player) {
        int currentPlayer = player==1 ? 1 : -1;

        // update row and col
        rows[row] += currentPlayer;
        cols[col] += currentPlayer;

        // update diagonal
        if (row == col){
            diagonal += currentPlayer;
        }
        // update anti-diagonal
        if (col == (cols.size()-row-1)){
            antiDiagonal += currentPlayer;
        }

        int n = rows.size();
        
        if (abs(rows[row])==n || abs(cols[col])==n || abs(diagonal)==n || abs(antiDiagonal)==n){
            return player;
        }
        
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
