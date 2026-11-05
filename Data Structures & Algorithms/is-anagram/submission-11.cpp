class Solution {
public:
    bool isAnagram(string s, string t) {

        if (s.size() != t.size()){
            return false;
        }

        vector<int> charmap(26, 0);

        for(const char c : s){
            charmap[c-'a']++;
        }

        for(const char c : t){
            charmap[c-'a']--;

            if (charmap[c-'a']<0){
                return false;
            }
        }

        return true;
    }
};
