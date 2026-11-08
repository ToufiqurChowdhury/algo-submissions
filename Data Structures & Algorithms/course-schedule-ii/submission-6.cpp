// Allah, please help.

class Solution {
    unordered_map<int, vector<int>> preMap;
    unordered_set<int> cycle, visit;
    vector<int> res;

public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        for (int i=0; i<numCourses; i++) {
            preMap[i] = {};
        }    

        for (const auto& prereq : prerequisites) {
            preMap[prereq[0]].push_back(prereq[1]);
        }

        for (int i=0; i<numCourses; i++) {
            if(!dfs(i)) {
                return {};
            }
        }

        return res;
    }

    bool dfs(int crs){

        if (cycle.count(crs)) {
            return false;
        }

        if (visit.count(crs)) {
            return true;
        }

        cycle.insert(crs);
        for (int pre : preMap[crs]) {
            if (!dfs(pre)) {
                return false;
            }
        }
        cycle.erase(crs);
        visit.insert(crs);
        res.push_back(crs);

        return true;
    }
};
