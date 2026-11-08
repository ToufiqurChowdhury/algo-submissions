class Solution {
    unordered_map<int, vector<int>> preMap;
    unordered_set<int> cycle, visit;

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        // init preMap;
        for (int i=0; i<numCourses; i++) {
            preMap[i] = {};
        }

        // prepare adjacency list
        for (const auto& prereq : prerequisites) {
            preMap[prereq[0]].push_back(prereq[1]);
        }

        for (int i=0; i<numCourses; i++){
            if (!dfs(i)){
                return false;
            }
        }
        
        return true;
    }

    bool dfs(int crs) {

        if (cycle.count(crs)) {
            return false;
        }

        if (visit.count(crs)){
            return true;
        }

        cycle.insert(crs);
        for (int pre : preMap[crs]){
            if (!dfs(pre)){
                return false;
            }
        }
        cycle.erase(crs);
        visit.insert(crs);

        return true;
    }
};
