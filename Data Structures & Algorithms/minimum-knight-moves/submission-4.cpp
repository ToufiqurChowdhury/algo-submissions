class Solution {
public:
    int minKnightMoves(int x, int y) {
        x = abs(x);
        y = abs(y);

        vector<pair<int, int>> moves = {
            {1, 2}, {2, 1}, {2, -1}, {1, -2},
            {-1, -2}, {-2, -1}, {-2, 1}, {-1, 2}
        };

        queue<pair<int,int>> q;
        //unordered_set<string> visited;
        set<pair<int, int>> visited;
        q.push({0,0});
        //visited.insert("0,0");
        visited.insert({0,0});
        
        int steps = 0;
        while (!q.empty()) {
            int qsize = q.size();

            while (qsize--) {
                auto [cx,cy] = q.front(); q.pop();

                if (cx==x && cy==y) {
                    return steps;
                }

                for (auto [dx, dy] : moves) {
                    int nx = cx+dx;
                    int ny = cy+dy;

                    if (nx<-2 || ny < -2 || nx> x+2 || ny > y+2){
                        continue;
                    }

                    //string key = to_string(nx) + "," +to_string(ny);
                    pair<int, int> keypair = {nx,ny};
                    if (!visited.count(keypair)) {
                        visited.insert(keypair);
                        q.push({nx,ny});
                    }
                } 
            }

            steps++;
        }

        return -1;
        
    }
};
