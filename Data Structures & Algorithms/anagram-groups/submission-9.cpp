class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> res;

        for(string& s : strs){

            vector<int> count(26, 0);

            for(char c : s){
                count[c-'a']++;
            }

            string key;
            for(int n:count){
                key += to_string(n)+"#";
            }

            res[key].push_back(s);
        }

        vector<vector<string>> result;

        for(auto& [key, words]: res){
            result.push_back(words);
        }

        return result;
    }
};
